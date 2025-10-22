# VeronaLabs Support Assistant

This Claude Code project is designed to streamline and accelerate support operations for VeronaLabs WordPress plugins (WP SMS, WP Statistics, and others).

## Overview

This project provides automated workflows, templates, and knowledge management tools to help the VeronaLabs support team efficiently handle customer inquiries, bug reports, feature requests, and general support tickets.

## ⚠️ CRITICAL SAFETY RULE

**NEVER SEND EMAILS TO CUSTOMERS DIRECTLY. ALWAYS CREATE NOTES.**

All FreeScout integrations and response generation commands will create notes for the support team to review, edit, and send manually. This ensures:
- Full control over customer communications
- Responses can be reviewed before sending
- No accidental or inappropriate messages reach customers
- Team can add personalization and context

## Available Slash Commands

### FreeScout Integration

- `/respond-to-conversation` - ⭐ **NEW!** Fetch conversation by URL/ID and get AI-generated response draft
- `/freescout-import` - Import and analyze a ticket from FreeScout, get instant analysis and suggested response
- `/learn-from-freescout` - Analyze 100+ real conversations to learn patterns and improve support

### Quick Actions

- `/quick-categorize` - Fast automatic categorization and priority assessment
- `/analyze-ticket` - Detailed ticket analysis with solution suggestions
- `/draft-response` - Generate a professional support response

### Issue & Bug Tracking

- `/create-bug-report` - Create a standardized bug report from user description
- `/github-issue` - Convert a ticket into a GitHub issue for WP SMS or WP Statistics
- `/troubleshoot` - Generate step-by-step troubleshooting guides
- `/compatibility-check` - Check compatibility information for WordPress/PHP versions or other plugins

### Knowledge Base

- `/kb-search` - Search the knowledge base for relevant articles and solutions
- `/kb-add` - Document a new solution in the knowledge base

### Plugin-Specific Helpers

- `/wpsms-help` - WP SMS documentation and common issues (wp-sms-pro.com)
- `/wpstats-help` - WP Statistics documentation and common issues (wp-statistics.com)

### Response Templates

- `/template-use` - Use pre-written templates for common scenarios

**Available Templates:**
- `first-response` - Initial ticket acknowledgment
- `setup-guide` - Complete setup instructions
- `troubleshooting-request` - Request debugging information
- `bug-confirmed` - Acknowledge confirmed bugs
- `feature-request-response` - Respond to feature requests
- `resolved-closing` - Close resolved tickets
- `escalation` - Escalate to development team
- `compatibility-issue` - Handle compatibility problems
- `documentation-link` - Point to relevant documentation
- `follow-up` - Follow up on pending tickets

## Project Structure

```
vl-support/
├── .claude/
│   ├── claude.md              # This file
│   └── commands/              # Slash command definitions
├── templates/
│   ├── responses/             # Pre-written response templates
│   └── issues/                # Issue report templates
├── knowledge-base/            # Documented solutions and guides
├── scripts/                   # Automation scripts
└── docs/                      # Plugin documentation references
```

## Getting Started

### Typical Workflow

1. **New Ticket from FreeScout**
   - Use `/freescout-import` to paste the ticket and get instant analysis + response
   - Or use `/quick-categorize` for fast triage

2. **Generate Response**
   - Response is suggested automatically from `/freescout-import`
   - Or use `/template-use` to select a specific template
   - Or use `/draft-response` for custom responses

3. **Handle Bugs**
   - Use `/create-bug-report` to standardize the report
   - Use `/github-issue` to create a GitHub issue
   - Use template `bug-confirmed` to respond to user

4. **Build Knowledge Base**
   - After resolving new issues, use `/kb-add` to document
   - Use `/kb-search` to find existing solutions

5. **Plugin-Specific Help**
   - Use `/wpsms-help` or `/wpstats-help` for quick reference to documentation

## Quick Start for FreeScout Users

The fastest way to handle a ticket:
```
1. Copy ticket from FreeScout
2. Type: /freescout-import
3. Paste ticket content
4. Get instant analysis + ready-to-use response
5. Copy response back to FreeScout
```

## Customization

Feel free to add new slash commands, templates, and knowledge base entries as your support needs evolve. Each command is defined in `.claude/commands/` and can be customized to match your workflow.
