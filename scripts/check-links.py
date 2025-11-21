#!/usr/bin/env python3
"""
Link Checker Script for MedSpa Flywheel Website
Checks all internal links across all HTML files
"""

import re
from pathlib import Path
from collections import defaultdict

def extract_links(file_path):
    """Extract all href links from an HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match href attributes
    # Matches: href="something" or href='something'
    pattern = r'href=["\'](.*?)["\']'
    links = re.findall(pattern, content)

    return links

def categorize_links(links):
    """Categorize links into internal, external, anchor, and special"""
    categorized = {
        'internal': [],
        'external': [],
        'anchor': [],
        'special': [],
        'tel': [],
        'mailto': []
    }

    for link in links:
        if link.startswith('#'):
            categorized['anchor'].append(link)
        elif link.startswith('tel:'):
            categorized['tel'].append(link)
        elif link.startswith('mailto:'):
            categorized['mailto'].append(link)
        elif link.startswith('http://') or link.startswith('https://'):
            categorized['external'].append(link)
        elif link == '/' or link.endswith('.html'):
            categorized['internal'].append(link)
        else:
            categorized['special'].append(link)

    return categorized

def check_internal_link_exists(link, site_root):
    """Check if an internal HTML file exists"""
    if link == '/':
        # Root link, should be index.html
        return (site_root / 'index.html').exists()

    # Remove leading slash if present
    link_clean = link.lstrip('/')

    # Check if file exists
    return (site_root / link_clean).exists()

def main():
    """Check all links in all HTML files"""
    site_root = Path(__file__).parent.parent

    print("🔍 MedSpa Flywheel Link Checker\n")
    print(f"📁 Site root: {site_root}\n")

    # Find all HTML files
    html_files = sorted(site_root.glob('*.html'))

    if not html_files:
        print("❌ No HTML files found!")
        return

    print(f"📝 Checking {len(html_files)} HTML files...\n")
    print("="*70)

    all_broken_links = []
    all_internal_links = set()
    all_external_links = set()
    files_with_issues = []

    for html_file in html_files:
        links = extract_links(html_file)
        categorized = categorize_links(links)

        # Check internal links
        broken_links = []
        for internal_link in categorized['internal']:
            all_internal_links.add(internal_link)
            if not check_internal_link_exists(internal_link, site_root):
                broken_links.append(internal_link)

        # Track external links
        for ext_link in categorized['external']:
            all_external_links.add(ext_link)

        if broken_links:
            files_with_issues.append(html_file.name)
            print(f"\n❌ {html_file.name}")
            print(f"   Broken links found:")
            for broken in broken_links:
                print(f"      - {broken}")
                all_broken_links.append((html_file.name, broken))

    # Summary
    print("\n" + "="*70)
    print("📊 LINK CHECK SUMMARY")
    print("="*70)

    print(f"\n📄 Files checked: {len(html_files)}")
    print(f"🔗 Unique internal links found: {len(all_internal_links)}")
    print(f"🌐 Unique external links found: {len(all_external_links)}")

    if all_broken_links:
        print(f"\n❌ Broken links found: {len(all_broken_links)}")
        print(f"📁 Files with issues: {len(files_with_issues)}")
        print("\nBroken links by file:")
        current_file = None
        for file, link in all_broken_links:
            if file != current_file:
                print(f"\n  {file}:")
                current_file = file
            print(f"    - {link}")
    else:
        print(f"\n✅ No broken internal links found!")

    # Show common internal links
    print("\n" + "="*70)
    print("📋 COMMON INTERNAL LINKS")
    print("="*70)

    internal_sorted = sorted(all_internal_links)
    for link in internal_sorted[:20]:  # Show first 20
        exists = "✅" if check_internal_link_exists(link, site_root) else "❌"
        print(f"{exists} {link}")

    if len(internal_sorted) > 20:
        print(f"   ... and {len(internal_sorted) - 20} more")

    # Show external links
    print("\n" + "="*70)
    print("🌐 EXTERNAL LINKS (for manual review)")
    print("="*70)

    external_sorted = sorted(all_external_links)
    for link in external_sorted:
        print(f"   {link}")

    print("\n" + "="*70)

    if all_broken_links:
        print("\n⚠️  Action needed: Fix broken internal links listed above")
        return 1
    else:
        print("\n✅ All internal links are working!")
        return 0

if __name__ == '__main__':
    exit(main())
