#!/usr/bin/env python3
"""
Formspree Setup Script
Configures contact form to use Formspree for submissions
Usage: python3 scripts/setup-formspree.py "YOUR_FORM_ID"
"""

import re
import sys
from pathlib import Path


def update_contact_form(contact_file, form_id):
    """Update contact.html with Formspree configuration"""

    print(f"Updating {contact_file.name}...")

    with open(contact_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Update 1: Add form action and method
    # Find: <form id="contact-form" class="space-y-6">
    # Replace with: <form id="contact-form" class="space-y-6" action="https://formspree.io/f/{form_id}" method="POST">

    form_pattern = r'<form id="contact-form" class="space-y-6">'
    form_replacement = f'<form id="contact-form" class="space-y-6" action="https://formspree.io/f/{form_id}" method="POST">'

    if re.search(form_pattern, content):
        content = re.sub(form_pattern, form_replacement, content)
        print(f"  ✓ Added Formspree action: https://formspree.io/f/{form_id}")
    else:
        # Check if it's already configured
        if f'action="https://formspree.io/f/' in content:
            print(f"  ⚠️  Form already has Formspree action configured")
            # Update the form ID if different
            content = re.sub(
                r'action="https://formspree\.io/f/[^"]*"',
                f'action="https://formspree.io/f/{form_id}"',
                content
            )
            print(f"  ✓ Updated Form ID to: {form_id}")
        else:
            print("  ❌ Could not find form tag pattern")
            return False

    # Update 2: Add hidden input for redirect (optional, can also be set in Formspree dashboard)
    # Add after form opening tag
    hidden_redirect = f'''
                                <!-- Formspree Configuration -->
                                <input type="hidden" name="_next" value="https://medspaflywheel.com/thank-you.html">
                                <input type="hidden" name="_subject" value="New Lead from MedSpa Flywheel Contact Form">
                                <input type="hidden" name="_cc" value="">
                                '''

    # Check if hidden inputs already exist
    if '_next' not in content:
        # Insert after the form opening tag
        insert_pattern = r'(<form[^>]*>)'
        content = re.sub(insert_pattern, r'\1' + hidden_redirect, content, count=1)
        print("  ✓ Added hidden fields for redirect and subject")
    else:
        print("  ⏭️  Hidden fields already exist")

    # Update 3: Modify JavaScript to handle Formspree submission
    # Find the form submission handler and update it

    js_pattern = r"contactForm\.addEventListener\('submit', \(e\) => \{.*?\}\);"

    js_replacement = '''contactForm.addEventListener('submit', (e) => {
            // Formspree will handle the submission
            // Show loading state
            const submitButton = contactForm.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.innerHTML;
            submitButton.innerHTML = '<svg class="animate-spin inline-block w-5 h-5 mr-2" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> Sending...';
            submitButton.disabled = true;

            // Note: Formspree will handle the actual submission
            // The form will POST to https://formspree.io/f/YOUR_FORM_ID
            // After submission, user will be redirected to thank-you.html
        });'''

    if re.search(r"contactForm\.addEventListener\('submit'", content, re.DOTALL):
        content = re.sub(js_pattern, js_replacement, content, flags=re.DOTALL)
        print("  ✓ Updated JavaScript submission handler")
    else:
        print("  ⚠️  Could not find JavaScript form handler (this is okay)")

    # Write back if changes were made
    if content != original_content:
        with open(contact_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n  ✅ Successfully configured {contact_file.name} with Formspree!")
        return True
    else:
        print(f"\n  ⏭️  No changes needed")
        return False


def main():
    """Setup Formspree for contact form"""

    # Check if Form ID was provided
    if len(sys.argv) < 2:
        print("❌ Error: Form ID not provided!\n")
        print("Usage:")
        print('  python3 scripts/setup-formspree.py "YOUR_FORM_ID"\n')
        print("Example:")
        print('  python3 scripts/setup-formspree.py "xpwzabcd"\n')
        print("To get your Form ID:")
        print("  1. Go to https://formspree.io/")
        print("  2. Sign up or log in")
        print('  3. Create a new form (click "+ New Form")')
        print('  4. Copy the Form ID from the URL (looks like "xpwzabcd")')
        print("  5. Run this script with that Form ID\n")
        print("For detailed instructions, see: SETUP-CONTACT-FORM.md\n")
        sys.exit(1)

    form_id = sys.argv[1].strip()

    # Validate Form ID (basic check)
    if len(form_id) < 4:
        print(f"⚠️  Warning: Form ID seems too short ({len(form_id)} characters)")
        print("   Formspree Form IDs are usually 8-12 characters long.")
        response = input("   Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)

    site_root = Path(__file__).parent.parent

    print("🔧 Formspree Contact Form Setup\n")
    print(f"📁 Site root: {site_root}")
    print(f"🆔 Form ID: {form_id}")
    print(f"🔗 Formspree endpoint: https://formspree.io/f/{form_id}\n")
    print("="*70 + "\n")

    # Update contact.html
    contact_file = site_root / 'contact.html'

    if not contact_file.exists():
        print(f"❌ Error: {contact_file} not found!")
        sys.exit(1)

    success = update_contact_form(contact_file, form_id)

    print("\n" + "="*70)

    if success:
        print("📊 SETUP SUMMARY")
        print("="*70)
        print("✅ Contact form configured with Formspree")
        print(f"✅ Form endpoint: https://formspree.io/f/{form_id}")
        print("✅ Redirect to thank-you page enabled")
        print("✅ Form submission ready to test")
        print("="*70)

        print("\n💡 Next steps:")
        print("   1. Commit changes:")
        print('      git add contact.html')
        print('      git commit -m "Connect contact form to Formspree"')
        print('      git push')
        print("\n   2. Wait for Vercel to deploy (2-3 minutes)")
        print("\n   3. Test your form:")
        print("      - Go to https://medspaflywheel.com/contact.html")
        print("      - Fill out and submit the form")
        print("      - First submission: confirm email (one-time setup)")
        print("      - Check your email for notification")
        print("\n   4. Configure Formspree settings:")
        print("      - Go to https://formspree.io/forms")
        print("      - Click on your form")
        print("      - Settings → Email notifications")
        print("      - Settings → After Submit → Redirect to:")
        print("        https://medspaflywheel.com/thank-you.html")
        print("\n📖 For detailed instructions, see: SETUP-CONTACT-FORM.md")

    else:
        print("📊 SETUP SUMMARY")
        print("="*70)
        print("⚠️  Form may already be configured or no changes needed")
        print("="*70)

    print("\n✅ Done!\n")


if __name__ == '__main__':
    main()
