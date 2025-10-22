# Quick Start Guide - VeronaLabs Support

## For Solo Support Team Member

This guide will get you up and running with the VeronaLabs support system in 5 minutes.

## The Fastest Way to Handle Tickets

### Step 1: Open This Project in Claude Code
You're already here if you're reading this!

### Step 2: Handle Your First Ticket

When you get a new ticket in FreeScout:

1. **Copy the ticket content** from FreeScout (just select and copy the user's message)

2. **Type:** `/freescout-import` in Claude Code

3. **Paste the ticket content** when prompted

4. **Get instant results:**
   - Automatic categorization (WP SMS vs WP Statistics)
   - Priority level (Critical/High/Medium/Low)
   - Suggested solution (if similar issue exists)
   - Ready-to-use professional response

5. **Copy the response** back to FreeScout and send!

### That's It!

The whole process takes less than 2 minutes per ticket.

---

## Other Useful Commands

### Quick Commands
- `/quick-categorize` - Just categorize without full response (faster)
- `/draft-response` - Generate custom response for specific scenario
- `/kb-search` - Search for solution in knowledge base

### When You Have a Bug
- `/create-bug-report` - Format the bug report properly
- `/github-issue` - Create GitHub issue for WP SMS or WP Statistics
- `/template-use bug-confirmed` - Send bug confirmation to user

### When You Need Documentation
- `/wpsms-help` - Quick access to WP SMS docs
- `/wpstats-help` - Quick access to WP Statistics docs

### Build Your Knowledge Base
After solving a new issue:
- `/kb-add` - Document the solution for future reference

---

## Response Templates Available

Use `/template-use [template-name]`:

- **first-response** - "Thanks for contacting us, I'm looking into this..."
- **setup-guide** - Complete setup walkthrough
- **troubleshooting-request** - "Can you provide more info..."
- **bug-confirmed** - "Yes, this is a bug, we're working on it..."
- **feature-request-response** - "Thanks for the suggestion..."
- **resolved-closing** - "Great! Issue is resolved..."
- **escalation** - "I've escalated this to developers..."
- **compatibility-issue** - "This is a compatibility issue with..."
- **documentation-link** - "Here's the documentation..."
- **follow-up** - "Following up on your ticket..."

---

## Tips for Efficiency

1. **Use `/freescout-import` for 90% of tickets** - It's the all-in-one command

2. **Build your knowledge base as you go** - Every time you solve something new, use `/kb-add`

3. **Customize templates** - Edit files in `templates/responses/` to match your style

4. **Keep GitHub in sync** - Use `/github-issue` for bugs and features to track them properly

5. **Reference docs quickly** - Use `/wpsms-help` and `/wpstats-help` instead of opening browser

---

## Common Scenarios

### Scenario 1: "SMS not sending"
```
1. /freescout-import [paste ticket]
2. Claude analyzes and suggests checking gateway config
3. Copy response to FreeScout
4. If resolved later: /kb-add to document
```

### Scenario 2: "Statistics not tracking"
```
1. /freescout-import [paste ticket]
2. Claude identifies caching conflict
3. Provides step-by-step solution
4. Copy to FreeScout
```

### Scenario 3: User reports a bug
```
1. /freescout-import [paste ticket]
2. /create-bug-report to standardize
3. /github-issue to create issue
4. /template-use bug-confirmed
5. Send response with GitHub link
```

### Scenario 4: Feature request
```
1. /freescout-import [paste ticket]
2. /template-use feature-request-response
3. Customize based on feasibility
4. Send to user
```

---

## Documentation Links

Quick reference:

- **WP SMS**: https://wp-sms-pro.com/documentation/
- **WP SMS GitHub**: https://github.com/veronalabs/wp-sms
- **WP Statistics**: https://wp-statistics.com/documentation/
- **WP Statistics GitHub**: https://github.com/wp-statistics/wp-statistics

---

## Need Help with This System?

- Check [.claude/claude.md](.claude/claude.md) for full documentation
- All commands are in [.claude/commands/](.claude/commands/)
- All templates are in [templates/responses/](templates/responses/)
- Knowledge base is in [knowledge-base/](knowledge-base/)

## Your First Day Checklist

- [ ] Handle first ticket with `/freescout-import`
- [ ] Try using a template with `/template-use`
- [ ] Search knowledge base with `/kb-search`
- [ ] Document a solution with `/kb-add`
- [ ] Create a GitHub issue with `/github-issue` (if you encounter a bug)

Welcome to faster, more efficient support! 🚀
