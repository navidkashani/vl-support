#!/usr/bin/env python3
"""
Fetch a single FreeScout conversation by ID or URL and display full details
"""

import json
import requests
import sys
import re
import os
from datetime import datetime

# Load environment variables
def load_env():
    env_vars = {}
    env_file = os.path.join(os.path.dirname(__file__), '..', '.env')

    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()

    return env_vars

def extract_conversation_id(input_str):
    """Extract conversation ID from URL or return the ID if it's just a number"""
    # If it's just a number, return it
    if input_str.isdigit():
        return input_str

    # Try to extract from URL
    patterns = [
        r'/conversation/(\d+)',
        r'/conversations/view/(\d+)',
        r'/manage/conversations/view/(\d+)',
        r'#(\d+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, input_str)
        if match:
            return match.group(1)

    return None

def fetch_conversation(api_url, api_key, conversation_id):
    """Fetch conversation details from FreeScout API"""
    headers = {
        'X-FreeScout-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    # Fetch conversation details
    url = f"{api_url}/conversations/{conversation_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Fetch threads (messages)
        threads_url = f"{api_url}/conversations/{conversation_id}/threads"
        threads_response = requests.get(threads_url, headers=headers)

        if threads_response.status_code == 200:
            threads_data = threads_response.json()
            data['threads'] = threads_data.get('_embedded', {}).get('threads', [])
        else:
            data['threads'] = []

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching conversation: {e}")
        return None

def format_conversation(data):
    """Format conversation data for display"""
    if not data:
        return "Error: Could not fetch conversation"

    output = []
    output.append("=" * 80)
    output.append("FREESCOUT CONVERSATION DETAILS")
    output.append("=" * 80)
    output.append("")

    # Basic info
    output.append(f"📋 Ticket ID: #{data.get('number', 'N/A')}")
    output.append(f"📧 Subject: {data.get('subject', 'N/A')}")
    output.append(f"📊 Status: {data.get('status', 'N/A').upper()}")
    output.append(f"📂 Folder: {data.get('folderId', 'N/A')}")
    output.append("")

    # Customer info
    customer = data.get('customer', {})
    output.append(f"👤 Customer: {customer.get('firstName', '')} {customer.get('lastName', '')}".strip() or "N/A")
    output.append(f"📧 Email: {customer.get('email', 'N/A')}")
    output.append("")

    # Assignee
    assignee = data.get('assignee', {})
    if assignee:
        output.append(f"👨‍💼 Assigned to: {assignee.get('firstName', '')} {assignee.get('lastName', '')}".strip())
    output.append("")

    # Dates
    output.append(f"📅 Created: {data.get('createdAt', 'N/A')}")
    output.append(f"📅 Updated: {data.get('updatedAt', 'N/A')}")
    if data.get('closedAt'):
        output.append(f"📅 Closed: {data.get('closedAt', 'N/A')}")
    output.append("")

    # Thread count
    output.append(f"💬 Messages: {data.get('threadsCount', 0)}")
    output.append("")

    output.append("=" * 80)
    output.append("CONVERSATION THREAD")
    output.append("=" * 80)
    output.append("")

    # Threads (messages) - check both locations
    threads = data.get('threads', [])
    if not threads and '_embedded' in data:
        threads = data.get('_embedded', {}).get('threads', [])

    if threads:
        for i, thread in enumerate(threads, 1):
            thread_type = thread.get('type', 'unknown')
            created_by = thread.get('createdBy', {})

            if thread_type == 'customer':
                icon = "👤 CUSTOMER"
            elif thread_type == 'message':
                icon = "💬 SUPPORT"
            else:
                icon = f"📝 {thread_type.upper()}"

            output.append(f"{icon} - {thread.get('createdAt', 'N/A')}")
            output.append("-" * 80)

            # Get message body
            body = thread.get('body', '')
            # Clean HTML if present
            body = re.sub(r'<[^>]+>', '', body)  # Simple HTML strip
            body = body.strip()

            output.append(body)
            output.append("")
    else:
        output.append("No messages found.")
        output.append("")

    output.append("=" * 80)

    return "\n".join(output)

def save_conversation_json(data, conversation_id):
    """Save raw conversation data as JSON"""
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'single-conversations')
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f'conversation_{conversation_id}.json')

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

    return output_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch-conversation.py <conversation_id_or_url>")
        print("")
        print("Examples:")
        print("  python fetch-conversation.py 9491")
        print("  python fetch-conversation.py https://helpdesk.veronalabs.com/conversation/9491")
        sys.exit(1)

    input_str = sys.argv[1]

    # Extract conversation ID
    conversation_id = extract_conversation_id(input_str)

    if not conversation_id:
        print(f"Error: Could not extract conversation ID from: {input_str}")
        sys.exit(1)

    # Load environment variables
    env = load_env()
    api_url = env.get('FREESCOUT_API_URL', 'https://helpdesk.veronalabs.com/api')
    api_key = env.get('FREESCOUT_API_KEY')

    if not api_key:
        print("Error: FREESCOUT_API_KEY not found in .env file")
        sys.exit(1)

    print(f"Fetching conversation #{conversation_id}...")
    print("")

    # Fetch conversation
    data = fetch_conversation(api_url, api_key, conversation_id)

    if data:
        # Display formatted conversation
        print(format_conversation(data))

        # Save JSON
        json_file = save_conversation_json(data, conversation_id)
        print("")
        print(f"✅ Full conversation data saved to: {json_file}")
    else:
        print("❌ Failed to fetch conversation")
        sys.exit(1)

if __name__ == '__main__':
    main()
