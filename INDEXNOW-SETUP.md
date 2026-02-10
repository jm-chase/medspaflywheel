# IndexNow Setup for MedSpa Flywheel

IndexNow is a protocol that allows websites to instantly notify search engines about content changes, ensuring faster indexing.

## What's Been Set Up

### 1. API Key File
- **File**: `b78d8c7a35784a0b8077235e720af300.txt`
- **Location**: Root directory
- **Content**: Your IndexNow API key
- **URL**: `https://medspaflywheel.com/b78d8c7a35784a0b8077235e720af300.txt`

This file **must be deployed** to your live site for IndexNow to work.

### 2. Submission Script
- **File**: `scripts/submit-to-indexnow.sh`
- **Purpose**: Submits URLs to IndexNow API
- **Supported Search Engines**: Bing, Yandex, and other IndexNow partners

## How to Use

### Submit All URLs from Sitemap
```bash
bash scripts/submit-to-indexnow.sh
```

This will submit all 58 URLs from your sitemap to IndexNow.

### Submit Specific URLs
```bash
bash scripts/submit-to-indexnow.sh "https://medspaflywheel.com/" "https://medspaflywheel.com/services.html"
```

### When to Submit URLs
Submit URLs to IndexNow when you:
- Publish new content
- Update existing pages
- Add new location pages
- Publish new blog posts
- Make significant content changes

## Important Notes

### 1. Deploy the Key File First
Before running the submission script, make sure:
- ✅ The key file `b78d8c7a35784a0b8077235e720af300.txt` is deployed to production
- ✅ It's accessible at `https://medspaflywheel.com/b78d8c7a35784a0b8077235e720af300.txt`
- ✅ The file contains only your API key with no extra whitespace

### 2. Rate Limiting
- IndexNow may rate-limit submissions if you submit too frequently
- The script includes a small delay between individual submissions
- Batch submissions are recommended for multiple URLs

### 3. Response Codes
- **200 OK**: URL submitted successfully
- **400 Bad Request**: Invalid format
- **403 Forbidden**: Key not valid (key file not accessible)
- **422 Unprocessable Entity**: URLs don't belong to your domain
- **429 Too Many Requests**: Rate limited (wait before retrying)

## Testing the Setup

After deploying, test the setup:

```bash
# Test key file accessibility
curl https://medspaflywheel.com/b78d8c7a35784a0b8077235e720af300.txt

# Should return: b78d8c7a35784a0b8077235e720af300
```

Then submit a test URL:
```bash
bash scripts/submit-to-indexnow.sh "https://medspaflywheel.com/"
```

You should see: `✓ Success: https://medspaflywheel.com/`

## Automation

You can automate IndexNow submissions using:

### Option 1: Manual After Content Updates
Run the script manually whenever you update content:
```bash
bash scripts/submit-to-indexnow.sh "https://medspaflywheel.com/blog/new-post.html"
```

### Option 2: Scheduled Submissions
Add to your CI/CD pipeline or create a cron job to submit sitemap URLs periodically:
```bash
# Add to crontab to run weekly
0 0 * * 0 cd /path/to/medspaflywheel && bash scripts/submit-to-indexnow.sh
```

### Option 3: Deploy Hook
Integrate with your deployment process (Vercel, Netlify, etc.) to automatically submit URLs after each deployment.

## Search Engine Coverage

IndexNow is supported by:
- ✅ **Microsoft Bing** - Full support
- ✅ **Yandex** - Full support
- ✅ **Seznam.cz** - Full support
- ℹ️ **Google** - Not currently supported (use Google Search Console instead)

## Additional Resources

- [IndexNow Documentation](https://www.indexnow.org/)
- [IndexNow API Reference](https://www.indexnow.org/documentation)
- [Bing Webmaster Tools](https://www.bing.com/webmasters)
