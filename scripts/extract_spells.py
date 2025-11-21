#!/usr/bin/env python3
"""
Spell Extractor
Searches through PDF text extracts to find and format spell entries.
Outputs: Title, School, Level, Description (no mechanics)
"""

import os
import re
from pathlib import Path

# Spell schools
SCHOOLS = [
    "abjuration", "conjuration", "divination", "enchantment",
    "evocation", "illusion", "necromancy", "transmutation"
]

# Pattern to match spell headers like "1st-level evocation" or "Evocation cantrip"
LEVEL_PATTERN = re.compile(
    r'(cantrip|(?:1st|2nd|3rd|[4-9]th)-level)\s+(' + '|'.join(SCHOOLS) + r')',
    re.IGNORECASE
)

# Alternative pattern: "School cantrip" or "School"
ALT_LEVEL_PATTERN = re.compile(
    r'(' + '|'.join(SCHOOLS) + r')\s+(cantrip)',
    re.IGNORECASE
)

def extract_spell_description(text: str) -> str:
    """
    Extract just the description part of a spell, skipping mechanics.
    """
    # Skip everything up to and including Duration line
    lines = text.split('\n')
    description_lines = []
    found_duration = False

    for line in lines:
        if found_duration:
            # Skip "At Higher Levels" section (mechanics)
            if line.strip().lower().startswith("at higher levels"):
                break
            description_lines.append(line)
        elif line.strip().lower().startswith("duration"):
            found_duration = True

    return '\n'.join(description_lines).strip()

def find_spells_in_text(text: str, source_name: str) -> list:
    """
    Find spell entries in extracted text.
    Returns list of spell dictionaries.
    """
    spells = []

    # Split into potential spell blocks
    # Look for patterns where a spell name might be followed by level/school info

    # This regex looks for potential spell names (title case words)
    # followed by level/school indicators
    spell_block_pattern = re.compile(
        r'([A-Z][a-zA-Z\']+(?:\s+[A-Z][a-zA-Z\']+)*)\s*\n\s*'
        r'((?:cantrip|(?:1st|2nd|3rd|[4-9]th)-level)\s+(?:' + '|'.join(SCHOOLS) + r')|'
        r'(?:' + '|'.join(SCHOOLS) + r')\s+cantrip)',
        re.IGNORECASE | re.MULTILINE
    )

    for match in spell_block_pattern.finditer(text):
        spell_name = match.group(1).strip()
        level_school = match.group(2).strip().lower()

        # Parse level and school
        if 'cantrip' in level_school:
            level = 'Cantrip'
        else:
            level_match = re.search(r'(1st|2nd|3rd|[4-9]th)', level_school)
            level = level_match.group(1) + '-level' if level_match else 'Unknown'

        school = None
        for s in SCHOOLS:
            if s in level_school:
                school = s.capitalize()
                break

        if school:
            # Try to extract description
            # Find the text after this match until the next spell or page break
            start_pos = match.end()
            end_pos = start_pos + 2000  # Reasonable spell length

            # Look for next spell header or page break
            next_match = spell_block_pattern.search(text, start_pos)
            if next_match:
                end_pos = min(end_pos, next_match.start())

            spell_text = text[start_pos:end_pos]
            description = extract_spell_description(spell_text)

            # Only add if we got a reasonable description
            if len(description) > 20:
                spells.append({
                    'name': spell_name,
                    'level': level,
                    'school': school,
                    'description': description[:1500],  # Cap length
                    'source': source_name
                })

    return spells

def format_spell_markdown(spell: dict) -> str:
    """Format a spell entry as markdown."""
    return f"""### {spell['name']}

**Level:** {spell['level']}
**School:** {spell['school']}
**Source:** {spell['source']}

{spell['description']}

---
"""

def main():
    # Paths
    text_dir = Path("/home/user/lorekeeper/worldbuilding/text_extracts")
    output_file = Path("/home/user/lorekeeper/worldbuilding/all_spells.md")

    if not text_dir.exists():
        print("Text extracts not found. Run pdf_to_text.py first!")
        return

    # Find all text files
    text_files = list(text_dir.glob("*.txt"))
    print(f"Searching {len(text_files)} text files for spells...\n")

    all_spells = []

    for text_file in text_files:
        print(f"Scanning: {text_file.name}")

        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()

        spells = find_spells_in_text(text, text_file.stem)
        all_spells.extend(spells)
        print(f"  Found {len(spells)} spells")

    # Remove duplicates (same name)
    seen_names = set()
    unique_spells = []
    for spell in all_spells:
        if spell['name'].lower() not in seen_names:
            seen_names.add(spell['name'].lower())
            unique_spells.append(spell)

    # Sort by level then name
    def level_sort_key(spell):
        level = spell['level']
        if level == 'Cantrip':
            return (0, spell['name'])
        else:
            num = int(re.search(r'\d', level).group())
            return (num, spell['name'])

    unique_spells.sort(key=level_sort_key)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Spell Compendium\n\n")
        f.write(f"*{len(unique_spells)} spells extracted from worldbuilding sources*\n\n")
        f.write("---\n\n")

        current_level = None
        for spell in unique_spells:
            if spell['level'] != current_level:
                current_level = spell['level']
                f.write(f"\n## {current_level} Spells\n\n")

            f.write(format_spell_markdown(spell))

    print(f"\nComplete! {len(unique_spells)} unique spells saved to:")
    print(f"  {output_file}")

if __name__ == "__main__":
    main()
