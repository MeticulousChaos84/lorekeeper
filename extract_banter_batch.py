#!/usr/bin/env python3
"""Extract party banter dialogue files for Gale and Astarion.

Processes banter HTML files and extracts dialogue in narrative flow format
per extraction guidelines.
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

def clean_dialog_text(text):
    """Clean dialog text, preserving italics and formatting."""
    text = text.replace('&#39;', "'")
    text = text.replace('&quot;', '"')
    text = text.replace('&amp;', '&')
    return text.strip()

def extract_node_data(li):
    """Extract data from a dialogue node."""
    data = {}

    # Get node ID
    nodeid_span = li.find('span', class_='nodeid')
    if nodeid_span:
        data['id'] = nodeid_span.text.strip().rstrip('.')

    # Get speaker
    npc_div = li.find('div', class_='npc')
    npcplayer_span = li.find('span', class_='npcplayer')
    if npc_div:
        data['speaker'] = npc_div.text.strip()
    elif npcplayer_span:
        data['speaker'] = npcplayer_span.text.strip()

    # Get dialogue
    dialog_span = li.find('span', class_='dialog')
    if dialog_span:
        # Check for italic tags
        if dialog_span.find('i'):
            data['dialog'] = f"*{clean_dialog_text(dialog_span.get_text())}*"
        else:
            data['dialog'] = clean_dialog_text(dialog_span.get_text())

    # Get tags (for filtering)
    ruletag_span = li.find('span', class_='ruletag')
    if ruletag_span:
        data['tag'] = ruletag_span.get('title', '')

    # Get devnote/context
    context_span = li.find('span', class_='context')
    if context_span:
        data['context'] = context_span.get('title', '')

    # Check for God Gale flags (EXCLUDE these)
    checkflag_spans = li.find_all('span', class_='checkflag')
    setflag_spans = li.find_all('span', class_='setflag')
    data['is_god_gale'] = any('BeMyGod' in str(span) or 'GodGale' in str(span)
                               for span in checkflag_spans + setflag_spans)

    # Check for Ascended Astarion flags (EXCLUDE these)
    data['is_ascended'] = any('BecameVampireLord' in str(span) or 'AscendedAstarion' in str(span)
                               for span in checkflag_spans + setflag_spans)

    return data

def should_include_player_line(node_data):
    """Check if player dialogue should be included per rules."""
    if 'tag' not in node_data:
        return False  # For banter, typically exclude untagged player dialogue

    tag = node_data['tag'].lower()
    # Include only SORCERER, WILD_SORCERER, REALLY_GALE, REALLY_ASTARION
    if any(x in tag for x in ['sorcerer', 'really_astarion', 'really_gale']):
        return True

    # Exclude class/race tags
    excluded_tags = ['wizard', 'warlock', 'cleric', 'ranger', 'barbarian', 'fighter',
                     'githyanki', 'drow', 'tiefling', 'half-elf', 'halfling', 'dark_urge']
    if any(x in tag for x in excluded_tags):
        return False

    return False  # Default exclude

def format_dialogue_line(node_data):
    """Format a single dialogue line for markdown output."""
    speaker = node_data.get('speaker', '')
    dialog = node_data.get('dialog', '')

    if not dialog:
        return None

    # Format based on speaker
    if speaker:
        return f"**{speaker}:** {dialog}"
    else:
        return dialog

def get_synopsis(soup):
    """Extract synopsis from HTML if available."""
    synopsis_span = soup.find('span', class_='synopsis')
    if synopsis_span:
        return clean_dialog_text(synopsis_span.get_text())
    return None

def determine_output_path(input_file):
    """Determine output path based on input filename."""
    filename = input_file.stem  # e.g., PB_Gale_Astarion_ROM_Act1

    # Parse filename to determine character and location
    parts = filename.split('_')

    # Determine primary character(s)
    # Files are named like: PB_Character1_Character2_Location
    if len(parts) >= 3:
        char1 = parts[1].lower()
        char2 = parts[2].lower()

        # Determine subdirectory based on characters involved
        if char1 == 'gale' and char2 == 'astarion':
            subdir = 'gale/banter'
        elif char1 == 'astarion' and char2 == 'gale':
            subdir = 'astarion/banter'
        elif char1 == 'gale':
            subdir = 'gale/banter'
        elif char1 == 'astarion':
            subdir = 'astarion/banter'
        elif char2 == 'gale':
            subdir = 'gale/banter'
        elif char2 == 'astarion':
            subdir = 'astarion/banter'
        else:
            subdir = 'other/banter'

        # Create cleaner filename
        # Convert PB_Gale_Astarion_ROM_Act1 -> gale_astarion_romance_act1
        clean_name = filename.lower().replace('pb_', '')
        clean_name = clean_name.replace('rom_', 'romance_')
        clean_name = clean_name.replace('_act', '_act')

        output_path = Path(f"/home/user/lorekeeper/extracted_dialogue/{subdir}/{clean_name}.md")
        return output_path

    return None

def extract_banter(input_file):
    """Extract dialogue from a single banter HTML file."""
    print(f"\nProcessing: {input_file.name}")

    with open(input_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Get synopsis
    synopsis = get_synopsis(soup)

    # Parse all nodes
    all_lis = soup.find_all('li')
    nodes = []

    for li in all_lis:
        data = extract_node_data(li)
        if 'dialog' in data:
            nodes.append(data)

    # Filter nodes
    filtered_nodes = []
    for node in nodes:
        # Skip God Gale paths
        if node.get('is_god_gale'):
            continue

        # Skip Ascended Astarion paths
        if node.get('is_ascended'):
            continue

        # For player dialogue, apply tag filtering
        speaker = node.get('speaker', '')
        if speaker in ['', 'Player', 'Tav']:
            if should_include_player_line(node):
                filtered_nodes.append(node)
        else:
            # Include NPC dialogue
            filtered_nodes.append(node)

    if not filtered_nodes:
        print(f"  ⚠️  No dialogue extracted (may be filtered or empty)")
        return None

    # Determine output path
    output_file = determine_output_path(input_file)
    if not output_file:
        print(f"  ⚠️  Could not determine output path")
        return None

    # Create output directory
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        # Title
        title = input_file.stem.replace('PB_', '').replace('_', ' ').title()
        f.write(f"# Party Banter: {title}\n\n")

        # Synopsis if available
        if synopsis:
            f.write(f"*{synopsis}*\n\n")

        f.write("---\n\n")

        # Write dialogue
        for node in filtered_nodes:
            line = format_dialogue_line(node)
            if line:
                f.write(f"{line}\n\n")

    print(f"  ✓ Extracted {len(filtered_nodes)} lines -> {output_file.relative_to(Path('/home/user/lorekeeper'))}")
    return output_file

def main():
    banter_dir = Path("/home/user/lorekeeper/dialogs/banter")

    # Get all banter files involving Gale or Astarion
    all_files = sorted(banter_dir.glob("*.html"))

    # Filter for Gale and Astarion files
    target_files = [f for f in all_files
                    if 'Gale' in f.name or 'Astarion' in f.name]

    print(f"Found {len(target_files)} banter files to extract\n")
    print("=" * 60)

    extracted_count = 0
    skipped_count = 0

    for input_file in target_files:
        result = extract_banter(input_file)
        if result:
            extracted_count += 1
        else:
            skipped_count += 1

    print("\n" + "=" * 60)
    print(f"\n✓ Extraction complete!")
    print(f"  Extracted: {extracted_count} files")
    print(f"  Skipped: {skipped_count} files")

if __name__ == "__main__":
    main()
