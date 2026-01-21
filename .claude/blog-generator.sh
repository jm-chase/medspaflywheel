#!/bin/bash

# MedSpa Flywheel - Automated Blog Post Generator
# Usage: ./blog-generator.sh "Blog Topic" "primary-keyword"

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check arguments
if [ $# -lt 2 ]; then
    echo -e "${YELLOW}Usage: ./blog-generator.sh \"Blog Topic\" \"primary-keyword\"${NC}"
    echo "Example: ./blog-generator.sh \"How to Market a Med Spa\" \"how-to-market-med-spa\""
    exit 1
fi

TOPIC="$1"
KEYWORD="$2"
DATE=$(date +"%Y-%m-%d")
SLUG=$(echo "$KEYWORD" | tr ' ' '-')
FILENAME="blog/${SLUG}.html"

echo -e "${BLUE}🚀 Generating blog post...${NC}"
echo "Topic: $TOPIC"
echo "Keyword: $KEYWORD"
echo "File: $FILENAME"
echo ""

# Create blog directory if it doesn't exist
mkdir -p blog
mkdir -p images/blog

# Generate the blog post HTML
cat > "$FILENAME" << 'BLOGPOST'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="EDIT_META_DESCRIPTION">
    <link rel="canonical" href="https://medspaflywheel.com/EDIT_FILENAME">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="EDIT_TITLE">
    <meta property="og:description" content="EDIT_OG_DESCRIPTION">
    <meta property="og:image" content="https://medspaflywheel.com/images/blog/EDIT_IMAGE.jpg">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="EDIT_TITLE">
    <meta name="twitter:description" content="EDIT_TWITTER_DESC">
    <meta name="twitter:image" content="https://medspaflywheel.com/images/blog/EDIT_IMAGE.jpg">

    <title>EDIT_TITLE | MedSpa Flywheel</title>

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RL2PXG1Y0X"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-RL2PXG1Y0X');
    </script>

    <!-- Schema Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "EDIT_TITLE",
      "image": "https://medspaflywheel.com/images/blog/EDIT_IMAGE.jpg",
      "author": {
        "@type": "Person",
        "name": "James Chase"
      },
      "publisher": {
        "@type": "Organization",
        "name": "MedSpa Flywheel",
        "logo": {
          "@type": "ImageObject",
          "url": "https://medspaflywheel.com/images/logo/medspaflywheel.png"
        }
      },
      "datePublished": "EDIT_DATE",
      "dateModified": "EDIT_DATE"
    }
    </script>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" media="print" onload="this.media='all'">

    <style>
        body { font-family: 'Inter', sans-serif; }
        .prose { max-width: 65ch; }
        .prose h2 { font-size: 2rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; }
        .prose h3 { font-size: 1.5rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; }
        .prose p { margin-bottom: 1rem; line-height: 1.75; }
        .prose ul, .prose ol { margin-bottom: 1rem; padding-left: 1.5rem; }
        .prose li { margin-bottom: 0.5rem; }
    </style>
</head>
<body class="bg-gray-50">

    <!-- Navigation (copy from index.html) -->

    <!-- Article -->
    <article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20">

        <!-- Breadcrumb -->
        <nav class="mb-8">
            <ol class="flex items-center space-x-2 text-sm">
                <li><a href="/" class="text-gray-500 hover:text-primary-600">Home</a></li>
                <li class="text-gray-400">/</li>
                <li><a href="/blog.html" class="text-gray-500 hover:text-primary-600">Blog</a></li>
                <li class="text-gray-400">/</li>
                <li class="text-primary-600 font-semibold">EDIT_BREADCRUMB</li>
            </ol>
        </nav>

        <!-- Article Header -->
        <header class="mb-12">
            <h1 class="text-5xl font-bold text-gray-900 mb-4">
                EDIT_H1_TITLE
            </h1>
            <div class="flex items-center gap-4 text-sm text-gray-600">
                <span>By James Chase</span>
                <span>•</span>
                <time datetime="EDIT_DATE">EDIT_DATE_FORMATTED</time>
                <span>•</span>
                <span>EDIT_READ_TIME min read</span>
            </div>
        </header>

        <!-- Featured Image -->
        <div class="mb-12">
            <img src="/images/blog/EDIT_IMAGE.jpg" alt="EDIT_ALT_TEXT" class="w-full h-auto rounded-xl shadow-lg">
        </div>

        <!-- Article Content -->
        <div class="prose prose-lg">

            <!-- EDIT: Start writing your content here -->

            <p class="text-xl text-gray-600 font-medium mb-8">
                [HOOK: Start with a compelling statistic or problem statement that includes your primary keyword]
            </p>

            <p>
                [INTRODUCTION: 200 words explaining what this article covers and why it matters. Include primary keyword in first 100 words.]
            </p>

            <h2>Section 1: [Main Point]</h2>

            <p>
                [Content here - 300-500 words per section]
            </p>

            <h3>Subsection</h3>

            <p>
                [More detailed content]
            </p>

            <ul>
                <li>[Bullet point 1]</li>
                <li>[Bullet point 2]</li>
                <li>[Bullet point 3]</li>
            </ul>

            <!-- INTERNAL LINK EXAMPLE -->
            <p>
                Want help implementing this? <a href="/services.html" class="text-primary-600 hover:text-primary-700 font-semibold">Learn about our services</a>.
            </p>

            <h2>Section 2: [Next Main Point]</h2>

            <p>
                [Content continues...]
            </p>

            <!-- Continue with 5-7 main sections -->

            <h2>Conclusion</h2>

            <p>
                [Recap main points and provide clear next steps]
            </p>

            <!-- CTA -->
            <div class="mt-12 p-8 bg-gradient-to-br from-primary-50 to-accent-50 rounded-xl border border-primary-200">
                <h3 class="text-2xl font-bold text-gray-900 mb-3">Ready to Grow Your Med Spa?</h3>
                <p class="text-gray-700 mb-6">
                    Get a free marketing audit and discover exactly how to increase bookings by 180%.
                </p>
                <a href="/contact.html" class="inline-flex items-center px-6 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition">
                    Get Free Audit
                    <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                    </svg>
                </a>
            </div>

        </div>

    </article>

    <!-- Footer (copy from index.html) -->

</body>
</html>
BLOGPOST

# Replace placeholders
sed -i "s|EDIT_FILENAME|$FILENAME|g" "$FILENAME"
sed -i "s|EDIT_DATE|$DATE|g" "$FILENAME"

echo -e "${GREEN}✅ Blog post template created!${NC}"
echo ""
echo -e "${YELLOW}📝 Next steps:${NC}"
echo "1. Edit the file: $FILENAME"
echo "2. Replace all EDIT_ placeholders with actual content"
echo "3. Write 2,000-2,500 words of content"
echo "4. Find/create featured image and save as: images/blog/${SLUG}.jpg"
echo "5. Review for SEO (keyword in H1, first 100 words, meta tags)"
echo "6. Publish!"
echo ""
echo -e "${BLUE}📊 SEO Checklist:${NC}"
echo "☐ Primary keyword in title"
echo "☐ Primary keyword in H1"
echo "☐ Primary keyword in first 100 words"
echo "☐ 2-3 internal links to service/location pages"
echo "☐ 1-2 external links to authority sites"
echo "☐ Featured image (1200x630px)"
echo "☐ Alt tags on all images"
echo "☐ Meta description under 160 characters"
echo ""
