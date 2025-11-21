#!/usr/bin/env python3
"""
Script to update all city landing pages with real hero images
"""

import re
from pathlib import Path

# Map of city filename to display name for alt text
CITY_NAMES = {
    'alpharetta-ga': 'Alpharetta, GA',
    'arlington-va': 'Arlington, VA',
    'asheville-nc': 'Asheville, NC',
    'athens-ga': 'Athens, GA',
    'atlanta-ga': 'Atlanta, GA',
    'augusta-ga': 'Augusta, GA',
    'birmingham-al': 'Birmingham, AL',
    'boca-raton-fl': 'Boca Raton, FL',
    'cary-nc': 'Cary, NC',
    'chapel-hill-nc': 'Chapel Hill, NC',
    'charleston-sc': 'Charleston, SC',
    'charlotte-nc': 'Charlotte, NC',
    'chattanooga-tn': 'Chattanooga, TN',
    'chesapeake-va': 'Chesapeake, VA',
    'clearwater-fl': 'Clearwater, FL',
    'columbia-sc': 'Columbia, SC',
    'columbus-ga': 'Columbus, GA',
    'durham-nc': 'Durham, NC',
    'fort-lauderdale-fl': 'Fort Lauderdale, FL',
    'franklin-tn': 'Franklin, TN',
    'greensboro-nc': 'Greensboro, NC',
    'greenville-sc': 'Greenville, SC',
    'hilton-head-sc': 'Hilton Head, SC',
    'huntsville-al': 'Huntsville, AL',
    'jacksonville-fl': 'Jacksonville, FL',
    'knoxville-tn': 'Knoxville, TN',
    'memphis-tn': 'Memphis, TN',
    'miami-fl': 'Miami, FL',
    'mobile-al': 'Mobile, AL',
    'montgomery-al': 'Montgomery, AL',
    'myrtle-beach-sc': 'Myrtle Beach, SC',
    'naples-fl': 'Naples, FL',
    'nashville-tn': 'Nashville, TN',
    'norfolk-va': 'Norfolk, VA',
    'orlando-fl': 'Orlando, FL',
    'raleigh-nc': 'Raleigh, NC',
    'richmond-va': 'Richmond, VA',
    'sandy-springs-ga': 'Sandy Springs, GA',
    'sarasota-fl': 'Sarasota, FL',
    'savannah-ga': 'Savannah, GA',
    'tampa-fl': 'Tampa, FL',
    'virginia-beach-va': 'Virginia Beach, VA',
    'west-palm-beach-fl': 'West Palm Beach, FL',
    'winston-salem-nc': 'Winston-Salem, NC'
}

def update_city_page(file_path):
    """Update a single city landing page with the real hero image"""

    city_slug = file_path.stem  # e.g., 'miami-fl'
    city_name = CITY_NAMES.get(city_slug, city_slug.replace('-', ' ').title())

    print(f"Updating {city_slug}.html...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the placeholder hero image div
    # This matches the entire gradient placeholder div with SVG icon
    placeholder_pattern = r'<div class="aspect-\[4/3\] bg-gradient-to-br from-primary-200 via-primary-300 to-accent-200 rounded-2xl overflow-hidden shadow-2xl">\s*<div class="w-full h-full flex flex-col items-center justify-center p-8 text-center">.*?</div>\s*</div>'

    # Replacement: actual image
    replacement = f'''<div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-2xl">
                            <img src="images/cities/{city_slug}.jpg"
                                 alt="Med Spa Services in {city_name}"
                                 class="w-full h-full object-cover">
                        </div>'''

    # Replace the placeholder
    updated_content = re.sub(placeholder_pattern, replacement, content, flags=re.DOTALL)

    # Check if replacement was made
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"  ✅ Updated: {city_slug}.html")
        return True
    else:
        print(f"  ⚠️  No changes: {city_slug}.html (pattern not found)")
        return False

def main():
    """Update all city landing pages"""
    site_root = Path(__file__).parent.parent

    print("🚀 Starting city image update process...\n")

    updated_count = 0
    not_found_count = 0

    for city_slug in CITY_NAMES.keys():
        html_file = site_root / f"{city_slug}.html"

        if html_file.exists():
            if update_city_page(html_file):
                updated_count += 1
            else:
                not_found_count += 1
        else:
            print(f"  ❌ File not found: {city_slug}.html")
            not_found_count += 1

    print("\n" + "="*60)
    print(f"📊 SUMMARY")
    print("="*60)
    print(f"✅ Successfully updated: {updated_count} pages")
    print(f"⚠️  Not updated: {not_found_count} pages")
    print(f"📁 Total: {len(CITY_NAMES)} city landing pages")
    print("="*60)

    if updated_count > 0:
        print("\n💡 Next steps:")
        print("   1. Review the updated HTML files")
        print("   2. Test one or two pages locally")
        print("   3. Commit and push: git add . && git commit -m 'Add city hero images'")

    print("\n✅ Done!\n")

if __name__ == '__main__':
    main()
