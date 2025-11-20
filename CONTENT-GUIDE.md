# Content Management Guide
## MedSpa Flywheel Website

**Welcome!** This guide will help you easily update and add content to the MedSpa Flywheel website. No technical expertise required!

---

## Table of Contents

1. [Adding a New Case Study](#1-adding-a-new-case-study)
2. [Adding a New Blog Post](#2-adding-a-new-blog-post)
3. [Adding a New Location Page](#3-adding-a-new-location-page)
4. [Updating Services & Pricing](#4-updating-services--pricing)
5. [Updating Team Members](#5-updating-team-members)
6. [Quick Content Tips](#6-quick-content-tips)

---

## 1. Adding a New Case Study

### Step-by-Step Instructions

#### **Step 1: Copy the Template**

1. Find the file: `case-study-template.html`
2. Make a copy of this file
3. Rename it to match your case study (e.g., `case-study-miami-rejuvenation.html`)
4. Use lowercase letters and dashes (no spaces)

**Example naming:**
- ✅ Good: `case-study-atlanta-medspa.html`
- ❌ Bad: `Case Study Atlanta MedSpa.html`

#### **Step 2: Customize Your New Case Study**

Open your new file and update these sections:

**A. Meta Tags (top of file, lines 5-10):**
```html
<meta name="description" content="[Write 150-160 character summary of the case study]">
<title>[Client Name] Case Study - MedSpa Flywheel</title>
```

**B. Client Information (Hero Section):**
- Replace `[CLIENT NAME]` with actual client name
- Replace `[CITY, STATE]` with location
- Update the client logo image path

**C. Key Metrics (Results Section):**
Update the three metric cards:
- Booking increase percentage
- Revenue growth percentage
- Return on ad spend (ROAS)

**D. Challenge & Solution Sections:**
- Write the client's original problem/challenge
- Describe your solution and approach
- Be specific with numbers and timelines

**E. Results Timeline:**
Replace the timeline milestones with real data:
- Month 1 results
- Month 3 results
- Month 6 results

**F. Testimonial:**
```html
<blockquote>
  <p>"[Client's actual testimonial quote]"</p>
  <footer>— [Client Name], [Title], [Business Name]</footer>
</blockquote>
```

#### **Step 3: Add Images**

**Required Images:**

1. **Client Logo** (recommended: 300x100px, PNG with transparent background)
   - Save as: `images/clients/[client-name]-logo.png`
   - Update path in hero section

2. **Before/After Photos** (recommended: 800x600px each, JPG or WebP)
   - Save as: `images/case-studies/[client-name]-before.jpg`
   - Save as: `images/case-studies/[client-name]-after.jpg`

3. **Featured Image** (recommended: 1200x630px for social sharing)
   - Save as: `images/case-studies/[client-name]-og.jpg`
   - Update Open Graph image path

**Image Optimization Tips:**
- Keep file sizes under 100KB
- Use WebP format when possible (better compression)
- Tools: TinyPNG.com or Squoosh.app

#### **Step 4: Add to Case Studies Index**

Open `case-studies.html` and add a new card in the grid section:

```html
<a href="case-study-[your-filename].html" class="block bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition-all transform hover:-translate-y-2">
    <div class="aspect-w-16 aspect-h-9 bg-gradient-to-br from-primary-100 to-primary-50">
        <img src="images/case-studies/[your-featured-image].jpg"
             alt="[Client Name] Case Study"
             class="object-cover">
    </div>
    <div class="p-8">
        <div class="flex items-center gap-2 text-sm text-primary-600 font-semibold mb-3">
            <span class="px-3 py-1 bg-primary-100 rounded-full">Local SEO</span>
            <span class="px-3 py-1 bg-primary-100 rounded-full">PPC</span>
        </div>
        <h3 class="text-2xl font-bold text-gray-900 mb-3">
            [Client Name]: [Short Compelling Title]
        </h3>
        <p class="text-gray-600 mb-6">
            [1-2 sentence summary of results]
        </p>
        <div class="grid grid-cols-3 gap-4 pt-6 border-t border-gray-200">
            <div>
                <div class="text-3xl font-bold text-primary-600">+180%</div>
                <div class="text-sm text-gray-600">Bookings</div>
            </div>
            <div>
                <div class="text-3xl font-bold text-primary-600">+250%</div>
                <div class="text-sm text-gray-600">Revenue</div>
            </div>
            <div>
                <div class="text-3xl font-bold text-primary-600">6.2x</div>
                <div class="text-sm text-gray-600">ROAS</div>
            </div>
        </div>
    </div>
</a>
```

Place this code inside the `<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">` section.

#### **Step 5: Update Sitemap**

Open `sitemap.xml` and add your new case study:

```xml
<url>
  <loc>https://medspaflywheel.com/case-study-[your-filename].html</loc>
  <priority>0.7</priority>
  <changefreq>monthly</changefreq>
</url>
```

**Done!** Test your new case study by opening the HTML file in a browser.

---

## 2. Adding a New Blog Post

### Step-by-Step Instructions

#### **Step 1: Copy the Template**

1. Find: `blog-post-template.html`
2. Copy and rename to: `blog-[your-topic-slug].html`
3. Use descriptive, SEO-friendly names

**Example naming:**
- ✅ `blog-how-to-market-botox-services.html`
- ✅ `blog-5-social-media-tips-med-spas.html`
- ❌ `blog-post-1.html`

#### **Step 2: Update Meta Information**

**A. SEO Meta Tags (lines 5-15):**
```html
<title>[Your Compelling Blog Title] | MedSpa Flywheel</title>
<meta name="description" content="[150-160 character summary that makes people want to click]">
<meta name="keywords" content="[5-8 relevant keywords, comma separated]">
```

**Title Writing Tips:**
- Keep under 60 characters
- Include main keyword
- Make it compelling (use numbers, power words)
- Examples:
  - "7 Proven Ways to Market Your Med Spa on Instagram"
  - "How to Double Your Botox Bookings in 90 Days"
  - "Med Spa Marketing Trends You Can't Ignore in 2024"

**B. Open Graph & Social Tags:**
```html
<meta property="og:title" content="[Your Blog Title]">
<meta property="og:description" content="[Compelling summary for social shares]">
<meta property="og:image" content="https://medspaflywheel.com/images/blog/[your-post-image].jpg">
```

#### **Step 3: Write Your Article Content**

**Header Section:**
Replace these elements:
- Article title (H1)
- Author name
- Publication date
- Category tags
- Reading time estimate (count words ÷ 200 = minutes)

**Article Body:**
The template has a complete article structure. Replace with your content:

1. **Introduction** (1-2 paragraphs)
   - Hook the reader
   - State the problem
   - Promise the solution

2. **Main Content** (Use H2 and H3 headings)
   - Break into clear sections
   - Use numbered lists and bullet points
   - Add relevant statistics and data
   - Include actionable tips

3. **Conclusion** (1-2 paragraphs)
   - Summarize key points
   - Include strong call-to-action

**Formatting Tips:**
- Use `<h2>` for main sections
- Use `<h3>` for subsections
- Wrap paragraphs in `<p>` tags
- Create lists with `<ul>` and `<li>` tags
- Use `<strong>` for bold text
- Use `<em>` for italic text

**Example Structure:**
```html
<h2>1. Optimize Your Instagram Profile</h2>
<p>Your Instagram profile is your first impression. Here's how to make it count:</p>

<h3>Profile Photo</h3>
<p>Use your logo or a professional headshot. Make sure it's recognizable even at small sizes.</p>

<ul>
  <li><strong>Size:</strong> 320x320 pixels minimum</li>
  <li><strong>Format:</strong> PNG or JPG</li>
  <li><strong>Tip:</strong> Keep it consistent across all social platforms</li>
</ul>

<h3>Bio Optimization</h3>
<p>You have 150 characters to convince someone to follow you. Use them wisely...</p>
```

#### **Step 4: Add Images**

**Required Images:**

1. **Featured Image** (1200x630px)
   - Save as: `images/blog/[post-slug]-featured.jpg`
   - Update in hero section and Open Graph tags
   - This appears when shared on social media

2. **Author Photo** (200x200px, circular crop looks best)
   - Save as: `images/team/[author-name].jpg`
   - Update in author bio section

3. **In-Article Images** (800px wide recommended)
   - Save as: `images/blog/[descriptive-name].jpg`
   - Add with proper alt text:
   ```html
   <img src="images/blog/[image-name].jpg"
        alt="[Descriptive text for accessibility and SEO]"
        class="rounded-xl shadow-lg">
   ```

#### **Step 5: Update Author Bio**

Find the author bio section and update:
```html
<div class="author-bio">
  <img src="images/team/[author-photo].jpg" alt="[Author Name]">
  <div>
    <h3>[Author Name]</h3>
    <p class="text-gray-600">[Job Title]</p>
    <p class="mt-2">[Brief bio - 2-3 sentences about expertise and background]</p>
  </div>
</div>
```

#### **Step 6: Add Related Posts**

At the bottom, update the "Related Posts" section with 3 relevant articles:

```html
<a href="blog-[related-post].html" class="...">
  <img src="images/blog/[related-thumbnail].jpg" alt="...">
  <div class="p-6">
    <span class="text-primary-600 text-sm font-semibold">[Category]</span>
    <h3 class="text-xl font-bold mt-2 mb-3">[Related Post Title]</h3>
    <p class="text-gray-600">[Brief excerpt]</p>
  </div>
</a>
```

#### **Step 7: Add to Blog Index**

Open `blog.html` and add your post to the grid:

**For Featured Post** (large, top position):
```html
<a href="blog-[your-post].html" class="block bg-white rounded-2xl shadow-xl overflow-hidden hover:shadow-2xl transition-all transform hover:-translate-y-1">
  <div class="md:flex">
    <div class="md:w-2/5">
      <img src="images/blog/[your-featured-image].jpg" alt="[Your Title]" class="w-full h-full object-cover">
    </div>
    <div class="md:w-3/5 p-8">
      <div class="flex items-center gap-3 text-sm mb-4">
        <span class="px-3 py-1 bg-primary-100 text-primary-700 rounded-full font-semibold">[Category]</span>
        <span class="text-gray-500">[Date]</span>
      </div>
      <h2 class="text-3xl font-bold text-gray-900 mb-4 hover:text-primary-600 transition-colors">
        [Your Blog Post Title]
      </h2>
      <p class="text-gray-600 text-lg mb-6 leading-relaxed">
        [Compelling 2-3 sentence excerpt that makes people want to read more]
      </p>
      <div class="flex items-center gap-3">
        <img src="images/team/[author].jpg" alt="[Author]" class="w-10 h-10 rounded-full">
        <div>
          <div class="font-semibold text-gray-900">[Author Name]</div>
          <div class="text-sm text-gray-500">[Read Time] min read</div>
        </div>
      </div>
    </div>
  </div>
</a>
```

**For Regular Post** (in grid):
```html
<a href="blog-[your-post].html" class="block bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-all transform hover:-translate-y-1">
  <img src="images/blog/[thumbnail].jpg" alt="[Title]" class="w-full h-48 object-cover">
  <div class="p-6">
    <div class="flex items-center gap-2 text-sm mb-3">
      <span class="px-3 py-1 bg-primary-100 text-primary-700 rounded-full font-semibold">[Category]</span>
      <span class="text-gray-500">[Date]</span>
    </div>
    <h3 class="text-xl font-bold text-gray-900 mb-3 hover:text-primary-600 transition-colors">
      [Your Post Title]
    </h3>
    <p class="text-gray-600 mb-4">
      [Brief 1-2 sentence excerpt]
    </p>
    <div class="flex items-center justify-between pt-4 border-t border-gray-200">
      <div class="flex items-center gap-2">
        <img src="images/team/[author].jpg" alt="[Author]" class="w-8 h-8 rounded-full">
        <span class="text-sm font-medium text-gray-900">[Author]</span>
      </div>
      <span class="text-sm text-gray-500">[X] min read</span>
    </div>
  </div>
</a>
```

#### **Step 8: Blog Post SEO Checklist**

Before publishing, verify:

- [ ] Title is under 60 characters
- [ ] Meta description is 150-160 characters
- [ ] Main keyword appears in title, first paragraph, and at least one H2
- [ ] URL is descriptive and includes main keyword
- [ ] Featured image has descriptive alt text
- [ ] All images have alt text
- [ ] Article is at least 800 words (1,500+ is ideal)
- [ ] Internal links to other blog posts or pages (3-5 links)
- [ ] External links to authoritative sources (if relevant)
- [ ] Clear call-to-action at the end
- [ ] No spelling or grammar errors
- [ ] Mobile-friendly (test on phone)

#### **Step 9: Update Sitemap**

Add to `sitemap.xml`:
```xml
<url>
  <loc>https://medspaflywheel.com/blog-[your-post].html</loc>
  <priority>0.8</priority>
  <changefreq>monthly</changefreq>
</url>
```

**Done!** Preview your blog post in a browser before going live.

---

## 3. Adding a New Location Page

### Step-by-Step Instructions

#### **Step 1: Copy the Template**

1. Find: `location-template.html`
2. Copy and rename to: `[city-name]-[state-abbreviation].html`
3. Use lowercase, no spaces

**Examples:**
- `austin-tx.html`
- `charlotte-nc.html`
- `tampa-fl.html`

#### **Step 2: Find and Replace**

Open your new location file and replace these placeholders throughout the entire file:

| **Placeholder** | **Replace With** | **Example** |
|-----------------|------------------|-------------|
| `[CITY]` | City name | `Austin` |
| `[STATE]` | Full state name | `Texas` |
| `[STATE_ABBREV]` | State abbreviation | `TX` |
| `[CITY_SLUG]` | Lowercase city-state | `austin-tx` |
| `[POPULATION]` | Metro population | `2.3M` |
| `[MEDIAN_INCOME]` | Median household income | `$75,000` |
| `[TARGET_AGE]` | Target demographic age | `38` |
| `[LATITUDE]` | City latitude | `30.2672` |
| `[LONGITUDE]` | City longitude | `-97.7431` |

**How to Find & Replace:**
- Most text editors: Press `Ctrl+H` (Windows) or `Cmd+F` (Mac)
- Find: `[CITY]`
- Replace with: `Austin`
- Click "Replace All"
- Repeat for each placeholder

#### **Step 3: Update Neighborhoods & Areas**

Find the "Service Area" section and update these lists:

**Neighborhoods** (3-5 upscale areas where med spa clients live):
```html
<ul>
  <li>Downtown Austin</li>
  <li>Westlake Hills</li>
  <li>Tarrytown</li>
  <li>Barton Creek</li>
  <li>Hyde Park</li>
</ul>
```

**Nearby Cities** (4-6 cities within 20-30 miles):
```html
<ul>
  <li>Round Rock</li>
  <li>Cedar Park</li>
  <li>Georgetown</li>
  <li>Pflugerville</li>
</ul>
```

**Suburbs** (3-5 affluent suburbs):
```html
<ul>
  <li>Lakeway</li>
  <li>Bee Cave</li>
  <li>West Lake Hills</li>
  <li>Rollingwood</li>
</ul>
```

**Research Tips:**
- Google: "[City] affluent neighborhoods"
- Check Zillow for median home prices by neighborhood
- Target areas with homes $400K+
- Look for areas with spa/wellness businesses

#### **Step 4: Customize Local Content**

**A. Local Market Insights Section:**

Update the statistics and local details:
```html
<p>The [CITY] metro area is home to [POPULATION] residents with a median household income of [MEDIAN_INCOME]. The target demographic for med spa services—ages 35-55 with disposable income—represents approximately [X]% of the population, creating a robust market for aesthetic services.</p>
```

Add local flavor:
- Mention local characteristics (e.g., "Austin's health-conscious culture")
- Reference local events or lifestyle
- Note competitive landscape
- Highlight growth trends

**B. Update Local Results:**

Customize the case study examples to feel local:
```html
<h3>[Nearby Neighborhood] Med Spa - [X]% Revenue Growth</h3>
<p>A medical spa in [specific area of city] was struggling with...</p>
```

Make it feel authentic to that location.

#### **Step 5: Get Coordinates**

For the LocalBusiness schema (helps with local SEO):

1. Go to: https://www.latlong.net/
2. Enter your city name
3. Copy the latitude and longitude
4. Replace `[LATITUDE]` and `[LONGITUDE]` in the schema section

#### **Step 6: Add to Locations Index**

Open `locations.html` and find the correct state section.

Add your city card:
```html
<a href="[city-slug].html" class="block bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all transform hover:-translate-y-1">
  <div class="flex items-center justify-between mb-4">
    <h3 class="text-2xl font-bold text-gray-900">[City Name]</h3>
    <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
    </svg>
  </div>
  <p class="text-gray-600 mb-4">
    [1-2 sentence description highlighting why this market is great for med spas]
  </p>
  <div class="flex items-center text-primary-600 font-semibold">
    Learn More
    <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
    </svg>
  </div>
</a>
```

Place it in alphabetical order within the state section.

#### **Step 7: Update Sitemap**

Add to `sitemap.xml`:
```xml
<url>
  <loc>https://medspaflywheel.com/[city-slug].html</loc>
  <priority>0.7</priority>
  <changefreq>monthly</changefreq>
</url>
```

### What Makes Good Local Content?

**Do:**
- ✅ Mention specific neighborhoods and landmarks
- ✅ Reference local demographics and market data
- ✅ Use local terminology and area names
- ✅ Include relevant local statistics
- ✅ Highlight area-specific advantages

**Don't:**
- ❌ Use generic content that could apply anywhere
- ❌ Copy-paste from other location pages without customizing
- ❌ Make up statistics or data
- ❌ Forget to update all placeholders
- ❌ Use incorrect neighborhood or city names

**Local Content Quality Check:**
Read your page and ask: "Could this only be about [City]?" If you could swap the city name and it would work for any city, add more local details.

---

## 4. Updating Services & Pricing

### Which Files to Edit

**Main Services Page:** `services.html`

This is your primary services page with detailed descriptions.

### How to Update Services

#### **Adding a New Service**

Find the services grid section and add a new card:

```html
<div class="bg-white rounded-2xl shadow-xl p-8 hover:shadow-2xl transition-all transform hover:-translate-y-1">
  <!-- Icon -->
  <div class="w-16 h-16 bg-gradient-to-br from-primary-500 to-primary-600 rounded-xl flex items-center justify-center mb-6 shadow-lg">
    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      [Choose an appropriate icon SVG path]
    </svg>
  </div>

  <!-- Service Title -->
  <h3 class="text-2xl font-bold text-gray-900 mb-4">
    [Service Name]
  </h3>

  <!-- Service Description -->
  <p class="text-gray-600 mb-6 leading-relaxed">
    [2-3 sentences describing what this service includes and who it's for]
  </p>

  <!-- Key Features List -->
  <ul class="space-y-3 mb-8">
    <li class="flex items-start gap-3">
      <svg class="w-6 h-6 text-primary-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
      </svg>
      <span class="text-gray-700">[Key feature or benefit]</span>
    </li>
    <li class="flex items-start gap-3">
      <svg class="w-6 h-6 text-primary-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
      </svg>
      <span class="text-gray-700">[Key feature or benefit]</span>
    </li>
    [Add more features as needed]
  </ul>

  <!-- Call to Action -->
  <a href="contact.html" class="inline-block w-full text-center px-6 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition-colors">
    Learn More
  </a>
</div>
```

#### **Updating Existing Service Descriptions**

1. Find the service card you want to update
2. Edit the text within the `<p>` tags for descriptions
3. Update the bullet points in the `<ul>` section
4. Keep descriptions clear and benefit-focused

#### **Updating Pricing Information**

If you have a pricing section, update it carefully:

```html
<div class="pricing-card">
  <h4 class="text-xl font-bold mb-2">[Package Name]</h4>
  <div class="text-4xl font-bold text-primary-600 mb-4">
    $[PRICE]<span class="text-lg text-gray-600">/month</span>
  </div>
  <ul class="space-y-2 mb-6">
    <li>✓ [What's included]</li>
    <li>✓ [What's included]</li>
    <li>✓ [What's included]</li>
  </ul>
</div>
```

### Maintaining Consistency

When updating services across the site:

**1. Homepage (`index.html`)**
- Update the services overview section
- Keep it high-level (1-2 sentences per service)
- Ensure service names match exactly

**2. Services Page (`services.html`)**
- Detailed descriptions (2-3 paragraphs)
- Full feature lists
- This is your comprehensive service page

**3. About Page (`about.html`)**
- May reference services in "What We Do" section
- Keep aligned with services page

**Consistency Checklist:**
- [ ] Service names are identical everywhere
- [ ] Pricing matches across all pages
- [ ] Feature lists don't contradict each other
- [ ] CTAs point to the same place
- [ ] Terminology is consistent (don't say "PPC" on one page and "Paid Advertising" on another unless you explain they're the same)

---

## 5. Updating Team Members

### Where to Edit

**Main File:** `about.html`

Find the "Meet Our Team" section (usually near the bottom of the page).

### How to Add a New Team Member

#### **Step 1: Prepare Team Member Photo**

**Image Requirements:**
- **Dimensions:** 400x400 pixels (square)
- **Format:** JPG or PNG
- **File size:** Under 100KB
- **Style:** Professional headshot with consistent background
- **Naming:** `firstname-lastname.jpg` (lowercase, no spaces)

**Photo Tips:**
- Use the same background style as other team photos
- Professional attire
- Good lighting
- Friendly, approachable expression
- Centered composition

**Where to save:** `images/team/firstname-lastname.jpg`

#### **Step 2: Add Team Member Card**

Find the team grid and add:

```html
<div class="text-center">
  <!-- Photo -->
  <div class="relative inline-block mb-6">
    <img src="images/team/[firstname-lastname].jpg"
         alt="[Full Name], [Job Title]"
         class="w-48 h-48 rounded-full object-cover shadow-xl mx-auto">
    <div class="absolute -bottom-2 -right-2 w-12 h-12 bg-primary-600 rounded-full flex items-center justify-center shadow-lg">
      <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
      </svg>
    </div>
  </div>

  <!-- Name & Title -->
  <h3 class="text-2xl font-bold text-gray-900 mb-2">
    [Full Name]
  </h3>
  <p class="text-primary-600 font-semibold mb-4">
    [Job Title]
  </p>

  <!-- Bio -->
  <p class="text-gray-600 leading-relaxed mb-6">
    [2-3 sentences about their background, expertise, and what they bring to the team. Keep it professional but personable.]
  </p>

  <!-- Social Links (Optional) -->
  <div class="flex items-center justify-center gap-3">
    <a href="[LinkedIn URL]" class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center hover:bg-primary-600 hover:text-white transition-colors">
      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
        <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
      </svg>
    </a>
  </div>
</div>
```

#### **Step 3: Update Team Member Order**

Typically, team members appear in order of:
1. Founders/CEO
2. Leadership team
3. Senior staff
4. Staff members

Arrange your team cards in the appropriate order within the grid.

### How to Update an Existing Team Member

1. Find their card in `about.html`
2. Update any of these elements:
   - Photo: Replace image file (keep same filename, or update path)
   - Name: Update `<h3>` tag
   - Title: Update `<p class="text-primary-600">` tag
   - Bio: Update the description paragraph
   - Social links: Update href URLs

### Team Bio Writing Tips

**Good Bio Example:**
> "Sarah has 10+ years of experience in digital marketing for healthcare businesses. She specializes in Google Ads strategy and has helped over 50 med spas grow their patient base. Outside of work, she's an avid yoga practitioner."

**What to Include:**
- Years of experience
- Specific expertise or specialization
- Notable achievements or numbers
- One personal detail (makes them relatable)

**What to Avoid:**
- Generic buzzwords without substance
- Overly formal or stiff language
- Going over 3-4 sentences
- Information that will quickly become outdated

---

## 6. Quick Content Tips

### Writing for the Med Spa Audience

#### **Know Your Audience**

**Primary Audience:**
- Med spa owners and managers
- Ages 35-60
- Business-savvy but may not be marketing experts
- Looking for proven strategies and ROI
- Value professionalism and results

**Tone & Style:**
- Professional but approachable
- Confident without being arrogant
- Data-driven (use numbers and statistics)
- Solution-focused
- Empathetic to their challenges

#### **Power Words for Med Spa Marketing**

Use these words to create compelling content:

**Results-Focused:**
- Proven
- Guaranteed
- Increase
- Growth
- ROI (Return on Investment)
- Revenue
- Bookings
- Conversions

**Trust-Building:**
- Expert
- Specialized
- Certified
- Experience
- Track record
- Success stories
- Testimonials

**Action-Oriented:**
- Transform
- Optimize
- Scale
- Accelerate
- Launch
- Implement
- Achieve

### SEO Best Practices

#### **Keyword Research**

Before writing, identify your target keywords:

**Tools:**
- Google Keyword Planner (free)
- Ubersuggest (free tier available)
- Answer the Public (free)
- Google Search autocomplete

**Target Keywords for Med Spa Marketing:**
- "med spa marketing"
- "medical spa advertising"
- "aesthetic clinic marketing"
- "botox marketing"
- "med spa google ads"
- "medical spa social media"
- "[city] med spa marketing"

#### **On-Page SEO Checklist**

For every page you create:

**1. Title Tag**
- [ ] Include primary keyword
- [ ] Under 60 characters
- [ ] Compelling and clickable
- [ ] Unique for each page

**2. Meta Description**
- [ ] 150-160 characters
- [ ] Include primary keyword
- [ ] Include call-to-action
- [ ] Compelling summary

**3. Headings**
- [ ] One H1 per page (main title)
- [ ] H2s for main sections
- [ ] H3s for subsections
- [ ] Keywords in at least one H2

**4. Content**
- [ ] Primary keyword in first 100 words
- [ ] Keyword density 1-2% (natural usage)
- [ ] Minimum 300 words (800+ for blog posts)
- [ ] Easy to read (short paragraphs, bullet points)
- [ ] No keyword stuffing

**5. Images**
- [ ] Descriptive file names (not IMG_1234.jpg)
- [ ] Alt text with keywords (naturally)
- [ ] Compressed for fast loading
- [ ] Relevant to content

**6. Links**
- [ ] 2-5 internal links to other pages
- [ ] External links to authoritative sources
- [ ] Descriptive anchor text (not "click here")

#### **Content Length Guidelines**

| Page Type | Minimum Words | Ideal Length |
|-----------|---------------|--------------|
| Homepage | 500 | 800-1,200 |
| Service Pages | 500 | 800-1,500 |
| About Page | 400 | 600-1,000 |
| Case Studies | 600 | 1,000-1,500 |
| Blog Posts | 800 | 1,500-2,500 |
| Location Pages | 500 | 800-1,200 |

**Quality over Quantity:** Don't add fluff just to hit word count. Every sentence should provide value.

### Call-to-Action (CTA) Guidelines

#### **Effective CTA Formulas**

**Formula 1: Action + Benefit**
- ✅ "Get Your Free Strategy Call"
- ✅ "Download the Complete Guide"
- ✅ "See Your Custom Plan"

**Formula 2: Remove Risk**
- ✅ "Try Risk-Free for 30 Days"
- ✅ "No Obligation Consultation"
- ✅ "Free Initial Audit"

**Formula 3: Create Urgency**
- ✅ "Limited Spots Available"
- ✅ "Book Your Strategy Call Today"
- ✅ "Get Started This Week"

#### **CTA Placement**

Place CTAs in these locations:

1. **Above the fold** (top of homepage)
2. **After describing a benefit** (services page)
3. **End of case studies** (convert impressed readers)
4. **End of blog posts** (while they're engaged)
5. **Footer** (always available)

#### **CTA Button Best Practices**

**Button Text:**
- ✅ "Schedule My Free Call"
- ✅ "Get My Custom Strategy"
- ✅ "Download Free Guide"
- ❌ "Submit"
- ❌ "Click Here"
- ❌ "Learn More" (too vague)

**Design:**
- Use contrasting colors (stands out)
- Make it large enough to click easily
- Add hover effects
- Use action-oriented language
- Make it clear what happens when clicked

### Content Writing Checklist

Before publishing any content:

**Clarity:**
- [ ] Is the main point clear within the first paragraph?
- [ ] Would someone unfamiliar with marketing understand this?
- [ ] Are there any jargon terms that need explanation?
- [ ] Is the structure logical and easy to follow?

**Engagement:**
- [ ] Does the opening hook the reader?
- [ ] Are there specific examples or data points?
- [ ] Is it visually scannable (headings, bullets, short paragraphs)?
- [ ] Does it answer the reader's likely questions?

**Action:**
- [ ] Is there a clear next step?
- [ ] Is the CTA compelling?
- [ ] Would this content motivate someone to contact us?

**Quality:**
- [ ] No spelling or grammar errors
- [ ] All links work
- [ ] Images load properly
- [ ] Looks good on mobile
- [ ] All placeholders replaced

### Quick Writing Tips

**1. Start with an Outline**
Before writing, create a simple outline:
```
I. Introduction
   - Hook
   - Problem statement
   - What this article covers

II. Main Points
   A. First main section
      - Supporting point
      - Supporting point
   B. Second main section
      - Supporting point
      - Supporting point

III. Conclusion
   - Summary
   - Call-to-action
```

**2. Use the Inverted Pyramid**
- Most important information first
- Supporting details in the middle
- Background info last

**3. Keep Sentences Short**
- Aim for 15-20 words per sentence
- Vary sentence length for rhythm
- One idea per sentence

**4. Write for Scanners**
Most people scan, not read. Help them:
- Use descriptive subheadings
- Highlight key points in **bold**
- Use bullet points and numbered lists
- Keep paragraphs to 3-4 sentences max

**5. Use Active Voice**
- ✅ "We increased bookings by 180%"
- ❌ "Bookings were increased by 180%"

**6. Add Specific Numbers**
- ✅ "213% increase in bookings"
- ❌ "Significant increase in bookings"

**7. Answer Questions Clearly**
Structure content as Q&A when possible:
- What is [topic]?
- Why does it matter?
- How does it work?
- What are the benefits?
- How do I get started?

---

## Need Help?

### Common Issues

**Q: I updated content but don't see changes**
**A:** Hard refresh your browser:
- Windows: `Ctrl + F5`
- Mac: `Cmd + Shift + R`

**Q: Images aren't showing up**
**A:** Check:
1. Image file path is correct
2. Image file name matches exactly (case-sensitive)
3. Image is in the correct folder
4. Image file isn't corrupted

**Q: I broke something!**
**A:** Don't panic:
1. Use your text editor's "Undo" function
2. Or revert to the template file
3. Or restore from backup

**Q: How do I know if my content is SEO-friendly?**
**A:** Use these free tools:
- Yoast SEO (WordPress plugin, but has guidelines)
- Google Search Console (see how Google views your pages)
- PageSpeed Insights (performance and SEO tips)

### Resources

**Image Tools:**
- [TinyPNG](https://tinypng.com/) - Compress images
- [Squoosh](https://squoosh.app/) - Image optimization
- [Canva](https://canva.com/) - Create graphics

**SEO Tools:**
- [Google Keyword Planner](https://ads.google.com/home/tools/keyword-planner/)
- [Answer the Public](https://answerthepublic.com/)
- [Google Search Console](https://search.google.com/search-console)

**Writing Tools:**
- [Grammarly](https://grammarly.com/) - Grammar and spell check
- [Hemingway Editor](http://hemingwayapp.com/) - Readability checker
- [CoSchedule Headline Analyzer](https://coschedule.com/headline-analyzer)

---

**Questions or Suggestions?**

If you have questions about managing content or suggestions for improving this guide, please contact the development team.

**Last Updated:** 2024-01-15
**Guide Version:** 1.0
