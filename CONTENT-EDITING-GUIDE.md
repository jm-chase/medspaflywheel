# Content Editing Guide
## MedSpa Flywheel Website - Centralized Content Management System

**Last Updated:** 2024-01-15
**Version:** 1.0

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [What Placeholder Content Was Found](#what-placeholder-content-was-found)
3. [How the System Works](#how-the-system-works)
4. [How to Edit Content](#how-to-edit-content)
5. [Content File Structure](#content-file-structure)
6. [Files Modified](#files-modified)
7. [Deployment Process](#deployment-process)
8. [Troubleshooting](#troubleshooting)

---

## Overview

This guide explains the new **centralized content management system** for the MedSpa Flywheel website. Instead of editing content directly in 58+ HTML files, you now edit **ONE JSON file** (`content/site-content.json`), and a build script automatically updates all HTML files.

### ✅ Benefits

- **Single source of truth** for all site content
- **Easy updates** - edit one file instead of 58
- **Consistency** - same content appears correctly everywhere
- **Version control** - track content changes in Git
- **Safe editing** - structured format prevents breaking HTML

### 🎯 Goal

**Replace all placeholder content with real company data before launch!**

---

## What Placeholder Content Was Found

During the audit, we identified **placeholder/filler content** across the entire website:

### 1. **Contact Information** (Found in 58 files)

| Type | Placeholder | Where to Update |
|------|-------------|-----------------|
| Email | `hello@medspaflywheel.com` | `company.contact.email` |
| Phone | `(888) 555-1234` | `company.contact.phone` |
| Social Media | facebook.com/medspaflywheel | `company.social.*` |

**Files affected:** All HTML files (index.html, services.html, about.html, contact.html, 45 location pages, blog pages, etc.)

---

### 2. **Fake Business Names** (Case Studies)

| Business Name | Location | Status |
|---------------|----------|--------|
| Glow MedSpa | Miami, FL | 🚨 Placeholder |
| Radiance Aesthetics | Charleston, SC | 🚨 Placeholder |
| Elite Rejuvenation | Atlanta, GA | 🚨 Placeholder |
| Bella Vita MedSpa | Tampa, FL | 🚨 Placeholder |
| Pure Aesthetics | Savannah, GA | 🚨 Placeholder |
| Luxury Skin Clinic | Nashville, TN | 🚨 Placeholder |

**Where to update:** `caseStudies` array in site-content.json

**Files affected:** case-studies.html, case-study-template.html, index.html

---

### 3. **Fake People Names** (Team & Testimonials)

| Name | Role | Status |
|------|------|--------|
| Sarah Mitchell | Founder & CEO | 🚨 Placeholder |
| Marcus Rodriguez | Head of Paid Media | 🚨 Placeholder |
| Aisha Patel | Director of Automation | 🚨 Placeholder |
| Dr. Sarah Chen | Client Testimonial | 🚨 Placeholder |

**Where to update:** `team` array in site-content.json

**Files affected:** about.html, case-study-template.html

---

### 4. **Placeholder Statistics**

| Stat | Value | Where Used | Status |
|------|-------|------------|--------|
| Med Spas Served | 50+ | Homepage | 🚨 Placeholder |
| Average ROI | 250% | Homepage | 🚨 Placeholder |
| Appointments Generated | 10K+ | Homepage | 🚨 Placeholder |
| Client Rating | 4.8★ | Homepage | 🚨 Placeholder |
| Booking Increase | 180% | All case studies | 🚨 Placeholder |
| Cost Per Lead | $31 | Case study | 🚨 Placeholder |
| ROAS | 4.2x | Case study | 🚨 Placeholder |

**Where to update:** `homepage.stats` and `caseStudies[].results` in site-content.json

**Files affected:** index.html, case-studies.html, case-study-template.html, 45 location pages

---

### 5. **Missing Images** (50+ References)

| Image Type | Example | Status |
|------------|---------|--------|
| Open Graph Images | og-image.jpg | ❌ Missing |
| Twitter Card Images | twitter-image.jpg | ❌ Missing |
| Company Logo | logo.png | ❌ Missing |
| Team Photos | sarah-mitchell.jpg | ❌ Missing |
| Client Logos | glow-medspa-logo.png | ❌ Missing |
| Case Study Photos | case-studies/*.jpg | ❌ Missing |
| Certification Badges | google-ads.png | ❌ Missing |

**Where to update:** `images` and `team[].photo` and `caseStudies[].featuredImage` in site-content.json

**Files affected:** All HTML files

---

### 6. **Location Pages** (45 Cities)

All 45 location pages use the same template content with only the city name changed:

**States covered:**
- Florida (10 cities)
- Georgia (7 cities)
- North Carolina (8 cities)
- South Carolina (5 cities)
- Tennessee (5 cities)
- Alabama (4 cities)
- Virginia (5 cities)

**Generic content includes:**
- Same market descriptions
- Same 3 case study examples per city
- Same statistics (180% increase, 87 reviews, etc.)

**Where to update:** `locationDefaults` in site-content.json (for default stats) or individual location pages for unique content

**Files affected:** All 45 city pages (miami-fl.html, atlanta-ga.html, etc.)

---

### 7. **TODO/REPLACE Comments** (180+ occurrences)

Found comments like:
```html
<!-- REPLACE WITH ACTUAL [City] CASE STUDY -->
<!-- Replace YOUR_VERIFICATION_CODE -->
<!-- Badge Placeholders -->
```

**Action needed:** Review these comments in HTML files and replace with actual content

---

## How the System Works

### Architecture

```
┌─────────────────────────────────┐
│   content/site-content.json     │  ← Edit this file
│   (Single source of truth)      │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  scripts/update-content.py      │  ← Build script
│  (Reads JSON, updates HTML)     │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   58 HTML files updated         │  ← Automatically updated
│   (index.html, services.html...)│
└─────────────────────────────────┘
```

### Build Process

1. **You edit** `content/site-content.json`
2. **Run** `npm run build` (or Vercel runs it automatically)
3. **Python script** reads JSON and updates all HTML files
4. **Website** is deployed with updated content

### Automation

- **Local development:** Run `npm run build` to update HTML files
- **Vercel deployment:** Runs automatically before every deploy
- **No manual HTML editing needed!**

---

## How to Edit Content

### Step-by-Step Process

#### **Step 1: Open the Content File**

Open `content/site-content.json` in your text editor.

```bash
# Using VS Code
code content/site-content.json

# Using nano
nano content/site-content.json

# Using vim
vim content/site-content.json
```

#### **Step 2: Find the Section to Edit**

The JSON file is organized into sections:

```json
{
  "company": { ... },          // Contact info, social media
  "homepage": { ... },         // Homepage content
  "team": [ ... ],             // Team members
  "caseStudies": [ ... ],      // Case studies
  "locationDefaults": { ... }, // Location page defaults
  "images": { ... },           // Image paths
  "certifications": [ ... ],   // Badges/certifications
  "seo": { ... }              // SEO defaults
}
```

#### **Step 3: Edit the Content**

Replace placeholder values with real content.

**Example: Updating Contact Information**

**Before:**
```json
"contact": {
  "email": "hello@medspaflywheel.com",
  "phone": "(888) 555-1234"
}
```

**After:**
```json
"contact": {
  "email": "info@yourrealcompany.com",
  "phone": "(305) 123-4567"
}
```

#### **Step 4: Save the File**

Save your changes to `site-content.json`.

#### **Step 5: Run the Build Script**

```bash
npm run build
```

**Output:**
```
🚀 Starting content update process...
📁 Site root: /home/user/medspaflywheel
📄 Content file: content/site-content.json

📝 Found 58 HTML files to process

✅ Updated: index.html
✅ Updated: services.html
✅ Updated: about.html
...

📊 CONTENT UPDATE SUMMARY
✅ Files processed: 58
🔄 Replacements made: 342
✨ No errors encountered!
```

#### **Step 6: Test Locally**

Open the HTML files in a browser to verify changes:

```bash
# Start a local server
npm run dev

# Open in browser: http://localhost:8000
```

#### **Step 7: Commit and Deploy**

```bash
git add content/site-content.json
git commit -m "Update contact information and case studies"
git push
```

Vercel will automatically run the build script and deploy!

---

## Content File Structure

### Detailed Breakdown

#### **1. Company Information**

```json
"company": {
  "name": "MedSpa Flywheel",
  "tagline": "Medical Spa Marketing That Delivers Results",
  "description": "...",
  "contact": {
    "email": "hello@medspaflywheel.com",    // ← Update this
    "phone": "(888) 555-1234",               // ← Update this
    "phoneFormatted": "+1-888-555-1234",     // ← Update this
    "address": {
      "street": "",                          // ← Add real address
      "city": "",
      "state": "",
      "zip": ""
    }
  },
  "social": {
    "facebook": "https://www.facebook.com/...",   // ← Update these
    "instagram": "https://www.instagram.com/...",
    "linkedin": "https://www.linkedin.com/...",
    "twitter": "https://www.twitter.com/..."
  },
  "logo": {
    "path": "images/logo.png",                    // ← Add actual logo
    "alt": "MedSpa Flywheel Logo"
  }
}
```

**Used in:** All pages (header, footer, contact forms, schema markup)

---

#### **2. Homepage Content**

```json
"homepage": {
  "hero": {
    "headline": "Grow Your Med Spa with Proven Marketing",
    "subheadline": "We help medical spas fill their...",
    "cta": {
      "primary": "Get Your Free Strategy Call",
      "secondary": "See Case Studies"
    }
  },
  "stats": {
    "medSpasServed": {
      "number": "50+",                    // ← Update with real number
      "label": "Med Spas Served"
    },
    "averageROI": {
      "number": "250%",                   // ← Update with real stat
      "label": "Average ROI Increase"
    },
    "appointmentsGenerated": {
      "number": "10K+",                   // ← Update with real stat
      "label": "New Client Appointments Generated"
    },
    "clientRating": {
      "number": "4.8★",                   // ← Update with real rating
      "label": "Average Client Rating"
    }
  }
}
```

**Used in:** index.html only

---

#### **3. Team Members**

```json
"team": [
  {
    "id": "sarah-mitchell",              // Unique ID
    "name": "Sarah Mitchell",            // ← Update with real name
    "title": "Founder & CEO",            // ← Update with real title
    "bio": "With over 12 years...",      // ← Update with real bio
    "photo": "images/team/sarah-mitchell.jpg",  // ← Add real photo
    "linkedIn": "",                      // ← Add LinkedIn URL
    "email": ""                          // ← Add email
  },
  {
    "id": "marcus-rodriguez",
    "name": "Marcus Rodriguez",
    // ... same structure
  }
]
```

**How to add a new team member:**

1. Copy an existing team member object
2. Change the `id` to something unique (e.g., "john-smith")
3. Update all fields with real information
4. Add the team member's photo to `images/team/`
5. Run `npm run build`

**Used in:** about.html

---

#### **4. Case Studies**

```json
"caseStudies": [
  {
    "id": "glow-medspa",                    // Unique ID
    "clientName": "Glow MedSpa",            // ← Update with real client
    "location": "Miami, FL",
    "industry": "Medical Spa",
    "featured": true,                       // Show on homepage?
    "featuredImage": "images/case-studies/glow-medspa.jpg",
    "logo": "images/clients/glow-medspa-logo.png",
    "slug": "glow-medspa-miami",           // Used in URL
    "testimonial": {
      "quote": "Working with MedSpa Flywheel...",  // ← Real quote
      "author": "Dr. Sarah Chen",                  // ← Real name
      "authorTitle": "Founder & Medical Director",
      "authorPhoto": "images/testimonials/dr-sarah-chen.jpg"
    },
    "challenge": "Glow MedSpa was struggling...",  // ← Real challenge
    "solution": "We implemented a precision...",    // ← Real solution
    "results": {
      "headline": "180% Increase in Monthly Bookings",  // ← Real result
      "metrics": [
        {
          "label": "Increase in Bookings",
          "value": "+180%",                    // ← Real metric
          "description": "From 14 to 72 appointments per month"
        },
        {
          "label": "Return on Ad Spend",
          "value": "4.2x",                     // ← Real ROAS
          "description": "For every $1 spent, generated $4.20"
        }
      ],
      "timeline": "90 days",
      "additionalRevenue": "$287K",            // ← Real revenue
      "tags": ["Google Ads", "Email Automation", "Local SEO"]
    }
  }
]
```

**How to add a new case study:**

1. Copy an existing case study object
2. Change the `id` to match the client (e.g., "abc-medspa")
3. Update all fields with real client data
4. Add client logo to `images/clients/`
5. Add featured image to `images/case-studies/`
6. Add testimonial photo to `images/testimonials/`
7. Run `npm run build`

**Used in:** case-studies.html, index.html (if featured), case-study-template.html

---

#### **5. Location Defaults**

```json
"locationDefaults": {
  "stats": {
    "bookingIncrease": "180%",               // ← Default for all cities
    "bookingIncreaseLabel": "Increase in Monthly Bookings",
    "reviews": "87",                         // ← Default review count
    "reviewsLabel": "New 5-Star Reviews in 90 Days",
    "medSpasInCity": "15+"                   // ← Avg med spas per city
  },
  "caseStudyCount": 3                        // Number of case studies shown
}
```

**Note:** These are defaults used across all 45 location pages. To customize individual cities, you'll need to edit the specific HTML file directly (or extend the JSON structure).

**Used in:** All 45 location pages

---

#### **6. Images**

```json
"images": {
  "og": {
    "default": "images/og-image.jpg",        // ← Add actual OG image
    "blog": "images/og-blog.jpg",
    "locations": "images/og-locations.jpg"
  },
  "twitter": {
    "default": "images/twitter-image.jpg"    // ← Add actual Twitter card
  },
  "placeholders": {
    "clientLogo": "images/placeholders/client-logo.svg",
    "teamPhoto": "images/placeholders/team-photo.svg",
    "caseStudy": "images/placeholders/case-study.jpg"
  }
}
```

**Image Requirements:**

| Image Type | Dimensions | Format |
|------------|------------|--------|
| Open Graph | 1200x630px | JPG/PNG |
| Twitter Card | 1200x675px | JPG/PNG |
| Team Photos | 400x400px | JPG/PNG |
| Client Logos | 300x100px | PNG (transparent) |
| Case Study Featured | 1200x630px | JPG |
| Company Logo | 300x100px | PNG (transparent) |

**Used in:** All pages (meta tags, team section, case studies, etc.)

---

#### **7. Certifications/Badges**

```json
"certifications": [
  {
    "name": "Google Ads Certified",
    "icon": "images/badges/google-ads.png",   // ← Add actual badge
    "url": ""                                 // ← Add credential URL
  },
  {
    "name": "Facebook Blueprint",
    "icon": "images/badges/facebook-blueprint.png",
    "url": ""
  }
]
```

**How to add a certification:**

1. Add the badge image to `images/badges/`
2. Add a new object to the `certifications` array
3. Run `npm run build`

**Used in:** about.html

---

#### **8. SEO Defaults**

```json
"seo": {
  "defaultTitle": "MedSpa Flywheel - Medical Spa Marketing...",
  "defaultDescription": "Specialized marketing agency...",
  "siteName": "MedSpa Flywheel",
  "siteUrl": "https://medspaflywheel.com",      // ← Update domain
  "twitterHandle": "@medspaflywheel"            // ← Update handle
}
```

**Used in:** Schema markup, meta tags

---

## Files Modified

### Created Files

| File | Purpose |
|------|---------|
| `content/site-content.json` | Single source of truth for all content |
| `scripts/update-content.py` | Python script that updates HTML files |
| `package.json` | NPM scripts for building |
| `vercel.json` | Vercel deployment configuration |
| `CONTENT-EDITING-GUIDE.md` | This documentation file |

### HTML Files That Will Be Updated

**All 58 HTML files** in the root directory will be automatically updated when you run `npm run build`:

#### Core Pages (7 files)
- index.html
- services.html
- about.html
- process.html
- contact.html
- case-studies.html
- case-study-template.html

#### Blog (2 files)
- blog.html
- blog-post-template.html

#### Utility Pages (2 files)
- thank-you.html
- 404.html

#### Location Pages (45 files)
- miami-fl.html
- atlanta-ga.html
- tampa-fl.html
- charlotte-nc.html
- *(and 41 more location pages)*

#### Other (2 files)
- locations.html
- location-template.html

### What Gets Replaced Automatically

The Python script automatically replaces:

✅ **Contact information** (email, phone) everywhere
✅ **Social media URLs** in all footers
✅ **Homepage statistics** (50+, 250%, 10K+, 4.8★)
✅ **Location page stats** (180%, 87 reviews)
✅ **Image paths** (og-image.jpg, logo.png, etc.)
✅ **Consistent formatting** across all files

❌ **Does NOT replace** (requires manual HTML editing):
- Team member sections (complex HTML structure)
- Full case study pages (complex layout)
- Blog post content
- Navigation menus
- Footer structure

**For complex HTML sections**, edit the HTML directly or extend the Python script.

---

## Deployment Process

### Local Development

1. Edit `content/site-content.json`
2. Run `npm run build`
3. Test with `npm run dev` (opens http://localhost:8000)
4. Review changes in browser
5. Commit and push when satisfied

### Vercel Deployment (Automatic)

When you push to GitHub, Vercel automatically:

1. ✅ Detects the push
2. ✅ Runs `npm install` (no dependencies needed)
3. ✅ Runs `npm run build` (executes update-content.py)
4. ✅ Deploys the updated HTML files
5. ✅ Your site is live!

**No manual intervention required!**

### Manual Deployment

If deploying to a traditional host:

1. Edit `content/site-content.json`
2. Run `npm run build` locally
3. Upload ALL files (including updated HTML) via FTP/SFTP
4. Your site is live!

---

## Troubleshooting

### Problem: "python3: command not found"

**Solution:**

```bash
# Install Python 3
# On Ubuntu/Debian:
sudo apt-get install python3

# On macOS:
brew install python3

# On Windows (use Git Bash or WSL):
# Download from https://www.python.org/downloads/
```

---

### Problem: "npm: command not found"

**Solution:**

```bash
# Install Node.js and npm
# On Ubuntu/Debian:
sudo apt-get install nodejs npm

# On macOS:
brew install node

# On Windows:
# Download from https://nodejs.org/
```

---

### Problem: Changes not showing up on website

**Checklist:**

1. ✅ Did you save `site-content.json`?
2. ✅ Did you run `npm run build`?
3. ✅ Did the script complete without errors?
4. ✅ Did you hard-refresh the browser (Ctrl+F5)?
5. ✅ Did you commit and push the changes?
6. ✅ Did Vercel finish deploying?

---

### Problem: JSON syntax error

**Common JSON mistakes:**

❌ **Trailing comma:**
```json
{
  "name": "John",
  "email": "john@example.com",  ← Remove this comma
}
```

✅ **Correct:**
```json
{
  "name": "John",
  "email": "john@example.com"
}
```

❌ **Missing quotes:**
```json
{
  name: "John"  ← Keys must be in quotes
}
```

✅ **Correct:**
```json
{
  "name": "John"
}
```

**Use a JSON validator:**
- https://jsonlint.com/
- VS Code (built-in validation)

---

### Problem: Script fails with "KeyError"

**Cause:** Missing field in JSON

**Solution:** Make sure all required fields exist in `site-content.json`. Compare with the original template.

---

### Problem: Want to revert changes

```bash
# Revert site-content.json to previous version
git checkout HEAD~1 content/site-content.json

# Rebuild HTML files
npm run build

# Commit the reversion
git add .
git commit -m "Revert content changes"
git push
```

---

## Best Practices

### ✅ Do's

- **Always run `npm run build`** after editing `site-content.json`
- **Test locally** before pushing to production
- **Commit frequently** with descriptive messages
- **Keep backup copies** of `site-content.json`
- **Use a JSON validator** before committing
- **Document your changes** in commit messages

### ❌ Don'ts

- **Don't edit HTML files directly** for content that's in the JSON
- **Don't break JSON syntax** (always validate)
- **Don't forget to run the build script**
- **Don't push untested changes** to production
- **Don't delete fields** from JSON (set to empty string instead)

---

## Quick Reference

### Common Commands

```bash
# Update content and rebuild HTML files
npm run build

# Start local development server
npm run dev

# Update content only (no server)
npm run update-content

# Test deployment locally
python3 -m http.server 8000
```

### File Locations

```
medspaflywheel/
├── content/
│   └── site-content.json          ← Edit this file
├── scripts/
│   └── update-content.py          ← Build script (don't edit unless needed)
├── images/                        ← Add your images here
│   ├── team/
│   ├── clients/
│   ├── case-studies/
│   ├── badges/
│   └── testimonials/
├── package.json                   ← NPM scripts configuration
├── vercel.json                    ← Vercel deployment settings
└── *.html                         ← Automatically updated by script
```

### Editing Workflow

```
1. Edit content/site-content.json
2. Run npm run build
3. Test locally (npm run dev)
4. Review changes in browser
5. Commit and push
6. Vercel auto-deploys
7. Verify live site
```

---

## Support & Resources

### Documentation

- **This guide:** `CONTENT-EDITING-GUIDE.md`
- **Content guide:** `CONTENT-GUIDE.md` (for HTML editing)
- **Deployment guide:** `DEPLOYMENT.md`
- **Performance guide:** `PERFORMANCE-OPTIMIZATION.md`

### Tools

- **JSON Validator:** https://jsonlint.com/
- **VS Code:** Best editor for JSON (built-in validation)
- **GitHub Desktop:** Easy Git management

### Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review the script output for error messages
3. Validate your JSON syntax
4. Check the GitHub repository for updates

---

## Next Steps

### Immediate Action Items

1. **Review the current placeholder content** in `site-content.json`
2. **Start replacing placeholder data** with real company information
3. **Focus on high-priority items first:**
   - Contact information (email, phone)
   - Company name and description
   - Homepage statistics
   - Team member information
4. **Add real images** to the `images/` directory
5. **Test thoroughly** before going live

### Long-Term Maintenance

- **Monthly:** Review and update case studies
- **Quarterly:** Update statistics and metrics
- **As needed:** Add new team members, certifications, testimonials
- **Before major launches:** Update all placeholder content

---

## Appendix: Complete Content Checklist

Use this checklist to track what content has been updated:

### Company Information
- [ ] Company name
- [ ] Tagline
- [ ] Description
- [ ] Email address
- [ ] Phone number
- [ ] Physical address
- [ ] Social media URLs (Facebook, Instagram, LinkedIn, Twitter)
- [ ] Company logo

### Homepage
- [ ] Hero headline
- [ ] Hero subheadline
- [ ] CTA button text
- [ ] Med Spas Served stat
- [ ] Average ROI stat
- [ ] Appointments Generated stat
- [ ] Client Rating stat

### Team Members
- [ ] Replace all 3 placeholder team members with real people
- [ ] Add real photos for each team member
- [ ] Update bios with accurate information
- [ ] Add LinkedIn profiles
- [ ] Add email addresses

### Case Studies
- [ ] Replace all 6 fake case studies with real clients
- [ ] Update client names
- [ ] Update locations
- [ ] Replace testimonial quotes with real quotes
- [ ] Update all statistics and metrics
- [ ] Add real client logos
- [ ] Add real featured images
- [ ] Add real testimonial photos

### Images
- [ ] Open Graph image (1200x630px)
- [ ] Twitter card image (1200x675px)
- [ ] Company logo (300x100px)
- [ ] All team photos (400x400px each)
- [ ] All client logos
- [ ] All case study featured images
- [ ] All testimonial photos

### Certifications
- [ ] Add all relevant certification badge images
- [ ] Add credential URLs

### SEO
- [ ] Update site URL (if different domain)
- [ ] Update Twitter handle
- [ ] Update default meta descriptions

### Location Pages (45 cities)
- [ ] Review default statistics (180%, 87 reviews, etc.)
- [ ] Consider customizing per-city if needed

---

**🎉 Congratulations!** You now have a centralized content management system.

**Remember:** Edit `content/site-content.json`, run `npm run build`, and all 58 HTML files are automatically updated!

---

**Last Updated:** 2024-01-15
**Document Version:** 1.0
**Maintained by:** MedSpa Flywheel Development Team
