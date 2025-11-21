# Contact Form Setup with Formspree

Complete guide to set up your contact form to actually receive leads!

---

## Overview

Your contact form on `/contact.html` is currently configured to use **Formspree**, a form backend service that will email you when someone submits the form.

**Benefits:**
- ✅ No server code needed
- ✅ Email notifications
- ✅ Spam protection
- ✅ Form submissions dashboard
- ✅ Free for up to 50 submissions/month
- ✅ Paid plans available for more submissions

---

## Step 1: Create Your Formspree Account

### 1.1 Sign Up

1. Go to **https://formspree.io/**
2. Click **"Sign Up"** (top right)
3. Enter your email address (use the email where you want to receive leads)
4. Create a password
5. Click **"Sign Up"**

### 1.2 Verify Your Email

1. Check your email inbox
2. Click the verification link in the email from Formspree
3. You'll be redirected to your Formspree dashboard

---

## Step 2: Create a New Form

### 2.1 Add Form to Formspree

1. In your Formspree dashboard, click **"+ New Form"**
2. Enter a name: **"MedSpa Flywheel Contact Form"**
3. Click **"Create Form"**

### 2.2 Get Your Form Endpoint

After creating the form, you'll see your form endpoint. It looks like:

```
https://formspree.io/f/YOUR_FORM_ID
```

**Example:**
```
https://formspree.io/f/xpwzabcd
```

**Copy this URL** - you'll need it in the next step.

---

## Step 3: Update Your Website

### 3.1 Option A: Automated Setup (Recommended)

Run this Python script with your Form ID:

```bash
# In WSL/Linux
cd /home/user/medspaflywheel
python3 scripts/setup-formspree.py "YOUR_FORM_ID"
```

**Example:**
```bash
python3 scripts/setup-formspree.py "xpwzabcd"
```

The script will:
- ✅ Update contact.html with your Formspree endpoint
- ✅ Configure proper form submission handling
- ✅ Add thank-you page redirect
- ✅ Show you what was changed

### 3.2 Option B: Manual Setup

If you prefer to do it manually:

1. Open `/contact.html` in a text editor

2. Find the form tag (around line 255):
   ```html
   <form id="contact-form" class="space-y-6">
   ```

3. Replace it with:
   ```html
   <form id="contact-form" class="space-y-6"
         action="https://formspree.io/f/YOUR_FORM_ID"
         method="POST">
   ```

4. Replace `YOUR_FORM_ID` with your actual Form ID from Step 2.2

---

## Step 4: Deploy Your Changes

### 4.1 Commit and Push

```bash
git add contact.html
git commit -m "Connect contact form to Formspree"
git push
```

### 4.2 Wait for Deployment

Vercel will automatically deploy your changes in 2-3 minutes.

---

## Step 5: Test Your Form

### 5.1 Submit a Test

1. Go to **https://medspaflywheel.com/contact.html**
2. Fill out the form with test data
3. Click **"Schedule Strategy Call"**

### 5.2 First Submission Confirmation

**Important:** The first time someone submits your form, Formspree will ask them to confirm they're human. This is a one-time setup step.

1. After submitting, the person will see a Formspree confirmation page
2. They need to click **"Confirm your email"**
3. Check the email inbox of the person who submitted
4. Click the confirmation link in the email
5. Done! The form is now fully activated

### 5.3 Check Your Email

After confirmation:
- You should receive an email notification with the form data
- Check your spam folder if you don't see it
- Add formspree.io to your safe senders list

---

## Step 6: Configure Formspree Settings

### 6.1 Access Form Settings

1. Go to **https://formspree.io/forms**
2. Click on your **"MedSpa Flywheel Contact Form"**
3. Click **"Settings"** tab

### 6.2 Recommended Settings

**Email Notifications:**
- ✅ Enable email notifications
- ✅ Set notification email (where leads go)
- ✅ Customize email subject: "New Lead from MedSpa Flywheel"

**After Submit:**
- ✅ Enable "Redirect to custom URL"
- ✅ Enter: `https://medspaflywheel.com/thank-you.html`
- ✅ This redirects users to your thank-you page after submission

**Spam Protection:**
- ✅ Enable reCAPTCHA
- ✅ Enable honeypot field
- ✅ Protect against spam

**Field Validation:**
- ✅ Make sure these fields are marked as required:
  - name
  - email
  - phone
  - medspa-name
  - revenue
  - challenge

---

## Step 7: Monitor Submissions

### 7.1 Formspree Dashboard

View all submissions at: **https://formspree.io/forms**

You can:
- View all form submissions
- Export submissions to CSV
- See submission statistics
- Manage spam

### 7.2 Email Notifications

You'll receive an email for each submission with:
- All form fields and values
- Timestamp
- IP address
- User agent

---

## Troubleshooting

### ❌ Form Not Submitting

**Problem:** Form doesn't submit or shows error

**Solutions:**
1. Check that Form ID is correct in contact.html
2. Make sure the form action URL includes `https://`
3. Clear browser cache and try again
4. Check browser console for JavaScript errors

---

### ❌ Not Receiving Emails

**Problem:** Form submits but no email received

**Solutions:**
1. **Check spam folder** - Formspree emails often go to spam initially
2. **Verify notification email** - Check Formspree settings
3. **Confirm form** - Make sure first submission was confirmed
4. **Check Formspree dashboard** - Submissions should appear even if email fails

**Add to safe senders:**
- Add `noreply@formspree.io` to your contacts
- Add to email whitelist

---

### ❌ Users See Formspree Page Instead of Thank-You

**Problem:** After submitting, users see Formspree page instead of your thank-you page

**Solutions:**
1. Go to Formspree form settings
2. Enable "Redirect to custom URL"
3. Enter: `https://medspaflywheel.com/thank-you.html`
4. Save settings
5. Test again

---

### ❌ Spam Submissions

**Problem:** Receiving spam through the form

**Solutions:**
1. Enable reCAPTCHA in Formspree settings
2. Enable honeypot field
3. Use Formspree's spam filtering
4. Consider upgrading to paid plan for better spam protection

---

## Upgrade Options

### Free Plan
- 50 submissions/month
- Email notifications
- Spam filtering
- File uploads (10MB)

### Gold Plan ($10/month)
- 1,000 submissions/month
- Advanced spam protection
- Custom email templates
- Priority support
- Remove Formspree branding

### Platinum Plan ($40/month)
- 10,000 submissions/month
- Everything in Gold
- Webhook integrations
- API access
- Team collaboration

---

## Alternative: Netlify Forms (If on Netlify)

If you're hosting on Netlify instead of Vercel, you can use Netlify Forms:

1. Add `netlify` attribute to form:
   ```html
   <form name="contact" netlify netlify-honeypot="bot-field">
   ```

2. Add hidden field:
   ```html
   <input type="hidden" name="form-name" value="contact">
   ```

3. Deploy to Netlify
4. Check Netlify dashboard for submissions

**Note:** You're currently on Vercel, so Formspree is recommended.

---

## Form Fields Reference

Your form collects these fields:

| Field Name | Type | Required | Purpose |
|------------|------|----------|---------|
| `name` | Text | Yes | Contact's full name |
| `email` | Email | Yes | Contact's email address |
| `phone` | Tel | Yes | Contact's phone number |
| `medspa-name` | Text | Yes | Med spa business name |
| `revenue` | Select | Yes | Current monthly revenue range |
| `challenge` | Textarea | Yes | Main marketing challenge |
| `referral` | Select | No | How they heard about you |

All data is sent to Formspree and emailed to you.

---

## Quick Setup Checklist

- [ ] 1. Create Formspree account (https://formspree.io/)
- [ ] 2. Create new form in Formspree
- [ ] 3. Copy your Form ID
- [ ] 4. Run setup script: `python3 scripts/setup-formspree.py "YOUR_FORM_ID"`
- [ ] 5. Commit and push changes
- [ ] 6. Wait for Vercel deployment (2-3 minutes)
- [ ] 7. Submit test form
- [ ] 8. Confirm first submission (check email)
- [ ] 9. Configure Formspree settings (redirect, notifications)
- [ ] 10. Add formspree.io to safe senders
- [ ] 11. Test again to verify everything works
- [ ] 12. Monitor dashboard for submissions

---

## Current Status

- ✅ Contact form HTML structure ready
- ✅ Form validation in place
- ✅ Thank-you page exists
- ✅ Setup script created (scripts/setup-formspree.py)
- ⏳ **Waiting for you:** Create Formspree account and get Form ID
- ⏳ **Then run:** `python3 scripts/setup-formspree.py "YOUR_FORM_ID"`

---

## Support

**Formspree Support:**
- Documentation: https://help.formspree.io/
- Email: team@formspree.io
- Response time: Usually within 24 hours

**Your Setup:**
- Form location: `/contact.html`
- Thank-you page: `/thank-you.html`
- Setup script: `/scripts/setup-formspree.py`

---

## Security & Privacy

**Data Handling:**
- Form data is encrypted in transit (HTTPS)
- Stored securely on Formspree servers
- You can export and delete data anytime
- GDPR compliant

**Best Practices:**
- Never collect sensitive health information through web forms
- Add privacy policy link to form
- Include consent checkbox if required by law
- Consider adding terms of service link

---

That's it! Once you complete the setup, your contact form will be fully functional and you'll start receiving lead notifications via email. 🎉
