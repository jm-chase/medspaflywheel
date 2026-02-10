# 🚀 MedSpa Flywheel - Automated Blog System

**Complete, repeatable workflow for weekly SEO blog posts**

---

## 📁 **System Overview**

This system automates your blog content creation process from planning to publishing.

**What's Included:**
- ✅ 52-week content calendar (full year planned)
- ✅ Blog post generator (creates HTML templates)
- ✅ Weekly workflow guide (step-by-step)
- ✅ Outline generator (ChatGPT prompts)
- ✅ Image sourcing guide
- ✅ SEO checklist

**Time Investment:**
- Setup: 30 minutes (one-time)
- Weekly: 4-6 hours per post
- ROI: 20-30% of site traffic from blog within 6 months

---

## 🗂️ **Files in This System**

| File | Purpose | When to Use |
|------|---------|-------------|
| `AUTOMATED_BLOG_SYSTEM_README.md` | Overview (this file) | Read first |
| `content-calendar-2025.csv` | 52 blog topics planned | Check every Monday |
| `blog-generator.sh` | Creates HTML templates | Start of each post |
| `WEEKLY_BLOG_WORKFLOW.md` | Step-by-step process | Follow every week |
| `blog-outline-generator.md` | ChatGPT prompts for outlines | When planning post |

---

## 🚀 **Quick Start (First Time)**

### Step 1: Review Content Calendar
```bash
cat .claude/content-calendar-2025.csv
```

**You'll see 52 weeks of:**
- Blog topics
- Primary keywords
- Search volume
- Target audience
- Content type

### Step 2: Test Blog Generator
```bash
cd /home/user/medspaflywheel
./.claude/blog-generator.sh "Test Blog Post" "test-blog-post"
```

This creates: `blog/test-blog-post.html`

### Step 3: Review Workflow
```bash
cat .claude/WEEKLY_BLOG_WORKFLOW.md
```

Print this and keep at your desk!

---

## 📅 **Weekly Workflow (Summary)**

### **Monday (30 min)**
1. Check content calendar for this week's topic
2. Run blog generator: `./.claude/blog-generator.sh "Title" "slug"`
3. Create outline using ChatGPT prompt

### **Tuesday-Wednesday (3-4 hours)**
1. Research: Read top 3 ranking articles
2. Write: 2,000-2,500 words
3. Include: 2-3 internal links, examples, stats

### **Thursday (1 hour)**
1. Find featured image (Unsplash/Canva)
2. Optimize to <200KB
3. Save as: `images/blog/[slug].jpg`

### **Friday (1 hour)**
1. Review SEO checklist
2. Replace all EDIT_ placeholders
3. Publish via Git
4. Submit to Google Search Console
5. Share on social media

---

## 🤖 **Using the Blog Generator**

### Basic Usage
```bash
./.claude/blog-generator.sh "Full Blog Title" "url-slug"
```

### Examples
```bash
# Week 1 post:
./.claude/blog-generator.sh "How to Market a Med Spa: Complete 2026 Guide" "how-to-market-med-spa"

# Week 2 post:
./.claude/blog-generator.sh "50+ Med Spa Marketing Ideas That Actually Work" "med-spa-marketing-ideas"

# Week 3 post:
./.claude/blog-generator.sh "Best CRM for Med Spas: 2025 Comparison" "best-crm-for-med-spas"
```

### What It Creates
- Full HTML file in `/blog/` directory
- Pre-configured with:
  - SEO meta tags
  - Open Graph tags
  - Schema markup
  - Navigation/footer placeholders
  - Content sections ready to fill
  - CTA section

### What You Need to Edit
- All `EDIT_` placeholders
- Write actual content (2,000+ words)
- Add navigation (copy from index.html)
- Add footer (copy from index.html)

---

## ✍️ **Creating Outlines with AI**

### Option 1: ChatGPT
1. Open ChatGPT
2. Use prompt from `blog-outline-generator.md`
3. Fill in: Topic, Keyword, Audience
4. Get detailed outline in seconds

### Option 2: Claude (This Assistant)
Ask me: "Create outline for: [topic from calendar]"

### Option 3: Manual
Use templates in `blog-outline-generator.md`:
- How-To Guide template
- Listicle template
- Comparison template

---

## 🎨 **Image Sourcing**

### Free High-Quality Sources
1. **Unsplash.com**
   - Search: "medical spa", "aesthetic clinic", "skincare"
   - Filter: Landscape orientation
   - Download: High-res

2. **Pexels.com**
   - Similar to Unsplash
   - More variety

3. **Canva.com**
   - Create custom graphics
   - Use template: Facebook Post (1200x630px)
   - Add text + branding

### Image Requirements
- **Dimensions:** 1200x630px minimum
- **File size:** Under 200KB
- **Format:** JPG (not PNG)
- **Naming:** Same as blog slug
- **Location:** `images/blog/[slug].jpg`

### Optimization
```bash
# Reduce file size (if ImageMagick installed):
convert images/blog/[slug].jpg -quality 85 -resize 1200x630 images/blog/[slug].jpg
```

Or use: TinyPNG.com, Squoosh.app

---

## ✅ **SEO Checklist (Before Publishing)**

Copy this checklist for each post:

**Meta Tags:**
- [ ] Title includes primary keyword (50-60 chars)
- [ ] Meta description includes keyword (<160 chars)
- [ ] Canonical URL is correct
- [ ] OG image path is correct
- [ ] Schema markup datePublished updated

**Content:**
- [ ] H1 includes primary keyword
- [ ] Keyword in first 100 words
- [ ] 2,000-2,500 word count
- [ ] 5-7 H2 sections
- [ ] 2-3 internal links (to services/locations)
- [ ] 1-2 external links (authority sites)
- [ ] Examples and case studies included
- [ ] CTA is clear and relevant

**Technical:**
- [ ] All EDIT_ placeholders replaced
- [ ] Navigation added from index.html
- [ ] Footer added from index.html
- [ ] All images have alt tags
- [ ] Mobile-friendly (test)
- [ ] All links work

**Quality:**
- [ ] Spell-checked
- [ ] Grammar-checked (Grammarly)
- [ ] Read aloud test passed
- [ ] Better than top 3 ranking articles

---

## 📊 **Tracking Results**

### Create Tracking Spreadsheet

**Columns:**
- Week number
- Publish date
- Topic
- Primary keyword
- Word count
- URL
- Date indexed
- Current ranking (check weekly)
- Traffic (monthly)

### Check Rankings
**Every Monday:**
1. Google Search Console → Performance
2. Filter by your blog URLs
3. Export last 7 days data
4. Update spreadsheet

**Manual Check:**
1. Open incognito browser
2. Search your primary keyword
3. Find your position (1-100)
4. Record in spreadsheet

---

## 🎯 **Content Calendar Guide**

### How Topics Were Selected
- ✅ **Search Volume:** 30-700 searches/month
- ✅ **Difficulty:** Low (easier to rank)
- ✅ **Intent:** Matches our services
- ✅ **Variety:** How-to, listicles, comparisons
- ✅ **Seasonal:** Holiday/promotion content timed right

### Post Types Explained

**Pillar Content (Weeks 1, 11, 23):**
- Long-form (3,000+ words)
- Comprehensive guides
- Hub for related content
- Link to from other posts

**Listicles (Weeks 2, 20, 33):**
- Easy to write
- Highly shareable
- Good for social media
- 50+ ideas format works well

**Comparisons (Weeks 3, 12, 32):**
- Commercial intent
- Closer to purchase decision
- Position your service
- Include pricing

**How-To Guides (Weeks 4, 6, 11):**
- Step-by-step instructions
- Actionable advice
- Include screenshots
- Link to services

**Seasonal (Weeks 25, 35, 43, 48):**
- Time-sensitive
- Higher urgency
- Update yearly
- Repurpose annually

---

## 🔄 **Monthly Review**

### End of Each Month Check:

**Content Performance:**
- Posts published: 4-5 ✅
- Average word count: 2,000+ ✅
- Internal links: 2-3 per post ✅
- On-time publishing: 100% ✅

**SEO Metrics (Google Search Console):**
- Blog traffic: [number] visits
- Top performing post: [title]
- New keywords ranking: [number]
- Average position change: [up/down]

**Engagement (Google Analytics):**
- Avg time on page: 3+ min = good
- Bounce rate: <70% = good
- Pages per session: 1.5+ = good

**Lead Generation:**
- Blog CTA clicks: [number]
- Forms from blog: [number]
- Conversion rate: [%]

---

## 🚨 **Common Problems & Solutions**

### Problem: Blog generator doesn't run
**Solution:**
```bash
chmod +x .claude/blog-generator.sh
```

### Problem: Can't think of what to write
**Solution:**
1. Read top 3 ranking articles for your keyword
2. Use outline templates
3. Expand each bullet point into 200-word paragraph

### Problem: Post is too short
**Solution:**
- Add more examples (client stories)
- Expand "how to" into step-by-step
- Add FAQ section (5-7 questions)
- Include comparison table

### Problem: Taking too long to write
**Solution:**
- Use voice typing (Google Docs)
- Write easiest sections first
- Set 25-min timer per section
- Batch: Create 4 outlines at once

### Problem: Not ranking
**Solution:**
- Wait 30-45 days (normal timeline)
- Check keyword in first 100 words
- Add more internal links
- Get 2-3 backlinks to post
- Share on social media more

---

## 📈 **Success Benchmarks**

### Month 1-3:
- Posts published: 12-15
- Blog traffic: 50-200 visitors/month
- Keywords ranking: 5-10
- Leads from blog: 1-3

### Month 4-6:
- Posts published: 24-30
- Blog traffic: 200-500 visitors/month
- Keywords ranking: 15-25
- Leads from blog: 5-10

### Month 7-12:
- Posts published: 40-52
- Blog traffic: 500-1,500 visitors/month
- Keywords ranking: 30-50
- Leads from blog: 10-20

### Year 2:
- Blog traffic: 20-30% of total site traffic
- Top 10 rankings: 15-25 keywords
- Monthly leads: 15-30 from blog
- Reduced CAC: 40-60% lower than ads

---

## 💡 **Pro Tips**

### Write Faster:
1. **Batch work:** Create 4 outlines in one session
2. **Voice type:** Talk, then edit
3. **Reuse structure:** Same format every week
4. **Set timers:** 25-min sprints
5. **Start with easiest section:** Build momentum

### Rank Higher:
1. **Internal linking:** Link every post to 2-3 service/location pages
2. **Update old posts:** Refresh top performers yearly
3. **Get backlinks:** Share in Facebook groups, forums
4. **Long content:** 2,500+ words rank better
5. **Answer questions:** Use "People Also Ask" from Google

### Generate More Leads:
1. **Strong CTAs:** Every post = clear next step
2. **Lead magnets:** Offer downloadable templates
3. **Email capture:** "Get the checklist" pop-ups
4. **Related services:** Link to relevant service pages
5. **Case studies:** Include real client results

---

## 🎓 **Next Level: Batch Production**

Once comfortable (Month 3+), switch to batching:

### Week 1: Planning
- Create 4 outlines (ChatGPT)
- Research all 4 topics
- Find all 4 images

### Week 2: Writing
- Write all 4 posts
- 2 per day = done in 2 days

### Week 3: Editing
- Edit all 4 posts
- Add images
- SEO optimize

### Week 4: Publishing
- Publish 1 per week
- You're now 3 weeks ahead!

### Benefits:
- More efficient (fewer context switches)
- Better quality (focused sessions)
- Less stress (always have buffer)
- Can take vacation (posts auto-publish)

---

## 📞 **Need Help?**

### Questions About:
- **System setup:** Re-read this file
- **Writing:** Check `WEEKLY_BLOG_WORKFLOW.md`
- **Outlines:** Check `blog-outline-generator.md`
- **Topics:** Check `content-calendar-2025.csv`

### Still Stuck?
Ask Claude (this assistant):
- "How do I [specific task]?"
- "Create outline for [topic]"
- "Review my blog post draft"
- "Generate content calendar for [niche]"

---

## ✨ **Final Notes**

**This system works if you:**
- Follow it consistently (weekly)
- Don't skip steps
- Focus on quality (2,000+ words)
- Be patient (results take 60-90 days)

**Expected Results:**
- Month 3: First post ranks top 20
- Month 6: 5-10 posts in top 20
- Month 12: 15-25 posts in top 10
- Year 2: Blog = 30% of site traffic

**You've Got This!** 🚀

Start with Week 1: "How to Market a Med Spa"
Run: `./.claude/blog-generator.sh "How to Market a Med Spa: Complete 2026 Guide" "how-to-market-med-spa"`

Then follow `WEEKLY_BLOG_WORKFLOW.md` step by step.

---

**System created:** January 2025
**Last updated:** January 2025
**Version:** 1.0
