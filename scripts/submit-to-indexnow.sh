#!/bin/bash

# IndexNow Submission Script for MedSpa Flywheel
# This script submits URLs to IndexNow API to notify search engines of content changes

HOST="medspaflywheel.com"
KEY="b78d8c7a35784a0b8077235e720af300"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
INDEXNOW_API="https://api.indexnow.org/indexnow"

# Function to submit a single URL
submit_url() {
    local url=$1
    echo "Submitting: $url"

    response=$(curl -s -w "\n%{http_code}" -X POST "$INDEXNOW_API" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "{
            \"host\": \"${HOST}\",
            \"key\": \"${KEY}\",
            \"keyLocation\": \"${KEY_LOCATION}\",
            \"urlList\": [
                \"${url}\"
            ]
        }")

    http_code=$(echo "$response" | tail -n 1)
    body=$(echo "$response" | head -n -1)

    case $http_code in
        200)
            echo "✓ Success: $url"
            ;;
        400)
            echo "✗ Bad request for $url - Invalid format"
            ;;
        403)
            echo "✗ Forbidden for $url - Key not valid"
            ;;
        422)
            echo "✗ Unprocessable Entity for $url - URL doesn't belong to host"
            ;;
        429)
            echo "✗ Too Many Requests - Rate limited"
            return 1
            ;;
        *)
            echo "✗ Error $http_code for $url"
            ;;
    esac

    # Small delay to avoid rate limiting
    sleep 0.5
}

# Function to submit batch of URLs
submit_batch() {
    local urls=("$@")
    local url_list=""

    for url in "${urls[@]}"; do
        if [ -z "$url_list" ]; then
            url_list="\"$url\""
        else
            url_list="$url_list,\"$url\""
        fi
    done

    echo "Submitting batch of ${#urls[@]} URLs..."

    response=$(curl -s -w "\n%{http_code}" -X POST "$INDEXNOW_API" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "{
            \"host\": \"${HOST}\",
            \"key\": \"${KEY}\",
            \"keyLocation\": \"${KEY_LOCATION}\",
            \"urlList\": [${url_list}]
        }")

    http_code=$(echo "$response" | tail -n 1)

    case $http_code in
        200)
            echo "✓ Success: Submitted ${#urls[@]} URLs"
            ;;
        400)
            echo "✗ Bad request - Invalid format"
            ;;
        403)
            echo "✗ Forbidden - Key not valid"
            ;;
        422)
            echo "✗ Unprocessable Entity - URLs don't belong to host"
            ;;
        429)
            echo "✗ Too Many Requests - Rate limited"
            ;;
        *)
            echo "✗ Error $http_code"
            ;;
    esac
}

# Function to extract URLs from sitemap
extract_urls_from_sitemap() {
    if [ -f "sitemap.xml" ]; then
        grep -oP '(?<=<loc>).*?(?=</loc>)' sitemap.xml
    else
        echo "Error: sitemap.xml not found" >&2
        exit 1
    fi
}

# Main script
echo "=========================================="
echo "IndexNow Submission for MedSpa Flywheel"
echo "=========================================="
echo ""

# Check if specific URLs provided as arguments
if [ $# -gt 0 ]; then
    echo "Submitting specific URLs..."
    for url in "$@"; do
        submit_url "$url"
    done
else
    # Extract all URLs from sitemap
    echo "Extracting URLs from sitemap.xml..."
    mapfile -t urls < <(extract_urls_from_sitemap)
    echo "Found ${#urls[@]} URLs"
    echo ""

    # Submit in batch (IndexNow supports up to 10,000 URLs per request)
    submit_batch "${urls[@]}"
fi

echo ""
echo "=========================================="
echo "Submission complete!"
echo "=========================================="
