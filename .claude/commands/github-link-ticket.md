---
description: Link a GitHub issue to a FreeScout ticket response
---

# Link GitHub Issue to Ticket

Generate a response for FreeScout that includes a GitHub issue link.

## Input

**Plugin**: [WP SMS / WP Statistics]

**GitHub Issue URL**: [Paste the GitHub issue link]

**Context**: [Brief description - is this a bug report, feature request, or escalation?]

**User Name**: [User's name from ticket]

## Output

I'll generate a professional response that:

1. Thanks the user for reporting
2. Confirms the issue has been logged
3. Provides the GitHub issue link
4. Explains what happens next
5. Sets appropriate expectations
6. Offers any available workarounds

### For Bug Reports

```
Hi [USER_NAME],

Thank you for reporting this issue with [PLUGIN_NAME].

I've confirmed this is a bug and have created a detailed report for our development team:

🔗 GitHub Issue: [GITHUB_URL]

What happens next:
- Our developers will review and prioritize the bug
- You can track progress and updates on the GitHub issue above
- We'll notify you when a fix is released
- [IF WORKAROUND:] In the meantime, see the workaround below

[IF WORKAROUND AVAILABLE:]
Temporary workaround:
[STEPS]

We appreciate you taking the time to report this - it helps us improve [PLUGIN_NAME] for everyone!

Best regards,
[YOUR_NAME]
VeronaLabs Support Team
```

### For Feature Requests

```
Hi [USER_NAME],

Thank you for this excellent feature suggestion!

I've submitted your request to our product team for consideration:

🔗 GitHub Issue: [GITHUB_URL]

What happens next:
- Product team will review the request
- They'll evaluate feasibility and user benefit
- If approved, it will be added to the roadmap
- You can follow updates on the GitHub issue

[OPTIONAL:]
You can help by:
- Adding any additional use cases in the GitHub issue
- Sharing how this would improve your workflow
- Engaging in the discussion if others comment

We value user feedback like yours - it shapes the future of [PLUGIN_NAME]!

Best regards,
[YOUR_NAME]
VeronaLabs Support Team
```

### For Technical Escalations

```
Hi [USER_NAME],

I've escalated your issue to our technical team for in-depth investigation:

🔗 GitHub Issue: [GITHUB_URL]

The team will need to:
- [SPECIFIC INVESTIGATION STEPS]
- [ANY INFO STILL NEEDED]

This level of investigation typically takes [TIMEFRAME]. I'll keep this ticket updated with any progress, and you can also monitor the GitHub issue directly.

Thank you for your patience as we work to resolve this!

Best regards,
[YOUR_NAME]
VeronaLabs Support Team
```

---

**Quick Workflow:**
1. Create GitHub issue using `/github-issue`
2. Copy the GitHub URL
3. Use this command to generate the user response
4. Paste back into FreeScout
