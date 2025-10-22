# Setup Guide Template

Hi [USER_NAME],

Thank you for choosing [PLUGIN_NAME]!

I'd be happy to help you get [PLUGIN_NAME] set up correctly. Here's a step-by-step guide:

## [FOR WP SMS]

### 1. Install and Activate
- Install WP SMS from WordPress.org or upload the plugin manually
- Activate the plugin from WordPress Admin > Plugins

### 2. Choose Your SMS Gateway
1. Go to **WP SMS > Settings > Gateway**
2. Select your preferred SMS gateway from the dropdown
3. Popular gateways include: [LIST RELEVANT ONES]

### 3. Configure Gateway Credentials
1. Enter your API Key / Username / Password (depending on gateway)
2. You can get these credentials from your gateway provider's dashboard
3. Test the connection using the "Send Test SMS" feature

### 4. Configure Notifications (Optional)
1. Go to **WP SMS > Settings > Notifications**
2. Choose which events should trigger SMS notifications:
   - New user registration
   - New post published
   - New comments
   - WooCommerce orders (if applicable)
3. Select who should receive notifications

### 5. Test Your Setup
1. Send a test SMS to your own number
2. Verify the message is received
3. If successful, your setup is complete!

## [FOR WP STATISTICS]

### 1. Install and Activate
- Install WP Statistics from WordPress.org or upload manually
- Activate the plugin

### 2. Initial Configuration
1. Go to **Settings > WP Statistics > Settings**
2. Choose tracking method:
   - **JavaScript Tracking** (recommended for cached sites)
   - **PHP Tracking** (more accurate but incompatible with page caching)

### 3. Privacy Settings (Important for GDPR)
1. Go to **Settings > WP Statistics > Privacy**
2. Configure:
   - IP address anonymization
   - Data retention period
   - Cookie consent (if needed)

### 4. GeoIP Database (Optional but Recommended)
1. Go to **Settings > WP Statistics > Settings > GeoIP**
2. Download and install the GeoIP database
3. This enables location-based statistics

### 5. Check Dashboard
1. Visit **WP Statistics > Overview**
2. You should start seeing statistics within minutes
3. Note: Initial data may be limited; statistics accumulate over time

## Need More Help?

If you encounter any issues during setup:
- Check our detailed documentation: [PLUGIN_SPECIFIC_LINK]
- Refer to our troubleshooting guide: [KB_LINK]
- Reply to this ticket with specific questions

[IF THEY MENTIONED SPECIFIC SETUP SCENARIO:]
Regarding your specific situation with [THEIR_SCENARIO], here's what I recommend:
[SPECIFIC_ADVICE]

Feel free to reach out if you need any clarification on these steps!

Best regards,
[YOUR_NAME]
VeronaLabs Support Team
