#!/bin/bash

# Fetch conversations from FreeScout API
# Usage: ./fetch-conversations.sh [number_of_conversations]

# Load environment variables
if [ -f ../.env ]; then
    export $(cat ../.env | grep -v '^#' | xargs)
fi

# Configuration
API_URL="${FREESCOUT_API_URL:-https://helpdesk.veronalabs.com/api}"
API_KEY="${FREESCOUT_API_KEY}"
MAILBOX_ID="${FREESCOUT_MAILBOX_ID:-1}"
NUM_CONVERSATIONS="${1:-100}"
OUTPUT_DIR="../data/conversations"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "Fetching conversations from FreeScout..."
echo "API URL: $API_URL"
echo "Mailbox ID: $MAILBOX_ID"
echo "Number of conversations: $NUM_CONVERSATIONS"
echo "---"

# Calculate number of pages (FreeScout API typically returns 50 per page)
PER_PAGE=50
TOTAL_PAGES=$(( ($NUM_CONVERSATIONS + $PER_PAGE - 1) / $PER_PAGE ))

# Fetch conversations
for page in $(seq 1 $TOTAL_PAGES); do
    echo "Fetching page $page of $TOTAL_PAGES..."

    curl -s -X GET \
        "${API_URL}/conversations?mailboxId=${MAILBOX_ID}&page=${page}&per_page=${PER_PAGE}" \
        -H "X-FreeScout-API-Key: ${API_KEY}" \
        -H "Content-Type: application/json" \
        > "${OUTPUT_DIR}/conversations_page_${page}.json"

    # Check if request was successful
    if [ $? -eq 0 ]; then
        echo "✓ Page $page fetched successfully"
    else
        echo "✗ Error fetching page $page"
    fi

    # Rate limiting - be nice to the API
    sleep 1
done

echo "---"
echo "Done! Conversations saved to: $OUTPUT_DIR"
echo ""
echo "Next steps:"
echo "1. Run: node scripts/analyze-conversations.js"
echo "2. Or use slash command: /analyze-freescout-data"
