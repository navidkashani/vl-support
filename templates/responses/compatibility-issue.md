# Compatibility Issue Template

Hi [USER_NAME],

Thank you for reporting this issue with [PLUGIN_NAME].

Based on your description and the information you've provided, this appears to be a compatibility issue with [WORDPRESS_VERSION / PHP_VERSION / OTHER_PLUGIN / THEME / HOSTING_ENVIRONMENT].

## Compatibility Issue Identified

**Issue:** [DESCRIPTION_OF_COMPATIBILITY_PROBLEM]

**Affected Environment:**
- [PLUGIN_NAME] version: [VERSION]
- [CONFLICTING_COMPONENT]: [VERSION / NAME]

## Current Status

[CHOOSE APPROPRIATE SCENARIO:]

### [KNOWN INCOMPATIBILITY - HAS WORKAROUND]

This is a known compatibility issue. Here's how to resolve it:

**Solution:**
[STEP_BY_STEP_WORKAROUND]

**Why this happens:**
[BRIEF_TECHNICAL_EXPLANATION]

**Permanent fix:**
We're working with [OTHER_PLUGIN_DEVELOPER / addressing this in a future update]. Expected timeline: [TIMEFRAME]

### [VERSION REQUIREMENT NOT MET]

The issue you're experiencing is because your environment doesn't meet the minimum requirements for [PLUGIN_NAME].

**Current Environment:**
- WordPress: [THEIR_VERSION]
- PHP: [THEIR_VERSION]

**Requirements:**
- WordPress: [MINIMUM_VERSION] or higher (recommended: [RECOMMENDED_VERSION])
- PHP: [MINIMUM_VERSION] or higher (recommended: [RECOMMENDED_VERSION])

**Solution:**
Please update [COMPONENT] to at least version [VERSION]. Here's how:

[FOR WORDPRESS UPDATE:]
1. Backup your site first (always!)
2. Go to Dashboard > Updates
3. Click "Update Now" for WordPress
4. Test the site after updating

[FOR PHP UPDATE:]
1. Contact your hosting provider
2. Request PHP version upgrade to [RECOMMENDED_VERSION]
3. They can usually do this via cPanel or their control panel
4. Test your site thoroughly after the upgrade

**Important:** Always backup your site before major updates!

### [PLUGIN/THEME CONFLICT]

Your issue is caused by a conflict with [CONFLICTING_PLUGIN / THEME].

**What's happening:**
[EXPLANATION_OF_CONFLICT]

**Solutions:**

**Option 1: Configuration Change (Recommended)**
[IF_POSSIBLE_TO_CONFIGURE_AROUND_IT]

**Option 2: Alternative Plugin/Theme**
If you don't absolutely need [CONFLICTING_COMPONENT], consider using:
- [ALTERNATIVE_1]
- [ALTERNATIVE_2]

**Option 3: Report to Other Developer**
Since this conflict involves another plugin/theme, you may want to report it to:
- [OTHER_PLUGIN] support: [LINK]
- Perhaps they can add compatibility support

**Option 4: Wait for Fix**
We've logged this compatibility issue and will work on improving compatibility in a future update.

### [HOSTING ENVIRONMENT LIMITATION]

This issue is related to your hosting environment's configuration.

**What's needed:**
[SERVER_REQUIREMENT / CONFIGURATION_CHANGE]

**Solution:**
Contact your hosting provider and request:
[SPECIFIC_REQUIREMENTS]

Most hosting providers can easily make these changes. Here's a message you can send them:

```
Hello,

I'm using the [PLUGIN_NAME] WordPress plugin which requires:
- [REQUIREMENT_1]
- [REQUIREMENT_2]
- [REQUIREMENT_3]

Could you please enable/configure these on my account?

Thank you!
```

## Testing After Resolution

After applying the solution:
1. Clear all caches (WordPress, browser, CDN)
2. Test the specific functionality that was problematic
3. Monitor for any new issues
4. Let me know if it's resolved!

## Additional Help

If you need assistance with any of these steps, or if the solution doesn't work, please reply with:
- What solution you tried
- What happened when you tried it
- Any new error messages

I'm here to help you get this working!

Best regards,
[YOUR_NAME]
VeronaLabs Support Team
