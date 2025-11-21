#!/usr/bin/env python3
"""
PDF to Text Converter
Converts all PDFs in worldbuilding folder to searchable text files.
"""

import os
import pdfplumber
from pathlib import Path

def extract_text_from_pdf(pdf_path: str, output_path: str) -> bool:
    """Extract all text from a PDF and save to a text file."""
    try:
        print(f"Processing: {os.path.basename(pdf_path)}")

        with pdfplumber.open(pdf_path) as pdf:
            all_text = []
            total_pages = len(pdf.pages)

            for i, page in enumerate(pdf.pages):
                if i % 50 == 0:
                    print(f"  Page {i+1}/{total_pages}...")

                text = page.extract_text()
                if text:
                    all_text.append(f"\n--- PAGE {i+1} ---\n")
                    all_text.append(text)

        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(all_text))

        print(f"  ✓ Saved to {os.path.basename(output_path)}")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    # Paths
    worldbuilding_dir = Path("/home/user/lorekeeper/worldbuilding")
    output_dir = worldbuilding_dir / "text_extracts"

    # Create output directory
    output_dir.mkdir(exist_ok=True)

    # Find all PDFs
    pdfs = list(worldbuilding_dir.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDFs to process\n")

    # Process each PDF
    successful = 0
    failed = 0

    for pdf_path in pdfs:
        output_path = output_dir / f"{pdf_path.stem}.txt"

        if extract_text_from_pdf(str(pdf_path), str(output_path)):
            successful += 1
        else:
            failed += 1
        print()

    print(f"\nComplete! {successful} successful, {failed} failed")
    print(f"Text files saved to: {output_dir}")

if __name__ == "__main__":
    main()
