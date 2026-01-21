# 📝 Weekly Blog Post Workflow

**Time Required:** 4-6 hours total (spread across the week)

---

## 🗓️ **Monday: Planning (30 minutes)**

### Step 1: Check Content Calendar
1. Open: `/tmp/content_calendar_2025.csv`
2. Find this week's topic
3. Note: Topic, Primary Keyword, Target Audience

### Step 2: Generate Blog Template
Run the generator script:

```bash
cd /home/user/medspaflywheel
./.claude/blog-generator.sh "Your Blog Title Here" "primary-keyword-slug"
```

**Example:**
```bash
./.claude/blog-generator.sh "How to Market a Med Spa" "how-to-market-med-spa"
```

This creates: `blog/how-to-market-med-spa.html`

### Step 3: Create Outline
Open a text editor and write:
- 5-7 main section headings
- 3-5 bullet points per section
- Where to add examples/case studies
- Internal links to plan

**Save as:** `blog-outlines/[topic]-outline.txt`

---

## 📊 **Tuesday-Wednesday: Research & Write (3-4 hours)**

### Step 4: Research
1. **Google the keyword** - See what's ranking
2. **Read top 3 articles** - Note what they cover
3. **Find 2-3 statistics** - Add credibility
4. **Check your services** - Link opportunities

### Step 5: Write First Draft
Open: `blog/[your-slug].html`

**Writing checklist:**
- [ ] Include primary keyword in first 100 words
- [ ] Write 2,000-2,500 words (check: `wc -w blog/[slug].html`)
- [ ] Add 5-7 H2 sections
- [ ] Add 2-3 H3 subsections per H2
- [ ] Include 2-3 internal links
- [ ] Add 1-2 external links (authority sites)
- [ ] Write compelling intro (hook + promise)
- [ ] Write clear conclusion + CTA

⚠️ **CRITICAL - Content Guidelines:**
- [ ] NO fabricated case studies or client examples
- [ ] ALL statistics cited with sources (WordStream, HubSpot, DMA, etc.)
- [ ] Use "Example Scenario:" for hypotheticals (NOT "Real Example:" unless verified)
- [ ] No specific client results without written permission
- [ ] Review: `.claude/BLOG_CONTENT_GUIDELINES.md` before writing

**Time-saving tips:**
- Use bullet lists (easier to read)
- Include industry benchmark data with sources
- Use clearly labeled hypothetical scenarios
- Break up text with subheadings every 200-300 words

---

## 🎨 **Thursday: Images (1 hour)**

### Step 6: Find Featured Image

**Option A: Unsplash (Free, High-Quality)**
1. Go to: https://unsplash.com
2. Search: "medical spa", "aesthetic clinic", "skincare"
3. Download high-res (1200x630px minimum)
4. Save as: `images/blog/[your-slug].jpg`

**Option B: Canva (Custom)**
1. Go to: https://canva.com
2. Create design → Facebook Post (1200x630px)
3. Add:
   - Blog title text
   - Relevant image background
   - MedSpa Flywheel branding
4. Download as JPG
5. Save as: `images/blog/[your-slug].jpg`

**Option C: Stock Photos**
- Pexels.com
- Pixabay.com
- StockSnap.io

### Step 7: Optimize Image
Run this command to reduce file size:

```bash
# If you have ImageMagick installed:
convert images/blog/[slug].jpg -quality 85 -resize 1200x630 images/blog/[slug].jpg
```

**Or use online tool:**
- TinyPNG.com
- Squoosh.app

**Target:** Under 200KB file size

---

## ✅ **Friday: Review & Publish (1 hour)**

### Step 8: SEO Review
Open your blog post and check:

**Meta Tags:**
- [ ] Title tag includes keyword (50-60 chars)
- [ ] Meta description includes keyword (<160 chars)
- [ ] OG image path correct
- [ ] Canonical URL correct

**Content:**
- [ ] H1 includes primary keyword
- [ ] Primary keyword in first paragraph
- [ ] Keyword appears 5-10 times naturally
- [ ] 2-3 internal links (to services/locations)
- [ ] 1-2 external links (to authority sites)
- [ ] All images have alt tags

**Technical:**
- [ ] All EDIT_ placeholders replaced
- [ ] Navigation added (copy from index.html)
- [ ] Footer added (copy from index.html)
- [ ] Links work (test in browser)
- [ ] Mobile-friendly (test on phone)

### Step 9: Final Review
Read the entire post aloud. Check:
- Grammar/spelling
- Flow and readability
- Calls-to-action clear
- Examples relevant
- Stats/data accurate

### Step 10: Publish
```bash
cd /home/user/medspaflywheel
git add blog/[your-slug].html images/blog/[your-slug].jpg
git commit -m "Add blog post: [Title]"
git push origin claude/hide-case-studies-footer-links-01XeGNJcWhDKtbisNJhebCCf
```

Then merge PR on GitHub.

### Step 11: Submit to Google
1. Go to: https://search.google.com/search-console
2. Click: URL Inspection
3. Enter: `https://medspaflywheel.com/blog/[your-slug].html`
4. Click: "Request Indexing"

### Step 12: Share on Social
- Post on LinkedIn with snippet
- Share in relevant Facebook groups
- Tweet with key takeaway
- Add to newsletter if applicable

---

## 📈 **Weekly Tracking (5 minutes)**

### Update Your Content Log
Create a spreadsheet:

| Date | Topic | Keyword | Word Count | Published URL | Indexed? | Ranking (Week 4) |
|------|-------|---------|------------|---------------|----------|------------------|
| 1/6  | How to Market | how to market med spa | 2,450 | /blog/how-to... | Yes | Position 15 |

---

## 🚨 **Troubleshooting**

**Problem:** Blog generator script doesn't work
**Fix:** Run: `chmod +x ./.claude/blog-generator.sh`

**Problem:** Can't find good images
**Fix:** Use Canva text-only design with gradient background

**Problem:** Don't know what to write
**Fix:** Follow the outline from content calendar, expand each bullet point into paragraph

**Problem:** Post is too short (under 2,000 words)
**Fix:** Add more examples, expand each section with "How to do this" steps

**Problem:** Not sure about keyword placement
**Fix:** Use keyword in: Title, H1, First paragraph, 1-2 H2s, Last paragraph, Meta description

---

## ⏰ **Time Breakdown**

| Day | Task | Time |
|-----|------|------|
| Monday | Planning + Outline | 30 min |
| Tuesday | Research + Write (Part 1) | 2 hours |
| Wednesday | Write (Part 2) + Edit | 2 hours |
| Thursday | Images | 1 hour |
| Friday | Review + Publish | 1 hour |
| **Total** | | **6.5 hours** |

---

## 📋 **Quick Checklist (Print This)**

**Before Publishing:**
- [ ] 2,000+ words
- [ ] Keyword in title, H1, first 100 words
- [ ] 5-7 H2 sections
- [ ] 2-3 internal links
- [ ] 1-2 external links
- [ ] Featured image (1200x630px, <200KB)
- [ ] All alt tags added
- [ ] Meta description written
- [ ] Navigation/footer added
- [ ] Tested on mobile
- [ ] Spell-checked
- [ ] CTA included
- [ ] Schema markup complete

**After Publishing:**
- [ ] Submit to Google Search Console
- [ ] Share on LinkedIn
- [ ] Add to blog index page
- [ ] Update sitemap
- [ ] Track in spreadsheet

---

## 🎯 **Success Metrics**

Track these monthly:
- Posts published: 4-5/month
- Total traffic to blog: Check Google Analytics
- Ranking keywords: Check Search Console
- Leads from blog: Track form submissions
- Time on page: 3+ minutes = good

**Goal:** 20-30% of site traffic from blog within 6 months
