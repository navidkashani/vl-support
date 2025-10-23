#!/usr/bin/env node
/**
 * Create a note in a FreeScout conversation
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// Load .env file
function loadEnv() {
    const envPath = path.join(__dirname, '..', '.env');
    const envVars = {};

    if (fs.existsSync(envPath)) {
        const content = fs.readFileSync(envPath, 'utf8');
        content.split('\n').forEach(line => {
            line = line.trim();
            if (line && !line.startsWith('#') && line.includes('=')) {
                const [key, ...valueParts] = line.split('=');
                envVars[key.trim()] = valueParts.join('=').trim();
            }
        });
    }

    return envVars;
}

// Make HTTPS POST request
function httpsPost(url, headers, body) {
    return new Promise((resolve, reject) => {
        const urlObj = new URL(url);

        const options = {
            hostname: urlObj.hostname,
            port: urlObj.port || 443,
            path: urlObj.pathname,
            method: 'POST',
            headers: {
                ...headers,
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(body)
            }
        };

        const req = https.request(options, (res) => {
            let data = '';

            res.on('data', chunk => {
                data += chunk;
            });

            res.on('end', () => {
                if (res.statusCode >= 200 && res.statusCode < 300) {
                    try {
                        resolve(JSON.parse(data));
                    } catch (e) {
                        resolve(data);
                    }
                } else {
                    reject(new Error(`HTTP ${res.statusCode}: ${data}`));
                }
            });
        });

        req.on('error', reject);
        req.write(body);
        req.end();
    });
}

// Create a note in FreeScout conversation
async function createNote(apiUrl, apiKey, conversationId, noteText, userId = 1) {
    const url = `${apiUrl}/conversations/${conversationId}/threads`;

    const headers = {
        'X-FreeScout-API-Key': apiKey
    };

    const payload = {
        type: 'note',
        text: noteText,
        user: userId,
        imported: false,
        status: 'active'
    };

    try {
        const response = await httpsPost(url, headers, JSON.stringify(payload));
        return response;
    } catch (error) {
        console.error('Error creating note:', error.message);
        return null;
    }
}

// Main function
async function main() {
    const args = process.argv.slice(2);

    if (args.length < 2) {
        console.log('Usage: node create-note.js <conversation_id> <note_text>');
        console.log('');
        console.log('Example:');
        console.log('  node create-note.js 9505 "This is a test note"');
        process.exit(1);
    }

    const conversationId = args[0];
    const noteText = args.slice(1).join(' ');

    // Load environment
    const env = loadEnv();
    const apiUrl = env.FREESCOUT_API_URL || 'https://helpdesk.veronalabs.com/api';
    const apiKey = env.FREESCOUT_API_KEY;

    if (!apiKey) {
        console.error('Error: FREESCOUT_API_KEY not found in .env file');
        process.exit(1);
    }

    console.log(`Creating note in conversation #${conversationId}...`);

    // Create note
    const result = await createNote(apiUrl, apiKey, conversationId, noteText);

    if (result) {
        console.log('Success! Note created.');
    } else {
        console.error('Failed to create note');
        process.exit(1);
    }
}

main();
