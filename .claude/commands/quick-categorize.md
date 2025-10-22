---
description: Quick automatic categorization and priority assessment of a ticket
---

# Quick Categorization

Quickly categorize and prioritize a support ticket for efficient routing and response.

## Input

Paste the ticket content below:

```
[PASTE TICKET CONTENT]
```

## Automatic Analysis

I'll provide instant categorization:

### 1. Plugin Identification
- **Plugin**: WP SMS / WP Statistics / Both / Unknown
- **Confidence**: High / Medium / Low

### 2. Issue Category
- **Primary**: Bug / Question / Setup / Feature Request / Compatibility / Documentation / Other
- **Sub-category**: [Specific area like "Gateway", "Tracking", "Performance", etc.]

### 3. Priority Level

**CRITICAL** - Requires immediate attention:
- Site broken/down
- Security issue
- Data loss
- Critical functionality not working

**HIGH** - Needs prompt response:
- Major feature not working
- Significant user impact
- Error messages
- Recent regression

**MEDIUM** - Normal priority:
- Minor bugs
- Configuration questions
- Feature clarification
- Documentation requests

**LOW** - Can be scheduled:
- Feature requests
- Enhancement suggestions
- General questions
- Minor improvements

### 4. Response Strategy

Based on the categorization, I'll suggest:

**Immediate Actions:**
- [ ] Search knowledge base for similar issues
- [ ] Check if this is a known issue
- [ ] [Other specific actions]

**Recommended Response Template:**
[TEMPLATE_NAME]

**Estimated Resolution Time:**
- **Quick** (< 1 hour): [If applies]
- **Moderate** (1-4 hours): [If applies]
- **Complex** (4+ hours or requires escalation): [If applies]

**Additional Notes:**
[Any specific observations or recommendations]

### 5. Required Information Check

Does the ticket include:
- [ ] Plugin version
- [ ] WordPress version
- [ ] PHP version
- [ ] Error messages (if applicable)
- [ ] Steps to reproduce (if bug)
- [ ] Expected vs actual behavior

**Missing Information:**
[List what needs to be requested from user]

## Next Steps

1. Use suggested template or `/draft-response`
2. If missing info, use `/template-use troubleshooting-request`
3. If known issue, use `/kb-search` to find solution
4. If needs escalation, use `/github-issue` or `/escalate`

---

**Quick tip**: For detailed analysis with solution suggestions, use `/analyze-ticket` instead.
