# MedSpa Flywheel - Deployment Guide

Complete guide for deploying the MedSpa Flywheel website to production.

---

## Table of Contents

1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Netlify Deployment (Recommended)](#netlify-deployment-recommended)
3. [Alternative Hosting Options](#alternative-hosting-options)
4. [Domain Configuration](#domain-configuration)
5. [SSL Certificate](#ssl-certificate)
6. [Analytics & Tracking](#analytics--tracking)
7. [Form Configuration](#form-configuration)
8. [Post-Launch Tasks](#post-launch-tasks)
9. [Troubleshooting](#troubleshooting)

---

## Pre-Deployment Checklist

Before deploying, ensure:

- [ ] All content is finalized
- [ ] All placeholder text replaced with real content
- [ ] All images optimized (WebP format, compressed)
- [ ] Contact form email address configured
- [ ] Google Analytics tracking ID added
- [ ] All internal links tested
- [ ] Mobile responsiveness verified
- [ ] Lighthouse audit passed (90+ scores)
- [ ] Browser testing completed (Chrome, Firefox, Safari, Edge)
- [ ] Domain name purchased (medspaflywheel.com)

---

## Netlify Deployment (Recommended)

Netlify offers the easiest deployment with automatic SSL, CDN, and form handling.

### Step 1: Sign Up for Netlify

1. Go to [netlify.com](https://www.netlify.com)
2. Click "Sign up" (can use GitHub account)
3. Verify your email

### Step 2: Connect Repository

**Option A: GitHub (Recommended)**

1. Push this repository to GitHub:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/medspaflywheel.git
   git branch -M main
   git push -u origin main
   ```

2. In Netlify dashboard:
   - Click "Add new site" → "Import an existing project"
   - Choose "GitHub"
   - Authorize Netlify
   - Select `medspaflywheel` repository
   - Click "Deploy site"

**Option B: Drag & Drop (Quick Test)**

1. In Netlify dashboard, click "Add new site" → "Deploy manually"
2. Drag the entire project folder into the upload area
3. Wait for deployment (usually 30 seconds)

### Step 3: Configure Site Settings

1. **Site name**: Click "Site settings" → "Change site name"
   - Enter: `medspaflywheel` (or your preferred subdomain)
   - Your site will be at: `https://medspaflywheel.netlify.app`

2. **Build settings**: Already configured in `netlify.toml`
   - No build command needed (static HTML)
   - Publish directory: `.` (root)

3. **Environment variables** (if needed):
   - Go to "Site settings" → "Environment variables"
   - Add any API keys or secrets

### Step 4: Connect Custom Domain

1. In Netlify, go to "Domain settings"
2. Click "Add custom domain"
3. Enter: `medspaflywheel.com`
4. Click "Verify" then "Add domain"

5. Configure DNS at your domain registrar (e.g., GoDaddy, Namecheap):

   **For Netlify DNS (Recommended):**
   - In Netlify, click "Set up Netlify DNS"
   - Copy the 4 nameservers provided
   - At your registrar, change nameservers to Netlify's

   **OR Use External DNS:**
   - Add an A record pointing to Netlify's load balancer IP
   - Add CNAME for www pointing to your Netlify subdomain

   DNS propagation takes 24-48 hours (usually faster).

### Step 5: Enable SSL (Automatic)

1. Once domain is connected, go to "Domain settings" → "HTTPS"
2. Click "Verify DNS configuration"
3. SSL certificate provisions automatically (takes 1-2 minutes)
4. Enable "Force HTTPS" to redirect all HTTP to HTTPS

### Step 6: Configure Forms

Forms are automatically detected by Netlify. Verify:

1. Go to "Forms" in Netlify dashboard
2. You should see "Contact Form" listed
3. Configure email notifications:
   - Click form → "Form notifications"
   - Add "Email notification"
   - Enter your email: `hello@medspaflywheel.com`

### Step 7: Set Up Redirects

Already configured in `netlify.toml` and `_redirects`:
- www → non-www redirect
- 404 page handling
- URL cleanup

Test redirects:
- `https://www.medspaflywheel.com` → should redirect to `https://medspaflywheel.com`
- `https://medspaflywheel.com/nonexistent` → should show 404 page

---

## Alternative Hosting Options

### Option 1: Vercel

1. Sign up at [vercel.com](https://vercel.com)
2. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```
3. Deploy:
   ```bash
   cd /path/to/medspaflywheel
   vercel
   ```
4. Follow prompts to connect domain
5. Configure `vercel.json`:
   ```json
   {
     "cleanUrls": true,
     "trailingSlash": false,
     "redirects": [
       { "source": "/home", "destination": "/", "permanent": true },
       { "source": "/index", "destination": "/", "permanent": true }
     ],
     "headers": [
       {
         "source": "/(.*)",
         "headers": [
           { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
           { "key": "X-Content-Type-Options", "value": "nosniff" }
         ]
       }
     ]
   }
   ```

### Option 2: GitHub Pages

1. Push code to GitHub repository
2. Go to repository → Settings → Pages
3. Source: Deploy from branch `main`
4. Folder: `/ (root)`
5. Custom domain: `medspaflywheel.com`
6. Enable "Enforce HTTPS"

**Note:** GitHub Pages limitations:
- No server-side form handling (use FormSpree)
- No custom headers
- No serverless functions

### Option 3: Traditional Hosting (cPanel, Bluehost, etc.)

1. **Upload files via FTP:**
   - Host: `ftp.medspaflywheel.com`
   - Username: (provided by host)
   - Password: (provided by host)
   - Upload all files to `/public_html/` or `/www/`

2. **Configure .htaccess:**
   ```apache
   # Enable HTTPS redirect
   RewriteEngine On
   RewriteCond %{HTTPS} off
   RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
   
   # www to non-www redirect
   RewriteCond %{HTTP_HOST} ^www\.medspaflywheel\.com [NC]
   RewriteRule ^(.*)$ https://medspaflywheel.com/$1 [L,R=301]
   
   # Custom 404 page
   ErrorDocument 404 /404.html
   
   # Browser caching
   <IfModule mod_expires.c>
     ExpiresActive On
     ExpiresByType image/jpeg "access plus 1 year"
     ExpiresByType image/png "access plus 1 year"
     ExpiresByType image/webp "access plus 1 year"
     ExpiresByType text/css "access plus 1 month"
     ExpiresByType application/javascript "access plus 1 month"
   </IfModule>
   
   # Gzip compression
   <IfModule mod_deflate.c>
     AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript
   </IfModule>
   ```

3. **Install SSL certificate:**
   - Most hosts offer free Let's Encrypt SSL
   - Enable in cPanel → SSL/TLS → Install SSL Certificate

4. **Form handling:**
   - Use FormSpree (see Form Configuration section)
   - OR set up server-side PHP script

---

## Domain Configuration

### Register Domain

**Recommended Registrars:**
- Namecheap: ~$8-12/year
- Google Domains: ~$12/year
- Cloudflare: ~$8/year (best value)

### DNS Configuration

**For Netlify:**
1. Use Netlify DNS (easiest)
2. Point nameservers to Netlify's servers
3. All DNS managed in Netlify dashboard

**For Custom DNS:**
```
Type    Name    Value                           TTL
A       @       Netlify IP (75.2.60.5)         3600
CNAME   www     medspaflywheel.netlify.app     3600
```

### Email Setup

Since `medspaflywheel.com` is your domain:

1. **Google Workspace** (professional email):
   - $6/user/month
   - Email: `hello@medspaflywheel.com`
   - Setup: Add MX records to DNS

2. **Zoho Mail** (free alternative):
   - Free for 5 users
   - Email: `hello@medspaflywheel.com`
   - Setup: Add MX and TXT records

3. **Email forwarding** (simple):
   - Forward `hello@medspaflywheel.com` to Gmail
   - Configure in domain registrar's DNS settings

---

## SSL Certificate

### Netlify (Automatic)
- Free Let's Encrypt SSL
- Auto-renewal
- No configuration needed
- Just enable HTTPS in domain settings

### Traditional Hosting
1. cPanel → SSL/TLS → Manage SSL
2. Enable "AutoSSL" (Let's Encrypt)
3. Certificate provisions in 5 minutes
4. Auto-renews every 90 days

### Cloudflare (Additional Layer)
1. Sign up at [cloudflare.com](https://www.cloudflare.com)
2. Add your domain
3. Change nameservers to Cloudflare's
4. Enable SSL/TLS → Full (strict)
5. Benefits: DDoS protection, faster CDN, better caching

---

## Analytics & Tracking

### Google Analytics 4 (Recommended)

1. **Create GA4 Property:**
   - Go to [analytics.google.com](https://analytics.google.com)
   - Click "Admin" → "Create Property"
   - Property name: "MedSpa Flywheel"
   - Click "Create"
   - Choose "Web" platform
   - Add website URL: `https://medspaflywheel.com`

2. **Get Measurement ID:**
   - Copy your Measurement ID (format: `G-XXXXXXXXXX`)

3. **Add to website:**
   Add this code to the `<head>` of every HTML file (after opening `<head>` tag):

   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```

   Replace `G-XXXXXXXXXX` with your actual Measurement ID.

4. **Verify installation:**
   - Open your site
   - Open Chrome DevTools → Console
   - Type: `gtag` (should show function, not undefined)
   - OR use Google Tag Assistant Chrome extension

### Google Search Console

1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Click "Add property"
3. Enter: `https://medspaflywheel.com`
4. Verify ownership (3 methods):

   **Method 1: DNS verification** (Recommended)
   - Copy TXT record
   - Add to DNS settings
   - Click "Verify"

   **Method 2: HTML tag**
   - Copy meta tag
   - Add to `<head>` of index.html
   - Upload and click "Verify"

   **Method 3: HTML file**
   - Download verification file
   - Upload to root directory
   - Click "Verify"

5. **Submit sitemap:**
   - Go to "Sitemaps" in left menu
   - Enter: `https://medspaflywheel.com/sitemap.xml`
   - Click "Submit"

### Facebook Pixel (Optional)

1. Go to [facebook.com/business](https://facebook.com/business)
2. Events Manager → Add Pixel
3. Get Pixel ID
4. Add code to `<head>` of all pages:

   ```html
   <!-- Facebook Pixel Code -->
   <script>
   !function(f,b,e,v,n,t,s)
   {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
   n.callMethod.apply(n,arguments):n.queue.push(arguments)};
   if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
   n.queue=[];t=b.createElement(e);t.async=!0;
   t.src=v;s=b.getElementsByTagName(e)[0];
   s.parentNode.insertBefore(t,s)}(window, document,'script',
   'https://connect.facebook.net/en_US/fbevents.js');
   fbq('init', 'YOUR_PIXEL_ID');
   fbq('track', 'PageView');
   </script>
   <noscript><img height="1" width="1" style="display:none"
   src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"
   /></noscript>
   <!-- End Facebook Pixel Code -->
   ```

### Google Tag Manager (Advanced - Optional)

Use GTM to manage all tracking codes from one place:

1. Create account at [tagmanager.google.com](https://tagmanager.google.com)
2. Create container for your website
3. Add GTM code to all pages
4. Add tags via GTM interface (GA, Facebook Pixel, etc.)

---

## Form Configuration

### Netlify Forms (If using Netlify)

Already configured! Just verify:

1. Contact form has `netlify` attribute:
   ```html
   <form name="contact" method="POST" data-netlify="true">
   ```

2. Add honeypot for spam protection:
   ```html
   <input type="hidden" name="form-name" value="contact">
   <div style="display:none">
     <input name="bot-field">
   </div>
   ```

3. Configure success redirect in form:
   ```html
   <form name="contact" method="POST" data-netlify="true" action="/thank-you.html">
   ```

4. Email notifications:
   - Netlify dashboard → Forms → Notifications
   - Add email notification to `hello@medspaflywheel.com`

### FormSpree (For Non-Netlify Hosting)

1. Sign up at [formspree.io](https://formspree.io)
2. Create new form
3. Get form endpoint: `https://formspree.io/f/YOUR_FORM_ID`
4. Update contact form:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
     <!-- form fields -->
   </form>
   ```

5. Configure in FormSpree dashboard:
   - Add notification email
   - Set custom success URL
   - Enable spam filtering

### Custom PHP Form (Advanced)

If your host supports PHP, create `process-form.php`:

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    
    $to = "hello@medspaflywheel.com";
    $subject = "Contact Form Submission from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email";
    
    if (mail($to, $subject, $body, $headers)) {
        header("Location: thank-you.html");
    } else {
        echo "Error sending message";
    }
}
?>
```

Update form action: `<form action="process-form.php" method="POST">`

---

## Post-Launch Tasks

### Week 1: Setup & Verification

- [ ] Verify site loads at custom domain
- [ ] Test SSL certificate (green padlock)
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools
- [ ] Verify Google Analytics tracking
- [ ] Test contact form submission
- [ ] Check email notifications working
- [ ] Test on mobile devices
- [ ] Run Lighthouse audit (target: 90+)
- [ ] Check all internal links

### Week 2: SEO Foundation

- [ ] Create Google My Business listing
- [ ] Claim business on major directories:
  - Yelp
  - Yellow Pages
  - Better Business Bureau
  - Local chamber of commerce
- [ ] Set up social media profiles (with same branding):
  - Facebook Business Page
  - Instagram Business
  - LinkedIn Company Page
- [ ] Link website to all social profiles

### Month 1: Content & Monitoring

- [ ] Publish first 3 blog posts
- [ ] Set up Google Alerts for brand name
- [ ] Install uptime monitoring (UptimeRobot)
- [ ] Review Google Analytics weekly
- [ ] Check Search Console for errors
- [ ] Monitor page load speed
- [ ] Start backlink building
- [ ] Reach out for initial testimonials

### Ongoing: Growth & Optimization

- [ ] Publish 2-4 blog posts per month
- [ ] Monitor keyword rankings
- [ ] A/B test CTAs and headlines
- [ ] Update location pages quarterly
- [ ] Add new case studies
- [ ] Build local citations
- [ ] Collect and respond to reviews
- [ ] Run monthly Lighthouse audits

---

## Troubleshooting

### Site Not Loading

**Problem:** Domain shows "Site not found" or old site

**Solutions:**
1. Check DNS propagation: Use [whatsmydns.net](https://www.whatsmydns.net)
2. Wait 24-48 hours for DNS propagation
3. Clear browser cache (Ctrl+Shift+Delete)
4. Try incognito/private window
5. Verify DNS records are correct

### SSL Certificate Not Working

**Problem:** Browser shows "Not Secure" warning

**Solutions:**
1. Check Netlify DNS is fully propagated
2. In Netlify: Domain Settings → HTTPS → Verify DNS
3. If using custom DNS, verify CAA records allow Let's Encrypt
4. Wait 24 hours after DNS setup
5. Contact Netlify support if persists

### Forms Not Submitting

**Problem:** Form submits but nothing happens

**Solutions:**
1. Verify `data-netlify="true"` attribute exists
2. Check form has `name` attribute
3. Redeploy site (Netlify must detect forms on deploy)
4. Check Netlify dashboard → Forms for errors
5. Verify email notification is configured

### Images Not Loading

**Problem:** Broken image icons

**Solutions:**
1. Check file paths are correct (case-sensitive)
2. Verify images uploaded to correct directory
3. Use absolute paths: `/images/photo.jpg`
4. Check file extensions match (jpg vs jpeg)
5. Verify images aren't too large (max 5MB recommended)

### Slow Page Speed

**Problem:** Lighthouse score below 90

**Solutions:**
1. Optimize images (WebP format, compress)
2. Implement PurgeCSS for CSS
3. Self-host fonts
4. Enable compression (Gzip/Brotli)
5. Remove unused JavaScript
6. Implement lazy loading for images
7. Use CDN (Netlify includes this)

### Google Analytics Not Tracking

**Problem:** No data in Google Analytics

**Solutions:**
1. Verify Measurement ID is correct
2. Check code is in `<head>` section
3. Test with Google Tag Assistant extension
4. Wait 24-48 hours for initial data
5. Check tracking isn't blocked by ad blocker
6. Verify domain matches in GA settings

### 404 Errors for Pages That Exist

**Problem:** Valid pages showing 404

**Solutions:**
1. Check file names match exactly (case-sensitive)
2. Verify .html extension in URL
3. Check _redirects file isn't conflicting
4. Ensure files uploaded to correct directory
5. Try hard refresh (Ctrl+F5)

---

## Performance Monitoring

### Recommended Tools

**Uptime Monitoring:**
- UptimeRobot (free, checks every 5 min)
- Pingdom (paid, more features)
- StatusCake (free tier available)

**Performance Monitoring:**
- Google PageSpeed Insights (free)
- GTmetrix (free)
- WebPageTest (free, detailed)
- Lighthouse CI (automate audits)

**SEO Monitoring:**
- Google Search Console (free, essential)
- Ahrefs (paid, comprehensive)
- SEMrush (paid, full suite)
- Moz (paid, beginner-friendly)

### Set Up Alerts

1. **Uptime alerts:**
   - UptimeRobot → Add Monitor
   - URL: https://medspaflywheel.com
   - Email alert if down > 2 minutes

2. **Search Console alerts:**
   - Automatic emails for critical issues
   - Coverage errors
   - Security issues
   - Manual actions

3. **Analytics alerts:**
   - GA4 → Admin → Custom Alerts
   - Alert if traffic drops 50%+
   - Alert if conversions = 0

---

## Security Best Practices

### Ongoing Security

1. **Keep everything updated:**
   - Monitor hosting provider updates
   - Update dependencies if using any

2. **Backup regularly:**
   - Netlify auto-backups every deploy
   - Keep local copy of code
   - Export Analytics data monthly

3. **Monitor for issues:**
   - Check Search Console weekly
   - Review form submissions for spam
   - Monitor Analytics for unusual activity

4. **Use strong passwords:**
   - Hosting account
   - Domain registrar
   - Analytics accounts
   - Email accounts

5. **Enable 2FA everywhere:**
   - Netlify account
   - Domain registrar
   - Google accounts
   - Social media

---

## Support & Resources

### Documentation

- Netlify Docs: https://docs.netlify.com
- Google Analytics: https://support.google.com/analytics
- Search Console: https://support.google.com/webmasters
- This repo: PERFORMANCE-OPTIMIZATION.md, PERFORMANCE-REPORT.md

### Getting Help

1. **Netlify Support:**
   - Community forum: https://answers.netlify.com
   - Paid support: support@netlify.com

2. **General Web Issues:**
   - Stack Overflow
   - MDN Web Docs
   - Web.dev

3. **SEO Questions:**
   - Google Search Central Community
   - /r/SEO on Reddit
   - Moz Community

---

## Quick Reference

### Key URLs

| Resource | URL |
|----------|-----|
| Production Site | https://medspaflywheel.com |
| Netlify Dashboard | https://app.netlify.com |
| Google Analytics | https://analytics.google.com |
| Search Console | https://search.google.com/search-console |
| GitHub Repo | https://github.com/YOUR_USERNAME/medspaflywheel |

### Important Credentials

Store these securely (LastPass, 1Password, etc.):

- Domain registrar login
- Hosting account login
- Email account credentials
- Google Analytics account
- Search Console account
- Social media accounts
- FTP credentials (if applicable)

### Emergency Contacts

- Hosting support: support@netlify.com
- Domain registrar support: (varies)
- Developer: (your contact info)

---

## Next Steps

1. ✅ Complete pre-deployment checklist
2. ✅ Deploy to Netlify (or chosen host)
3. ✅ Configure custom domain
4. ✅ Enable SSL
5. ✅ Set up forms
6. ✅ Add analytics
7. ✅ Submit sitemaps
8. ✅ Create social profiles
9. ✅ Monitor performance
10. ✅ Start content marketing

**Your site is ready to launch! 🚀**

---

*Last Updated: January 2024*
*Questions? Refer to PERFORMANCE-OPTIMIZATION.md and PERFORMANCE-REPORT.md*
