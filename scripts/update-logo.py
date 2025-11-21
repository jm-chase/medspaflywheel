#!/usr/bin/env python3
"""
Script to update all HTML files with the real MedSpa Flywheel logo
Replaces gradient placeholder logo boxes with the actual logo image
"""

import re
from pathlib import Path

def update_logo_in_file(file_path):
    """Update logo placeholders in a single HTML file"""

    print(f"Processing {file_path.name}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern 1: Main pages with "MF" text
    # Matches: <div class="w-10 h-10 bg-gradient-to-br from-primary-600 to-primary-800 rounded-lg flex items-center justify-center">
    #              <span class="text-white font-bold text-xl">MF</span>
    #          </div>
    logo_pattern_1 = r'<div class="w-10 h-10 bg-gradient-to-br from-primary-600 to-primary-800 rounded-lg flex items-center justify-center">\s*<span class="text-white font-bold text-xl">MF</span>\s*</div>'

    # Pattern 2: City pages with SVG chart icon
    # Matches: <div class="w-10 h-10 bg-gradient-to-br from-primary-600 to-primary-700 rounded-lg flex items-center justify-center">
    #              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    #                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path>
    #              </svg>
    #          </div>
    logo_pattern_2 = r'<div class="w-10 h-10 bg-gradient-to-br from-primary-600 to-primary-700 rounded-lg flex items-center justify-center">\s*<svg[^>]*>.*?</svg>\s*</div>'

    # Replacement: actual logo image
    replacement = '<img src="images/logo/medspaflywheel.png" alt="MedSpa Flywheel Logo" class="h-10 w-auto">'

    # Try both patterns
    updated_content = content
    match_count = 0

    # Replace pattern 1 (MF text)
    matches_1 = re.findall(logo_pattern_1, updated_content)
    if matches_1:
        match_count += len(matches_1)
        updated_content = re.sub(logo_pattern_1, replacement, updated_content)

    # Replace pattern 2 (SVG icon)
    matches_2 = re.findall(logo_pattern_2, updated_content, re.DOTALL)
    if matches_2:
        match_count += len(matches_2)
        updated_content = re.sub(logo_pattern_2, replacement, updated_content, flags=re.DOTALL)

    if match_count > 0:
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"  ✅ Updated {match_count} logo placeholder(s) in {file_path.name}")
        return True
    else:
        print(f"  ⏭️  No logo placeholders found in {file_path.name}")
        return False

def main():
    """Update logos in all HTML files"""
    site_root = Path(__file__).parent.parent

    print("🚀 Starting logo update process...\n")
    print(f"📁 Site root: {site_root}")
    print(f"🖼️  Logo: images/logo/medspaflywheel.png\n")

    # Find all HTML files
    html_files = sorted(site_root.glob('*.html'))

    if not html_files:
        print("❌ No HTML files found!")
        return

    print(f"📝 Found {len(html_files)} HTML files to process\n")

    updated_count = 0
    skipped_count = 0

    for html_file in html_files:
        if update_logo_in_file(html_file):
            updated_count += 1
        else:
            skipped_count += 1

    print("\n" + "="*60)
    print(f"📊 LOGO UPDATE SUMMARY")
    print("="*60)
    print(f"✅ Files updated: {updated_count}")
    print(f"⏭️  Files skipped (no placeholders): {skipped_count}")
    print(f"📁 Total files processed: {len(html_files)}")
    print("="*60)

    if updated_count > 0:
        print("\n💡 Next steps:")
        print("   1. Test the logo display: npm run dev")
        print("   2. Check http://localhost:8000 in your browser")
        print("   3. Verify logo appears in navigation and footer")
        print("   4. Commit changes: git add . && git commit -m 'Add company logo to all pages'")

    print("\n✅ Done!\n")

if __name__ == '__main__':
    main()
