---
description: Create a GitHub issue from a bug report or feature request
---

# Create GitHub Issue

Convert a support ticket into a properly formatted GitHub issue for the plugin repository.

## Input

**Issue Type**: [Bug Report / Feature Request / Enhancement]

**Plugin Repository**:
- [ ] WP SMS (https://github.com/veronalabs/wp-sms)
- [ ] WP Statistics (https://github.com/wp-statistics/wp-statistics)

**Source**: [Ticket ID or reference if applicable]

**Issue Details**:
[Paste the ticket content or describe the issue]

## Output

I'll generate a properly formatted GitHub issue with:

### For Bug Reports

```markdown
## Description
[Clear description of the bug]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- Plugin Version: [version]
- WordPress Version: [version]
- PHP Version: [version]
- Browser (if relevant): [browser]
- Theme: [if relevant]
- Active Plugins: [if relevant]

## Error Messages / Logs
```
[Error messages if any]
```

## Screenshots
[If available]

## Additional Context
[Any other relevant information]

## Reported By
User via support ticket [ticket ID if applicable]
```

### For Feature Requests

```markdown
## Feature Description
[Clear description of the requested feature]

## Use Case
[Why this feature is needed - user's scenario]

## Proposed Solution
[Suggested implementation if any]

## Alternatives Considered
[Other ways to achieve the same goal]

## Additional Context
[Any other relevant information, mockups, examples from other plugins]

## User Impact
[How many users might benefit, how critical is it]

## Requested By
User via support ticket [ticket ID if applicable]
```

## Next Steps

After generating the issue:
1. Review and adjust as needed
2. Copy and create the issue on GitHub
3. Update the FreeScout ticket with the GitHub issue link
4. Use `/draft-response` to notify the user their issue has been logged
