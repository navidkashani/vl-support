# Common SMS Gateway Configuration Issues

**Category**: Bug Fix / Troubleshooting
**Plugin**: WP SMS
**Date Added**: 2025-10-22
**Last Updated**: 2025-10-22
**Keywords**: gateway, configuration, api, authentication, connection, setup

## Problem Description

Users frequently encounter issues when configuring SMS gateways in WP SMS, including authentication errors, connection failures, and "Deactivated" status messages even when API credentials appear correct.

## Affected Versions

- Plugin version: All versions
- WordPress version: All versions
- PHP version: All supported versions

## Common Symptoms

- Gateway shows as "Deactivated!" even after entering credentials
- API authentication returns 200 OK but SMS fails to send
- "Cannot connect" error messages
- Gateway not appearing in dropdown list
- Test SMS fails with no clear error message

## Common Causes

### 1. Incorrect API Credentials Format
- Extra spaces before/after API key
- Wrong credential fields (mixing up API key, Secret key, Auth token)
- Copy-paste issues adding hidden characters

### 2. Server Configuration Issues
- Firewall blocking outbound connections
- SSL/TLS version incompatibility
- Server IP not whitelisted with gateway provider
- cURL not properly configured

### 3. Gateway-Specific Requirements
- Some gateways require specific PHP extensions
- Regional restrictions on gateway APIs
- Account not activated or verified with provider
- Insufficient balance or credits

### 4. WordPress/PHP Environment
- PHP cURL extension missing or disabled
- OpenSSL not up to date
- WordPress REST API blocked
- Conflicting plugins (security/firewall)

## Solutions by Gateway Type

### For Twilio

1. **Verify Credentials**:
   - Account SID (starts with AC...)
   - Auth Token (32 characters)
   - From Number (must be in E.164 format: +1234567890)

2. **Check Settings**:
   - Go to WP SMS > Settings > Gateway
   - Select "Twilio"
   - Enter Account SID in "Account SID" field
   - Enter Auth Token in "Auth Token" field
   - Enter your Twilio phone number with country code

3. **Test**:
   ```
   - Click "Send Test SMS"
   - Enter your mobile number
   - Check for success message
   ```

### For Nexmo/Vonage

1. **Credentials Needed**:
   - API Key
   - API Secret
   - From Name or Number

2. **Common Issue**: API Secret vs Signature Secret
   - Use API Secret, NOT Signature Secret
   - Find in Vonage Dashboard > Settings > API Settings

### For Generic REST API Gateways

1. **Endpoint URL**: Must include https://
2. **Request Method**: Usually POST
3. **Authentication**: Check if it's in headers or body
4. **Response Format**: JSON or XML

## Step-by-Step Troubleshooting

### Step 1: Verify API Credentials

1. Log into your SMS gateway provider dashboard
2. Generate NEW API credentials (don't reuse old ones)
3. Copy credentials carefully (use copy button if available)
4. Paste into WP SMS settings
5. **Important**: Remove any trailing spaces

### Step 2: Test Gateway Connection

1. Go to WP SMS > Settings > Gateway
2. After entering credentials, click "Send Test SMS"
3. Send to your own number first
4. Check gateway provider dashboard for delivery logs

### Step 3: Check Server Requirements

```php
// Check if cURL is enabled
<?php
if (function_exists('curl_version')) {
    $version = curl_version();
    echo 'cURL is enabled. Version: ' . $version['version'];
} else {
    echo 'cURL is NOT enabled';
}
?>
```

Run this in a test PHP file on your server.

### Step 4: Enable Debug Mode

1. Add to `wp-config.php`:
   ```php
   define('WP_DEBUG', true);
   define('WP_DEBUG_LOG', true);
   define('WP_DEBUG_DISPLAY', false);
   ```

2. Try sending test SMS again

3. Check `/wp-content/debug.log` for detailed errors

### Step 5: Check Firewall/Security

1. **Server Firewall**: Contact hosting provider to ensure outbound HTTPS (port 443) is allowed
2. **WordPress Security Plugins**: Temporarily disable to test
3. **Gateway IP Whitelisting**: Some providers require your server IP to be whitelisted

### Step 6: Verify Gateway Account Status

1. Log into gateway provider
2. Check:
   - Account is active (not suspended)
   - Sufficient credits/balance
   - API access is enabled
   - No rate limiting restrictions

## Gateway-Specific Troubleshooting

### Orange.com (Guinea) Gateway

**Issue**: Shows "Deactivated!" even with 200 OK response

**Solution**:
1. Verify OAuth token is not expired
2. Check if account has Guinea region enabled
3. Ensure phone numbers are in correct format for Guinea (+224...)
4. Contact Orange API support to verify API access permissions

### Brevo (formerly Sendinblue)

**Issue**: Cannot connect

**Solution**:
1. Use API v3 endpoint: `https://api.brevo.com/v3/transactionalSMS/sms`
2. Get API key from Brevo Dashboard > SMTP & API > API Keys
3. Sender must be a registered sender name in Brevo
4. Verify Brevo SMS service is activated on your account

### Telnyx

**Common Error**: API authentication fails

**Solution**:
1. Use API Key v2 (not v1)
2. Format: `KEY...` (starts with KEY)
3. Get from Telnyx Portal > Auth > API Keys
4. Ensure SMS is enabled on your Telnyx account
5. Verify messaging profile is active

## Quick Checks Checklist

Before contacting support, verify:

- [ ] API credentials are correct (no spaces, no typos)
- [ ] Gateway account has sufficient balance
- [ ] Account is active and not suspended
- [ ] Test SMS to your own number works
- [ ] Server can make outbound HTTPS connections
- [ ] PHP cURL extension is enabled
- [ ] No security plugins blocking requests
- [ ] WordPress DEBUG mode enabled to see errors
- [ ] Gateway provider dashboard shows the API call
- [ ] Correct phone number format (international format with country code)

## Prevention

- Always test configuration immediately after setup
- Keep API credentials secure (don't share publicly)
- Monitor gateway balance regularly
- Set up low-balance alerts with provider
- Document your working configuration
- Test after WP SMS plugin updates
- Keep PHP and WordPress updated

## Related Articles

- [SMS Messages Not Sending](example-sms-not-sending.md)
- [Supported SMS Gateways]
- [Troubleshooting API Connection Issues]
- [WooCommerce SMS Notifications Setup]

## Additional Resources

- WP SMS Documentation: https://wp-sms-pro.com/documentation/
- Gateway Configuration Guide: https://wp-sms-pro.com/documentation/gateways/
- GitHub Issues: https://github.com/veronalabs/wp-sms/issues
- Common Gateway Error Codes: [link to docs]
