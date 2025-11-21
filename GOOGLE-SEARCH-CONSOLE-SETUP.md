# Google Search Console Setup & Sitemap Submission Guide

Complete step-by-step guide to verify your website with Google Search Console and submit your sitemap.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step 1: Set Up Google Search Console](#step-1-set-up-google-search-console)
3. [Step 2: Verify Your Website](#step-2-verify-your-website)
4. [Step 3: Submit Your Sitemap](#step-3-submit-your-sitemap)
5. [Step 4: Monitor Your Site](#step-4-monitor-your-site)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

✅ **Already Complete:**
- ✅ Website is live at https://medspaflywheel.com
- ✅ Sitemap.xml exists with all 55 pages (updated 2025-11-21)
- ✅ Robots.txt is properly configured
- ✅ Google Analytics is installed (G-RL2PXG1Y0X)

**You Need:**
- Google account (can be any Gmail account)
- Access to deploy changes to the website

---

## Step 1: Set Up Google Search Console

### 1.1 Go to Google Search Console

**URL:** https://search.google.com/search-console/

### 1.2 Add Your Property

1. Click **"Add Property"** or **"Start Now"**

2. **Choose Property Type:**
   - Select **"URL prefix"** (recommended)
   - Enter: `https://medspaflywheel.com`
   - Click **"Continue"**

   **Note:** Use URL prefix (not Domain) because it's easier to verify with HTML meta tag.

---

## Step 2: Verify Your Website

Google offers multiple verification methods. We'll use the **HTML tag method** (easiest).

### 2.1 Choose HTML Tag Verification Method

1. In the verification screen, click **"HTML tag"**

2. You'll see a meta tag that looks like this:
   ```html
   <meta name="google-site-verification" content="ABC123xyz456..." />
   ```

3. **Copy the entire verification code** (the part that looks like `ABC123xyz456...`)
   - It will be a long string of letters and numbers
   - Do NOT copy the entire `<meta>` tag, just the content value

### 2.2 Add Verification Code to Your Website

**Option A: Using the Python Script (Easiest)**

1. Open PowerShell on Windows:
   ```powershell
   cd C:\Users\james\medspaflywheel
   ```

2. Run the verification script:
   ```bash
   # In WSL
   cd /home/user/medspaflywheel
   python3 scripts/add-google-verification.py "YOUR_VERIFICATION_CODE_HERE"
   ```

   Replace `YOUR_VERIFICATION_CODE_HERE` with the code you copied from Google.

   Example:
   ```bash
   python3 scripts/add-google-verification.py "ABC123xyz456def789ghi012jkl345mno678pqr901stu234vwx567yz890"
   ```

3. The script will:
   - Add the verification meta tag to ALL 55 HTML files
   - Show you a summary of updated files

**Option B: Manual Edit (If Script Fails)**

1. Open any text editor (VS Code, Notepad++, etc.)

2. Open `index.html`

3. Find this line (around line 29):
   ```html
   <!-- <meta name="google-site-verification" content="YOUR_VERIFICATION_CODE"> -->
   ```

4. Replace it with your actual verification tag:
   ```html
   <meta name="google-site-verification" content="ABC123xyz456def789ghi012jkl345mno678pqr901stu234vwx567yz890">
   ```

5. Save the file

6. **Repeat for ALL 55 HTML files** (or use the script!)

### 2.3 Deploy Your Changes

1. **Commit changes:**
   ```bash
   git add -A
   git commit -m "Add Google Search Console verification"
   git push
   ```

2. **Wait for Vercel to deploy** (~2-3 minutes)
   - Check https://vercel.com for deployment status
   - Or wait for the email notification

3. **Verify the meta tag is live:**
   - Go to https://medspaflywheel.com
   - Right-click → View Page Source
   - Press Ctrl+F and search for "google-site-verification"
   - You should see your verification meta tag

### 2.4 Complete Verification in Google Search Console

1. Go back to Google Search Console

2. Click **"Verify"** button

3. If successful, you'll see:
   ✅ **"Ownership verified"**

4. Click **"Go to property"**

**If verification fails:**
- Wait 5-10 minutes (DNS/CDN cache may need time)
- Make sure the meta tag is visible in the page source
- Try verification again
- See [Troubleshooting](#troubleshooting) section below

---

## Step 3: Submit Your Sitemap

### 3.1 Access Sitemap Section

1. In Google Search Console dashboard, look at the left sidebar

2. Click **"Sitemaps"** (under "Indexing" section)

### 3.2 Submit Your Sitemap

1. In the **"Add a new sitemap"** field, enter:
   ```
   sitemap.xml
   ```

2. Click **"Submit"**

3. You should see:
   - Status: **Success** (may take a few minutes)
   - **55 pages discovered**

### 3.3 What Happens Next

- **Immediately:** Google adds your sitemap to the queue
- **Within hours:** Google starts crawling your pages
- **Within days:** Pages start appearing in search results
- **Within weeks:** Full indexing complete (check "Coverage" report)

---

## Step 4: Monitor Your Site

### 4.1 Key Reports to Check

**Coverage Report:**
- Shows which pages are indexed
- Go to: Indexing → Coverage
- Check for errors or warnings

**Performance Report:**
- Shows search impressions, clicks, CTR
- Go to: Performance
- See which pages are getting traffic

**URL Inspection:**
- Test individual pages
- Enter any URL from your site
- See if it's indexed and request re-indexing if needed

### 4.2 Request Indexing for Important Pages

For high-priority pages (like your homepage), request immediate indexing:

1. Click **"URL Inspection"** (top of page)

2. Enter URL: `https://medspaflywheel.com/`

3. Click **"Request Indexing"**

4. Repeat for important pages:
   - https://medspaflywheel.com/services.html
   - https://medspaflywheel.com/contact.html
   - Your top city pages (Miami, Atlanta, Nashville, etc.)

### 4.3 Set Up Email Notifications

1. Click the ⚙️ **Settings** icon (top right)

2. Click **"Users and permissions"**

3. Make sure your email is set to receive notifications for:
   - New issues detected
   - Security issues
   - Manual actions

---

## Troubleshooting

### ❌ Verification Failed

**"Meta tag not found"**

**Solutions:**
1. Clear your browser cache and check the live site
2. View page source and search for "google-site-verification"
3. Make sure the tag is in the `<head>` section, not `<body>`
4. Wait 10-15 minutes for CDN cache to clear
5. Make sure there are no typos in the verification code

**"Verification has already been attempted"**

**Solutions:**
1. Wait 24 hours before trying again
2. Or try a different verification method (HTML file upload)

---

### ❌ Sitemap Not Found

**"Sitemap could not be read"**

**Solutions:**
1. Verify sitemap is accessible: https://medspaflywheel.com/sitemap.xml
2. Check for XML syntax errors
3. Make sure sitemap.xml is in the root directory
4. Check robots.txt references the correct URL

**Verify sitemap manually:**
```bash
# Check sitemap exists
curl https://medspaflywheel.com/sitemap.xml

# Check robots.txt
curl https://medspaflywheel.com/robots.txt
```

---

### ❌ Pages Not Being Indexed

**"Discovered - currently not indexed"**

**This is normal!** Google discovered your pages but hasn't indexed them yet.

**Solutions:**
1. **Wait:** Can take 2-4 weeks for new sites
2. **Request indexing:** Use URL Inspection tool
3. **Improve content:** Make sure pages have unique, valuable content
4. **Build backlinks:** Get other sites to link to you
5. **Social signals:** Share pages on social media

**"Crawled - currently not indexed"**

Google crawled but chose not to index. Usually means:
- Content is thin or duplicate
- Page quality is low
- Too many similar pages

**Solutions:**
1. Improve content quality and uniqueness
2. Add more text, images, value to pages
3. Make sure each city page has unique content

---

### ❌ Sitemap Warnings

**"Sitemap is HTML"**

Your sitemap.xml is being served as HTML instead of XML.

**Solution:** Make sure sitemap.xml has proper XML header:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
```

---

## Your Current Sitemap Structure

✅ **sitemap.xml includes:**
- 8 core pages (index, services, about, etc.)
- 2 blog pages
- 1 locations index
- 44 city landing pages (FL, GA, NC, SC, TN, AL, VA)
- **Total: 55 URLs**

✅ **robots.txt:**
- Allows all crawlers
- Points to sitemap: `https://medspaflywheel.com/sitemap.xml`

✅ **All pages updated:** 2025-11-21

---

## Quick Reference Commands

**Update sitemap dates:**
```bash
# Already done! All dates set to 2025-11-21
```

**Add Google verification:**
```bash
cd /home/user/medspaflywheel
python3 scripts/add-google-verification.py "YOUR_CODE"
```

**Commit and deploy:**
```bash
git add -A
git commit -m "Add Google Search Console verification"
git push
```

**Test sitemap:**
```bash
curl https://medspaflywheel.com/sitemap.xml
curl https://medspaflywheel.com/robots.txt
```

---

## Expected Timeline

| Timeframe | What to Expect |
|-----------|----------------|
| **Immediately** | Verification complete, sitemap submitted |
| **Within 24 hours** | Google starts crawling pages |
| **2-7 days** | First pages indexed, appear in search results |
| **2-4 weeks** | Majority of pages indexed |
| **1-3 months** | Full SEO benefits, ranking improvements |

---

## Next Steps After Setup

1. ✅ **Verify website** with Google Search Console
2. ✅ **Submit sitemap**
3. ⏳ **Wait 24-48 hours** for first crawl
4. 📊 **Check Coverage report** to see indexing progress
5. 🔍 **Request indexing** for priority pages
6. 📈 **Monitor Performance report** for search traffic
7. 🔧 **Fix any errors** reported in Coverage
8. 🔄 **Update sitemap** when you add new pages

---

## Resources

- **Google Search Console:** https://search.google.com/search-console/
- **Google Search Central:** https://developers.google.com/search
- **Sitemap Protocol:** https://www.sitemaps.org/
- **robots.txt Tester:** https://support.google.com/webmasters/answer/6062598

---

## Current Status

- ✅ Sitemap.xml exists with 55 pages
- ✅ All dates updated to 2025-11-21
- ✅ Robots.txt properly configured
- ✅ Google Analytics installed
- ⏳ Google Search Console verification - **Ready to start!**
- ⏳ Sitemap submission - **Ready after verification!**

**You're ready to begin!** Follow Step 1 above to get started.
