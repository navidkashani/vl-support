---
description: Import and analyze a ticket from FreeScout
---

# Import FreeScout Ticket

Import a support ticket from your FreeScout system for analysis and response.

## Input

Paste the ticket content from FreeScout below (you can copy the full ticket including headers):

```
[PASTE TICKET CONTENT HERE]
```

## What I'll Do

1. **Extract Key Information**:
   - Ticket ID
   - User name and email
   - Subject line
   - Full message content
   - Any system information mentioned
   - Previous conversation history (if included)

2. **Automatic Analysis**:
   - Identify plugin (WP SMS or WP Statistics)
   - Categorize issue type (Bug, Question, Setup, Feature Request)
   - Determine priority level
   - Extract WordPress/PHP version info if mentioned
   - Identify any error messages

3. **Search Knowledge Base**:
   - Look for similar previously solved issues
   - Find relevant documentation

4. **Generate Response**:
   - Draft a complete response ready to paste back into FreeScout
   - Include step-by-step instructions if needed
   - Reference relevant documentation links
   - Suggest follow-up questions if more info needed

## Output Format

### Ticket Analysis
- **Ticket ID**: [ID]
- **Plugin**: WP SMS / WP Statistics
- **Category**: Bug / Question / Setup / Feature Request / Compatibility
- **Priority**: Critical / High / Medium / Low
- **Summary**: [One-line description]

### User Environment
- WordPress: [version if mentioned]
- Plugin: [version if mentioned]
- PHP: [version if mentioned]
- Other relevant info: [if any]

### Similar Issues
[Links to relevant KB articles if found]

### Suggested Response
[Ready-to-use response text for FreeScout]

---

**Quick tip**: You can also use `/analyze-ticket` first for just analysis, or `/draft-response` for just response generation.
