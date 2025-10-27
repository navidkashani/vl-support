---
description: Fetch a FreeScout conversation by URL and generate a suggested response draft as a note
---

# Respond to FreeScout Conversation

Provide a FreeScout conversation URL and I'll fetch the full conversation, analyze it, generate a professional response draft in HTML format, and **create a note** in FreeScout for your team to review before sending.

## Usage

**Paste your FreeScout conversation URL:**

Example formats accepted:
- `https://helpdesk.veronalabs.com/conversation/9491`
- `https://helpdesk.veronalabs.com/manage/conversations/view/9491`
- Just the conversation ID: `9491`

## What I'll Do

1. **Fetch the Conversation**
   - Get full conversation details via FreeScout API
   - Load all message threads
   - Extract customer information
   - Get conversation history

2. **Analyze the Issue**
   - Identify plugin (WP SMS / WP Statistics)
   - Categorize issue type (Bug / Question / Feature / Setup)
   - Determine priority level
   - Extract key details (versions, errors, etc.)
   - Search knowledge base for similar issues

3. **Generate Response Draft (HTML Format)**
   - **IMPORTANT**: Read and follow `docs/customer-communication-guidelines.md` for ALL responses
   - Keep responses SHORT and CONCISE (avoid long lists and overwhelming details)
   - Use natural, conversational tone (warm, friendly, empathetic)
   - Match customer's energy and emotion level
   - Personalized with customer's first name only
   - Short paragraphs (2-3 sentences max)
   - Use lists ONLY when absolutely necessary (max 3-4 items)
   - Always end with "Best regards," (no name or team signature after)
   - **Formatted in HTML (not Markdown) for FreeScout compatibility**

4. **Create a Note in FreeScout**
   - **Automatically creates an internal note** in the conversation
   - Contains the suggested response draft
   - Support team can review before sending
   - Easy to copy and send when ready

5. **Provide Context**
   - Summary of the issue
   - Recommended actions
   - Relevant KB articles
   - Whether to escalate (if needed)
   - Suggested templates (if applicable)

## Output Format

### 📋 Conversation Summary
- **Ticket ID**: #9491
- **Customer**: John Doe (john@example.com)
- **Plugin**: WP SMS / WP Statistics
- **Subject**: [Subject line]
- **Category**: Bug / Question / Feature Request / Setup
- **Priority**: Critical / High / Medium / Low
- **Status**: Active / Pending / Closed

### 💬 Conversation Thread
[Summary of the conversation so far]

### 🔍 Analysis
- **Issue**: [One-line description]
- **Root Cause**: [If identifiable]
- **Similar Issues**: [Links to KB articles if found]
- **Recommended Action**: [Solve / Request Info / Escalate]

### ✍️ Suggested Response Draft (HTML)

[HTML formatted response ready to copy]

### 📝 Note Created in FreeScout
✅ **A note has been created** in conversation #9491 with the suggested response.
- Your support team can review it in FreeScout
- Copy and send when ready
- View it here: [Conversation Link]

### 📚 Additional Resources
- Relevant KB articles
- Documentation links
- GitHub issues (if applicable)

### 🎯 Next Steps
1. Review the note in FreeScout
2. Edit if needed
3. Send to customer when ready
4. Mark as resolved after confirmation

---

## Example Workflow

**Input**: `https://helpdesk.veronalabs.com/conversation/9491`

**I'll do**:
1. Fetch and analyze the conversation
2. Generate HTML response draft
3. **Create an internal note** in FreeScout with the draft
4. Show you the summary and analysis

**You do**:
1. Review the note in FreeScout
2. Edit if needed
3. Send to customer

---

**Paste your conversation URL below:**
