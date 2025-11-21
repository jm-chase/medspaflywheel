#!/usr/bin/env python3
"""
Fix broken links across all HTML files
Fixes:
- State abbreviation links (FL.html, GA.html, etc.) -> locations.html
- Non-existent case study links -> case-studies.html
- Category template links -> blog.html
- Template placeholders
"""

import re
from pathlib import Path


def fix_links_in_file(file_path):
    """Fix broken links in a single HTML file"""

    print(f"Processing {file_path.name}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # Fix 1: State abbreviation links -> locations.html
    state_abbrevs = ['AL', 'FL', 'GA', 'NC', 'SC', 'TN', 'VA']
    for state in state_abbrevs:
        old_link = f'href="/{state}.html"'
        new_link = 'href="/locations.html"'
        if old_link in content:
            content = content.replace(old_link, new_link)
            changes.append(f"  ✓ Fixed: /{state}.html → /locations.html")

    # Fix 2: Non-existent case study links -> case-studies.html
    # Pattern 1: /case-study-{anything}-{city}-{state}-{anything}.html
    case_study_pattern1 = r'href="/case-study-[a-z-]+-(?:al|fl|ga|nc|sc|tn|va)-[a-z-]+\.html"'
    case_study_matches1 = re.findall(case_study_pattern1, content)
    if case_study_matches1:
        content = re.sub(case_study_pattern1, 'href="/case-studies.html"', content)
        changes.append(f"  ✓ Fixed: {len(case_study_matches1)} case study links (type 1) → /case-studies.html")

    # Pattern 2: /case-study-{client}-{city}-{state}.html (without third part)
    case_study_pattern2 = r'href="/case-study-[a-z-]+-[a-z-]+-(?:al|fl|ga|nc|sc|tn|va)\.html"'
    case_study_matches2 = re.findall(case_study_pattern2, content)
    if case_study_matches2:
        content = re.sub(case_study_pattern2, 'href="/case-studies.html"', content)
        changes.append(f"  ✓ Fixed: {len(case_study_matches2)} case study links (type 2) → /case-studies.html")

    # Pattern 3: Any remaining case-study-*.html that doesn't exist
    case_study_pattern3 = r'href="/case-study-\[CLIENT_SLUG_[0-9]\]\.html"'
    case_study_matches3 = re.findall(case_study_pattern3, content)
    if case_study_matches3:
        content = re.sub(case_study_pattern3, 'href="/case-studies.html"', content)
        changes.append(f"  ✓ Fixed: {len(case_study_matches3)} case study placeholder links → /case-studies.html")

    # Fix 3: Category template links -> blog.html
    old_category = 'href="/category-template.html"'
    new_category = 'href="/blog.html"'
    category_count = content.count(old_category)
    if category_count > 0:
        content = content.replace(old_category, new_category)
        changes.append(f"  ✓ Fixed: {category_count} category template links → /blog.html")

    # Fix 4: Template placeholder links
    # [STATE_ABBREV].html -> locations.html
    old_placeholder1 = 'href="/[STATE_ABBREV].html"'
    if old_placeholder1 in content:
        content = content.replace(old_placeholder1, 'href="/locations.html"')
        changes.append(f"  ✓ Fixed: [STATE_ABBREV] placeholder → /locations.html")

    # Fix 5: Canonical URL placeholders in city pages
    # e.g., https://medspaflywheel.com/miami-fl-FL.html -> https://medspaflywheel.com/miami-fl.html
    canonical_pattern = r'https://medspaflywheel\.com/([a-z-]+)-([a-z]{2})-\2\.html'
    canonical_replacement = r'https://medspaflywheel.com/\1-\2.html'
    canonical_matches = re.findall(canonical_pattern, content)
    if canonical_matches:
        content = re.sub(canonical_pattern, canonical_replacement, content)
        changes.append(f"  ✓ Fixed: {len(canonical_matches)} duplicate state codes in canonical URLs")

    # Write back if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ Updated {file_path.name}")
        for change in changes:
            print(change)
        return True
    else:
        print(f"  ⏭️  No broken links in {file_path.name}")
        return False


def main():
    """Fix broken links in all HTML files"""
    site_root = Path(__file__).parent.parent

    print("🔧 MedSpa Flywheel Link Fixer\n")
    print(f"📁 Site root: {site_root}\n")

    # Find all HTML files
    html_files = sorted(site_root.glob('*.html'))

    if not html_files:
        print("❌ No HTML files found!")
        return

    print(f"📝 Fixing links in {len(html_files)} HTML files...\n")
    print("="*70 + "\n")

    updated_count = 0
    skipped_count = 0

    for html_file in html_files:
        if fix_links_in_file(html_file):
            updated_count += 1
        else:
            skipped_count += 1
        print()  # Blank line between files

    print("="*70)
    print(f"📊 LINK FIX SUMMARY")
    print("="*70)
    print(f"✅ Files updated: {updated_count}")
    print(f"⏭️  Files skipped (no broken links): {skipped_count}")
    print(f"📁 Total files processed: {len(html_files)}")
    print("="*70)

    if updated_count > 0:
        print("\n💡 Next steps:")
        print("   1. Run link checker again to verify: python3 scripts/check-links.py")
        print("   2. Test navigation on a sample page")
        print("   3. Commit changes: git add . && git commit -m 'Fix broken internal links'")

    print("\n✅ Done!\n")


if __name__ == '__main__':
    main()
