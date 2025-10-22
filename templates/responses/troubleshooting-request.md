# Troubleshooting Request Template

Hi [USER_NAME],

Thank you for providing those details about the issue you're experiencing with [PLUGIN_NAME].

To help diagnose this issue more effectively, I'll need some additional information:

## System Information
Please provide the following details (you can find most of these in WordPress Admin > Tools > Site Health):

- [ ] WordPress version
- [ ] [PLUGIN_NAME] version
- [ ] PHP version
- [ ] Active theme name and version
- [ ] Other active plugins (especially [RELEVANT_PLUGIN_TYPES])

## Issue-Specific Information
[CUSTOMIZE BASED ON ISSUE - EXAMPLES BELOW:]

For debugging purposes:
- [ ] Are there any error messages? If so, please copy the exact error text
- [ ] When did this issue first occur?
- [ ] Did anything change on your site recently? (WordPress update, new plugins, etc.)
- [ ] Does the issue occur for all users or specific user roles?

[IF APPLICABLE:]
## Debug Information
Could you please enable WordPress debug mode and check for any related errors?

1. Add these lines to your `wp-config.php` file:
   ```php
   define('WP_DEBUG', true);
   define('WP_DEBUG_LOG', true);
   define('WP_DEBUG_DISPLAY', false);
   ```
2. Try to reproduce the issue
3. Check the debug log file at `/wp-content/debug.log`
4. Share any relevant error messages (you can copy/paste or screenshot)

This information will help me identify the root cause and provide you with an accurate solution.

Looking forward to your response!

Best regards,
[YOUR_NAME]
VeronaLabs Support Team
