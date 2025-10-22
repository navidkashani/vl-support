#!/usr/bin/env python3
"""
Analyze FreeScout conversations to learn support patterns
"""

import json
import re
from collections import Counter, defaultdict
from datetime import datetime
import os

def load_conversations():
    """Load all conversation data"""
    conversations = []
    data_dir = "../data/conversations"

    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            with open(os.path.join(data_dir, filename), 'r') as f:
                data = json.load(f)
                if '_embedded' in data and 'conversations' in data['_embedded']:
                    conversations.extend(data['_embedded']['conversations'])

    return conversations

def identify_plugin(text):
    """Identify which plugin the conversation is about"""
    text_lower = text.lower()

    # Check for WP SMS indicators
    wpsms_keywords = ['wp sms', 'wp-sms', 'wpsms', 'sms', 'gateway', 'twilio', 'nexmo',
                      'text message', 'notification', 'sending sms']

    # Check for WP Statistics indicators
    wpstats_keywords = ['wp statistics', 'wp-statistics', 'wpstatistics', 'statistics',
                        'visitor', 'tracking', 'analytics', 'page view', 'geoip']

    wpsms_score = sum(1 for kw in wpsms_keywords if kw in text_lower)
    wpstats_score = sum(1 for kw in wpstats_keywords if kw in text_lower)

    if wpsms_score > wpstats_score:
        return 'WP SMS'
    elif wpstats_score > wpsms_score:
        return 'WP Statistics'
    else:
        return 'Unknown'

def categorize_issue(subject, preview):
    """Categorize the type of issue"""
    text = (subject + ' ' + preview).lower()

    # Bug indicators
    if any(kw in text for kw in ['error', 'not working', 'broken', 'bug', 'issue', 'problem',
                                   'fail', 'doesn\'t work', 'not sending', 'not tracking']):
        return 'Bug/Issue'

    # Feature request indicators
    if any(kw in text for kw in ['feature', 'suggestion', 'add', 'could you', 'would like',
                                   'request', 'enhancement']):
        return 'Feature Request'

    # Setup/Configuration indicators
    if any(kw in text for kw in ['setup', 'install', 'configure', 'how to', 'guide',
                                   'documentation', 'tutorial']):
        return 'Setup/Config'

    # Question indicators
    if any(kw in text for kw in ['how', 'why', 'what', 'can i', 'is it possible', '?']):
        return 'Question'

    # Compatibility indicators
    if any(kw in text for kw in ['compatible', 'compatibility', 'conflict', 'php', 'wordpress version']):
        return 'Compatibility'

    return 'Other'

def extract_keywords(text):
    """Extract important keywords from text"""
    text_lower = text.lower()

    # Common issue keywords
    keywords = []

    # SMS issues
    if 'not sending' in text_lower or 'sms not' in text_lower:
        keywords.append('sms-not-sending')
    if 'gateway' in text_lower:
        keywords.append('gateway-issue')
    if 'notification' in text_lower:
        keywords.append('notification')

    # Statistics issues
    if 'not tracking' in text_lower or 'tracking not' in text_lower:
        keywords.append('tracking-not-working')
    if 'cache' in text_lower or 'caching' in text_lower:
        keywords.append('caching-conflict')
    if 'performance' in text_lower or 'slow' in text_lower:
        keywords.append('performance')
    if 'gdpr' in text_lower or 'privacy' in text_lower:
        keywords.append('gdpr-privacy')

    # General issues
    if 'error' in text_lower:
        keywords.append('error')
    if 'upgrade' in text_lower or 'update' in text_lower:
        keywords.append('update-upgrade')

    return keywords

def analyze_conversations(conversations):
    """Analyze all conversations and generate insights"""

    analysis = {
        'total': len(conversations),
        'by_plugin': Counter(),
        'by_category': Counter(),
        'by_status': Counter(),
        'keywords': Counter(),
        'issues': defaultdict(list),
        'recent_closed': [],
        'active': []
    }

    for conv in conversations:
        subject = conv.get('subject', '')
        preview = conv.get('preview', '')
        status = conv.get('status', '')

        # Identify plugin
        plugin = identify_plugin(subject + ' ' + preview)
        analysis['by_plugin'][plugin] += 1

        # Categorize issue
        category = categorize_issue(subject, preview)
        analysis['by_category'][category] += 1

        # Status
        analysis['by_status'][status] += 1

        # Extract keywords
        keywords = extract_keywords(subject + ' ' + preview)
        for kw in keywords:
            analysis['keywords'][kw] += 1

        # Store issue info
        issue_info = {
            'id': conv.get('number'),
            'subject': subject,
            'plugin': plugin,
            'category': category,
            'status': status,
            'preview': preview[:200]
        }

        if status == 'closed':
            analysis['recent_closed'].append(issue_info)
        elif status == 'active':
            analysis['active'].append(issue_info)

        # Group by plugin and category
        analysis['issues'][f"{plugin}_{category}"].append(issue_info)

    return analysis

def print_report(analysis):
    """Print a formatted analysis report"""

    print("=" * 80)
    print("FREESCOUT CONVERSATION ANALYSIS REPORT")
    print("=" * 80)
    print()

    print(f"📊 OVERVIEW")
    print(f"Total Conversations Analyzed: {analysis['total']}")
    print()

    print("📦 BY PLUGIN:")
    for plugin, count in analysis['by_plugin'].most_common():
        percentage = (count / analysis['total']) * 100
        print(f"  {plugin}: {count} ({percentage:.1f}%)")
    print()

    print("🏷️  BY CATEGORY:")
    for category, count in analysis['by_category'].most_common():
        percentage = (count / analysis['total']) * 100
        print(f"  {category}: {count} ({percentage:.1f}%)")
    print()

    print("📊 BY STATUS:")
    for status, count in analysis['by_status'].most_common():
        percentage = (count / analysis['total']) * 100
        print(f"  {status}: {count} ({percentage:.1f}%)")
    print()

    print("🔑 TOP KEYWORDS/ISSUES:")
    for keyword, count in analysis['keywords'].most_common(15):
        print(f"  {keyword}: {count} times")
    print()

    print("=" * 80)
    print("WP SMS - MOST COMMON ISSUES")
    print("=" * 80)

    wpsms_bugs = [i for i in analysis['issues']['WP SMS_Bug/Issue']][:10]
    if wpsms_bugs:
        for i, issue in enumerate(wpsms_bugs, 1):
            print(f"{i}. #{issue['id']}: {issue['subject']}")
    print()

    print("=" * 80)
    print("WP STATISTICS - MOST COMMON ISSUES")
    print("=" * 80)

    wpstats_bugs = [i for i in analysis['issues']['WP Statistics_Bug/Issue']][:10]
    if wpstats_bugs:
        for i, issue in enumerate(wpstats_bugs, 1):
            print(f"{i}. #{issue['id']}: {issue['subject']}")
    print()

    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print()
    print("📝 Knowledge Base Articles Needed:")

    # Suggest KB articles based on common keywords
    if analysis['keywords']['sms-not-sending'] > 3:
        print("  - 'SMS Messages Not Sending' (frequent issue)")
    if analysis['keywords']['tracking-not-working'] > 3:
        print("  - 'Statistics Not Tracking Visits' (frequent issue)")
    if analysis['keywords']['caching-conflict'] > 2:
        print("  - 'WP Statistics and Caching Plugins Compatibility'")
    if analysis['keywords']['gateway-issue'] > 2:
        print("  - 'Common SMS Gateway Configuration Issues'")
    if analysis['keywords']['gdpr-privacy'] > 2:
        print("  - 'GDPR Compliance Setup for WP Statistics'")

    print()
    print("🎯 Templates to Create:")

    feature_requests = len(analysis['issues']['WP SMS_Feature Request']) + \
                       len(analysis['issues']['WP Statistics_Feature Request'])
    if feature_requests > 5:
        print(f"  - Feature request template (you have {feature_requests} feature requests)")

    setup_questions = len(analysis['issues']['WP SMS_Setup/Config']) + \
                      len(analysis['issues']['WP Statistics_Setup/Config'])
    if setup_questions > 5:
        print(f"  - Setup guide template (you have {setup_questions} setup questions)")

    print()

def save_detailed_analysis(analysis):
    """Save detailed analysis to file"""
    output_file = "../data/analysis-report.json"

    with open(output_file, 'w') as f:
        # Convert Counter objects to dicts for JSON serialization
        serializable_analysis = {
            'total': analysis['total'],
            'by_plugin': dict(analysis['by_plugin']),
            'by_category': dict(analysis['by_category']),
            'by_status': dict(analysis['by_status']),
            'keywords': dict(analysis['keywords']),
            'recent_closed': analysis['recent_closed'][:20],
            'active': analysis['active']
        }
        json.dump(serializable_analysis, f, indent=2)

    print(f"✅ Detailed analysis saved to: {output_file}")

if __name__ == '__main__':
    print("Loading conversations from FreeScout...")
    conversations = load_conversations()

    if not conversations:
        print("❌ No conversations found. Please run fetch-conversations.sh first.")
        exit(1)

    print(f"✓ Loaded {len(conversations)} conversations")
    print()

    print("Analyzing conversations...")
    analysis = analyze_conversations(conversations)

    print_report(analysis)
    save_detailed_analysis(analysis)
