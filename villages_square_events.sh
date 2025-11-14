#!/bin/bash

# =============================================================================
# VENUE ABBREVIATION KEYWORDS - Add new keywords here as needed
# =============================================================================
declare -A VENUE_KEYWORDS=(
    ["Brownwood"]="Brownwood"
    ["Sawgrass"]="Sawgrass"
    ["Spanish Springs"]="Spanish Springs"
    ["Lake Sumter"]="Lake Sumter"
)

# Function to abbreviate venue names
abbreviate_venue() {
    local venue="$1"
    for keyword in "${!VENUE_KEYWORDS[@]}"; do
        if [[ "$venue" == *"$keyword"* ]]; then
            echo "${VENUE_KEYWORDS[$keyword]}"
            return
        fi
    done
    # If no keyword matches, return original venue name
    echo "$venue"
}

# =============================================================================
# MAIN SCRIPT
# =============================================================================

# Step 1: Fetch main.js to extract dp_AUTH_TOKEN
JS_URL="https://cdn.thevillages.com/web_components/myvillages-auth-forms/main.js"
JS_RESPONSE=$(curl -s "$JS_URL")
if [ $? -ne 0 ]; then
    echo "Failed to fetch main.js"
    exit 1
fi

# Step 2: Extract the token using grep and sed (matches dp_AUTH_TOKEN="Basic <base64_token>")
TOKEN_LINE=$(echo "$JS_RESPONSE" | grep -o 'dp_AUTH_TOKEN\s*=\s*["'\'']Basic\s\+[a-zA-Z0-9+/=]\+["'\'']')
if [ -z "$TOKEN_LINE" ]; then
    echo "Could not find dp_AUTH_TOKEN in main.js"
    exit 1
fi

# Extract the Base64 part and reconstruct as "Basic <base64>"
EXTRACTED_TOKEN=$(echo "$TOKEN_LINE" | sed -E 's/.*Basic\s+([a-zA-Z0-9+/=]+).*/Basic \1/')

# Step 3: Create a cookie jar file for session cookies
COOKIE_JAR="cookies.txt"

# Step 4: Visit the calendar page to capture cookies
CALENDAR_URL="https://www.thevillages.com/calendar/#/?dateRange=today&categories=entertainment&locationCategories=town-squares"
curl -s -c "$COOKIE_JAR" \
  -H "User-Agent: Mozilla/5.0" \
  -H "Accept: */*" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Origin: https://www.thevillages.com" \
  -H "Referer: https://www.thevillages.com/calendar/" \
  "$CALENDAR_URL" > /dev/null

# Step 5: Make the API request with the extracted token and cookies
API_URL="https://api.v2.thevillages.com/events/?cancelled=false&startRow=0&endRow=24&dateRange=today&categories=entertainment&locationCategories=town-squares&subcategoriesQueryType=and"
API_RESPONSE=$(curl -s -b "$COOKIE_JAR" \
  -H "Authorization: $EXTRACTED_TOKEN" \
  -H "User-Agent: Mozilla/5.0" \
  -H "Accept: */*" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate, br, zstd" \
  -H "Origin: https://www.thevillages.com" \
  -H "Content-Type: application/json" \
  -H "Referer: https://www.thevillages.com/calendar/" \
  -H "Connection: keep-alive" \
  -H "Pragma: no-cache" \
  -H "Cache-Control: no-cache" \
  "$API_URL")

# Step 6: Check if API response is valid JSON and process with jq
echo "$API_RESPONSE" | jq -e . > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Failed: Invalid JSON response or API error - $API_RESPONSE"
    rm "$COOKIE_JAR"
    exit 1
fi

# Step 7: Extract events and abbreviate venue names
OUTPUT=""
while IFS= read -r line; do
    if [ -n "$line" ]; then
        # Split venue and artist
        venue=$(echo "$line" | cut -d',' -f1)
        artist=$(echo "$line" | cut -d',' -f2-)
        
        # Abbreviate venue name
        abbreviated_venue=$(abbreviate_venue "$venue")
        
        # Build output string
        if [ -z "$OUTPUT" ]; then
            OUTPUT="${abbreviated_venue},${artist}"
        else
            OUTPUT="${OUTPUT}#${abbreviated_venue},${artist}"
        fi
    fi
done < <(echo "$API_RESPONSE" | jq -r '.events[] | .location.title + "," + .title' | tr -d '\"'\')

# Add final # and output
echo "${OUTPUT}#"

# Clean up cookie jar
rm "$COOKIE_JAR"