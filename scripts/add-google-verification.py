#!/usr/bin/env python3
"""
Script to add Google Search Console verification meta tag to all HTML files
Usage: python3 scripts/add-google-verification.py "YOUR_VERIFICATION_CODE"
"""

import re
import sys
from pathlib import Path


def add_verification_to_file(file_path, verification_code):
    """Add Google verification meta tag to a single HTML file"""

    print(f"Processing {file_path.name}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if verification already exists
    if f'google-site-verification" content="{verification_code}"' in content:
        print(f"  ⏭️  Verification already exists in {file_path.name}")
        return False

    # Pattern to find the placeholder comment
    # <!-- Google Search Console Verification -->
    # <!-- Replace YOUR_VERIFICATION_CODE with the code from Google Search Console -->
    # <!-- <meta name="google-site-verification" content="YOUR_VERIFICATION_CODE"> -->
    placeholder_pattern = r'<!-- Google Search Console Verification -->\s*<!-- Replace YOUR_VERIFICATION_CODE with the code from Google Search Console -->\s*<!-- <meta name="google-site-verification" content="YOUR_VERIFICATION_CODE"> -->'

    # Replacement with actual verification tag
    replacement = f'''<!-- Google Search Console Verification -->
    <meta name="google-site-verification" content="{verification_code}">'''

    # Check if placeholder exists
    if re.search(placeholder_pattern, content, re.DOTALL):
        # Replace placeholder with actual verification tag
        updated_content = re.sub(placeholder_pattern, replacement, content, flags=re.DOTALL)

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"  ✅ Added verification to {file_path.name}")
        return True
    else:
        # Placeholder not found, try to add after <head> tag
        head_pattern = r'(<head>)'

        verification_tag = f'\n    <!-- Google Search Console Verification -->\n    <meta name="google-site-verification" content="{verification_code}">\n'

        if re.search(head_pattern, content, re.IGNORECASE):
            updated_content = re.sub(
                head_pattern,
                r'\1' + verification_tag,
                content,
                count=1,
                flags=re.IGNORECASE
            )

            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"  ✅ Added verification to {file_path.name} (after <head>)")
            return True
        else:
            print(f"  ❌ Could not find insertion point in {file_path.name}")
            return None


def main():
    """Add Google verification to all HTML files"""

    # Check if verification code was provided
    if len(sys.argv) < 2:
        print("❌ Error: Verification code not provided!")
        print("\nUsage:")
        print('  python3 scripts/add-google-verification.py "YOUR_VERIFICATION_CODE"\n')
        print("Example:")
        print('  python3 scripts/add-google-verification.py "ABC123xyz456def789ghi012jkl345mno678"\n')
        print("To get your verification code:")
        print("  1. Go to https://search.google.com/search-console/")
        print("  2. Add your property (https://medspaflywheel.com)")
        print('  3. Choose "HTML tag" verification method')
        print("  4. Copy the code (the part inside content=\"...\")")
        print("  5. Run this script with that code\n")
        sys.exit(1)

    verification_code = sys.argv[1].strip()

    # Validate verification code (basic check)
    if len(verification_code) < 20:
        print(f"⚠️  Warning: Verification code seems too short ({len(verification_code)} characters)")
        print("   Google verification codes are usually 40-60 characters long.")
        response = input("   Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)

    site_root = Path(__file__).parent.parent

    print("🚀 Starting Google Search Console verification setup...\n")
    print(f"📁 Site root: {site_root}")
    print(f"🔑 Verification code: {verification_code[:20]}...{verification_code[-10:]}\n")

    # Find all HTML files
    html_files = sorted(site_root.glob('*.html'))

    if not html_files:
        print("❌ No HTML files found!")
        sys.exit(1)

    print(f"📝 Found {len(html_files)} HTML files to process\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    for html_file in html_files:
        result = add_verification_to_file(html_file, verification_code)
        if result is True:
            updated_count += 1
        elif result is False:
            skipped_count += 1
        else:
            error_count += 1

    print("\n" + "="*60)
    print(f"📊 GOOGLE VERIFICATION SETUP SUMMARY")
    print("="*60)
    print(f"✅ Files updated: {updated_count}")
    print(f"⏭️  Files skipped (already have verification): {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📁 Total files processed: {len(html_files)}")
    print("="*60)

    if updated_count > 0:
        print("\n💡 Next steps:")
        print("   1. Commit changes:")
        print('      git add -A')
        print('      git commit -m "Add Google Search Console verification"')
        print('      git push')
        print("\n   2. Wait for Vercel to deploy (2-3 minutes)")
        print("\n   3. Verify deployment:")
        print("      - Go to https://medspaflywheel.com")
        print("      - Right-click → View Page Source")
        print("      - Search for 'google-site-verification'")
        print("      - Confirm your verification code is visible")
        print("\n   4. Complete verification in Google Search Console:")
        print("      - Go back to Google Search Console")
        print('      - Click "Verify" button')
        print("      - You should see 'Ownership verified' ✅")
        print("\n   5. Submit your sitemap:")
        print("      - In Google Search Console, go to Sitemaps")
        print("      - Enter: sitemap.xml")
        print("      - Click Submit")
        print("\n📖 For detailed instructions, see: GOOGLE-SEARCH-CONSOLE-SETUP.md")

    print("\n✅ Done!\n")


if __name__ == '__main__':
    main()
