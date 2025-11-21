#!/usr/bin/env python3
"""
Script to add favicon links to all HTML files
Adds favicon meta tags to the <head> section of each HTML file
"""

import re
from pathlib import Path

# Favicon HTML to insert
FAVICON_HTML = '''    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="images/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="192x192" href="images/android-chrome-192x192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="images/android-chrome-512x512.png">
'''

def add_favicon_to_file(file_path):
    """Add favicon links to a single HTML file"""

    print(f"Processing {file_path.name}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if favicon links already exist
    if 'favicon.ico' in content or 'apple-touch-icon' in content:
        print(f"  ⏭️  Favicon links already exist in {file_path.name}")
        return False

    # Find the closing </head> tag and insert favicon links before it
    # We'll insert it right before </head>
    head_pattern = r'(\s*)</head>'

    match = re.search(head_pattern, content, re.IGNORECASE)
    if not match:
        print(f"  ❌ Could not find </head> tag in {file_path.name}")
        return False

    # Insert favicon HTML before </head>
    updated_content = re.sub(
        head_pattern,
        f'\n{FAVICON_HTML}\\1</head>',
        content,
        count=1,
        flags=re.IGNORECASE
    )

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"  ✅ Added favicon links to {file_path.name}")
    return True

def main():
    """Add favicon links to all HTML files"""
    site_root = Path(__file__).parent.parent

    print("🚀 Starting favicon link addition...\n")
    print(f"📁 Site root: {site_root}\n")

    # Find all HTML files
    html_files = sorted(site_root.glob('*.html'))

    if not html_files:
        print("❌ No HTML files found!")
        return

    print(f"📝 Found {len(html_files)} HTML files to process\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    for html_file in html_files:
        result = add_favicon_to_file(html_file)
        if result is True:
            updated_count += 1
        elif result is False:
            skipped_count += 1
        else:
            error_count += 1

    print("\n" + "="*60)
    print(f"📊 FAVICON LINK UPDATE SUMMARY")
    print("="*60)
    print(f"✅ Files updated: {updated_count}")
    print(f"⏭️  Files skipped (already have favicon): {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📁 Total files processed: {len(html_files)}")
    print("="*60)

    if updated_count > 0:
        print("\n💡 Next steps:")
        print("   1. Make sure favicon files exist in the images/ directory:")
        print("      - images/favicon.ico")
        print("      - images/favicon-16x16.png")
        print("      - images/favicon-32x32.png")
        print("      - images/apple-touch-icon.png")
        print("      - images/android-chrome-192x192.png")
        print("      - images/android-chrome-512x512.png")
        print("   2. If you haven't created them yet, see CREATE-FAVICON.md")
        print("   3. Test locally: npm run dev")
        print("   4. Check favicon in browser tab")
        print("   5. Commit: git add images/*.{ico,png} *.html")
        print("   6. Push: git commit -m 'Add favicon to all pages' && git push")

    print("\n✅ Done!\n")

if __name__ == '__main__':
    main()
