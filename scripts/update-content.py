#!/usr/bin/env python3
"""
Content Update Script for MedSpa Flywheel Website
Reads content from site-content.json and updates all HTML files
"""

import json
import re
import os
import sys
from pathlib import Path

class ContentUpdater:
    def __init__(self, content_file, site_root):
        self.site_root = Path(site_root)
        self.content_file = content_file
        self.content = self.load_content()
        self.stats = {
            'files_processed': 0,
            'replacements_made': 0,
            'errors': []
        }

    def load_content(self):
        """Load content from JSON file"""
        try:
            with open(self.content_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Error loading content file: {e}")
            sys.exit(1)

    def update_all_files(self):
        """Update all HTML files in the site"""
        print("🚀 Starting content update process...")
        print(f"📁 Site root: {self.site_root}")
        print(f"📄 Content file: {self.content_file}\n")

        # Get all HTML files
        html_files = list(self.site_root.glob('*.html'))

        print(f"📝 Found {len(html_files)} HTML files to process\n")

        for html_file in html_files:
            self.update_file(html_file)

        self.print_summary()

    def update_file(self, file_path):
        """Update a single HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Apply all replacements
            content = self.replace_contact_info(content)
            content = self.replace_social_links(content)
            content = self.replace_stats(content, file_path.name)
            content = self.replace_images(content)

            # Only write if content changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                replacements = len(original_content) - len(content) if len(content) < len(original_content) else 1
                self.stats['replacements_made'] += replacements
                print(f"✅ Updated: {file_path.name}")
            else:
                print(f"⏭️  Skipped: {file_path.name} (no changes)")

            self.stats['files_processed'] += 1

        except Exception as e:
            error_msg = f"Error processing {file_path.name}: {e}"
            self.stats['errors'].append(error_msg)
            print(f"❌ {error_msg}")

    def replace_contact_info(self, content):
        """Replace all contact information"""
        company = self.content['company']

        # Email
        content = content.replace(
            'hello@medspaflywheel.com',
            company['contact']['email']
        )

        # Phone numbers - various formats
        phone_patterns = [
            (r'\(888\) 555-1234', company['contact']['phone']),
            (r'\+1-888-555-1234', company['contact']['phoneFormatted']),
            (r'888-555-1234', company['contact']['phone'].replace('(', '').replace(') ', '-'))
        ]

        for pattern, replacement in phone_patterns:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

        return content

    def replace_social_links(self, content):
        """Replace social media URLs"""
        social = self.content['company']['social']

        replacements = {
            'https://www.facebook.com/medspaflywheel': social['facebook'],
            'https://www.instagram.com/medspaflywheel': social['instagram'],
            'https://www.linkedin.com/company/medspaflywheel': social['linkedin'],
            'https://www.twitter.com/medspaflywheel': social.get('twitter', '')
        }

        for old, new in replacements.items():
            if new:  # Only replace if new value exists
                content = content.replace(old, new)

        return content

    def replace_stats(self, content, filename):
        """Replace statistics based on file type"""

        # Homepage stats
        if filename == 'index.html':
            stats = self.content['homepage']['stats']

            # Med Spas Served
            content = re.sub(
                r'<div class="text-4xl.*?font-bold.*?>50\+</div>',
                f'<div class="text-4xl font-bold text-gray-900 mb-2">{stats["medSpasServed"]["number"]}</div>',
                content,
                flags=re.DOTALL
            )

            # Average ROI
            content = re.sub(
                r'<div class="text-4xl.*?font-bold.*?>250%</div>',
                f'<div class="text-4xl font-bold text-gray-900 mb-2">{stats["averageROI"]["number"]}</div>',
                content,
                flags=re.DOTALL
            )

            # Appointments Generated
            content = re.sub(
                r'<div class="text-4xl.*?font-bold.*?>10K\+</div>',
                f'<div class="text-4xl font-bold text-gray-900 mb-2">{stats["appointmentsGenerated"]["number"]}</div>',
                content,
                flags=re.DOTALL
            )

            # Client Rating
            content = re.sub(
                r'<div class="text-4xl.*?font-bold.*?>4\.8★</div>',
                f'<div class="text-4xl font-bold text-gray-900 mb-2">{stats["clientRating"]["number"]}</div>',
                content,
                flags=re.DOTALL
            )

        # Location pages stats
        if filename.endswith('.html') and any(city in filename for city in ['miami', 'atlanta', 'tampa', 'charlotte']):
            defaults = self.content['locationDefaults']['stats']

            # Replace location-specific stats
            content = re.sub(
                r'<div class="text-3xl font-bold text-primary-600">180%</div>',
                f'<div class="text-3xl font-bold text-primary-600">{defaults["bookingIncrease"]}</div>',
                content
            )

            content = re.sub(
                r'<div class="text-3xl font-bold text-primary-600">87</div>',
                f'<div class="text-3xl font-bold text-primary-600">{defaults["reviews"]}</div>',
                content
            )

        return content

    def replace_images(self, content):
        """Replace image paths"""
        images = self.content['images']

        # Open Graph images
        content = content.replace(
            'https://medspaflywheel.com/og-image.jpg',
            f'https://medspaflywheel.com/{images["og"]["default"]}'
        )

        content = content.replace(
            'https://medspaflywheel.com/og-blog.jpg',
            f'https://medspaflywheel.com/{images["og"]["blog"]}'
        )

        # Twitter images
        content = content.replace(
            'https://medspaflywheel.com/twitter-image.jpg',
            f'https://medspaflywheel.com/{images["twitter"]["default"]}'
        )

        # Logo
        content = re.sub(
            r'"logo\.png"',
            f'"{self.content["company"]["logo"]["path"]}"',
            content
        )

        return content

    def print_summary(self):
        """Print summary of updates"""
        print("\n" + "="*60)
        print("📊 CONTENT UPDATE SUMMARY")
        print("="*60)
        print(f"✅ Files processed: {self.stats['files_processed']}")
        print(f"🔄 Replacements made: {self.stats['replacements_made']}")

        if self.stats['errors']:
            print(f"\n❌ Errors encountered: {len(self.stats['errors'])}")
            for error in self.stats['errors']:
                print(f"   - {error}")
        else:
            print(f"\n✨ No errors encountered!")

        print("="*60)
        print("\n💡 Next steps:")
        print("   1. Review the updated HTML files")
        print("   2. Edit content/site-content.json to update content")
        print("   3. Run 'npm run build' to apply changes")
        print("   4. Test the site locally before deploying\n")


def main():
    """Main execution function"""
    # Determine paths
    script_dir = Path(__file__).parent
    site_root = script_dir.parent
    content_file = site_root / 'content' / 'site-content.json'

    # Check if content file exists
    if not content_file.exists():
        print(f"❌ Content file not found: {content_file}")
        print("   Please create content/site-content.json first!")
        sys.exit(1)

    # Create updater and run
    updater = ContentUpdater(content_file, site_root)
    updater.update_all_files()

    print("✅ Content update complete!\n")


if __name__ == '__main__':
    main()
