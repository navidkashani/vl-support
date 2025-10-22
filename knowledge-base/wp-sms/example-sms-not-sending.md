# SMS Messages Not Sending - Troubleshooting Guide

**Category**: Bug Fix / Troubleshooting
**Plugin**: WP SMS
**Date Added**: 2025-10-22
**Last Updated**: 2025-10-22
**Keywords**: sms not sending, messages not delivered, gateway issues, api error

## Problem Description

Users report that SMS messages are not being sent from their WordPress site. The plugin appears to be configured correctly, but messages are not reaching recipients.

## Affected Versions

- Plugin version: All versions
- WordPress version: All versions
- PHP version: All supported versions

## Symptoms

- No SMS messages received by recipients
- No errors displayed in WordPress admin
- Messages may show as "sent" in logs but are not delivered
- Silent failure - no indication of problems

## Common Causes

1. **Incorrect Gateway Configuration**
   - Wrong API credentials
   - Invalid gateway URL
   - Incorrect gateway selection

2. **Insufficient Gateway Balance**
   - SMS gateway account has no credits
   - Payment issues with gateway provider

3. **Server/Network Issues**
   - Server cannot make outbound connections
   - Firewall blocking requests
   - SSL/TLS issues

4. **Gateway Service Issues**
   - Gateway API is down
   - Rate limiting
   - Account suspended

## Solution

### Step 1: Verify Gateway Configuration

1. Go to WordPress Admin > WP SMS > Settings
2. Navigate to the Gateway tab
3. Verify:
   - Correct gateway is selected
   - API credentials are entered correctly (no extra spaces)
   - Gateway URL is correct (if applicable)

### Step 2: Test Gateway Connection

1. Use the built-in test feature (if available)
2. Send a test SMS to your own number
3. Check for any error messages

### Step 3: Check Gateway Account

1. Log into your SMS gateway provider's dashboard
2. Verify:
   - Account has sufficient credits
   - Account is active (not suspended)
   - API access is enabled
   - Your server's IP is not blocked

### Step 4: Enable Debug Mode

1. Add to `wp-config.php`:
   ```php
   define('WP_DEBUG', true);
   define('WP_DEBUG_LOG', true);
   define('WP_DEBUG_DISPLAY', false);
   ```
2. Attempt to send a test SMS
3. Check `/wp-content/debug.log` for errors

### Step 5: Check Server Connectivity

1. Verify server can make outbound HTTPS requests
2. Check with hosting provider about:
   - Firewall restrictions
   - Outbound connection limits
   - Required ports (usually 443 for HTTPS)

### Step 6: Verify PHP Requirements

1. Check PHP version meets gateway requirements
2. Verify required PHP extensions are installed:
   - cURL
   - OpenSSL
   - JSON

## Prevention

- Regularly monitor gateway balance
- Set up low-balance alerts with your gateway provider
- Keep plugin updated to latest version
- Test after any server/hosting changes
- Maintain contact with gateway provider for service status

## Related Articles

- [Gateway Configuration Guide]
- [Supported SMS Gateways]
- [Troubleshooting API Connection Issues]

## Additional Resources

- WP SMS Documentation: [link]
- Common Gateway Error Codes: [link]
- WordPress Debug Guide: [link]
