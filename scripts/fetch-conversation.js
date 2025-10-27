#!/usr/bin/env node
/**
 * Fetch a single FreeScout conversation by ID or URL
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

// Extract conversation ID from URL or number
function extractConversationId(input) {
    if (/^\d+$/.test(input)) {
        return input;
    }

    const patterns = [
        /\/conversation\/(\d+)/,
        /\/conversations\/view\/(\d+)/,
        /\/manage\/conversations\/view\/(\d+)/,
        /#(\d+)/
    ];

    for (const pattern of patterns) {
        const match = input.match(pattern);
        if (match) {
            return match[1];
        }
    }

    return null;
}

// Make HTTPS request
function httpsGet(url, headers) {
    return new Promise((resolve, reject) => {
        https.get(url, { headers }, (res) => {
            let data = '';

            res.on('data', chunk => {
                data += chunk;
            });

            res.on('end', () => {
                if (res.statusCode >= 200 && res.statusCode < 300) {
                    try {
                        resolve(JSON.parse(data));
                    } catch (e) {
                        reject(new Error('Failed to parse JSON response'));
                    }
                } else {
                    reject(new Error(`HTTP ${res.statusCode}: ${data}`));
                }
            });
        }).on('error', reject);
    });
}

// Fetch conversation from FreeScout API
async function fetchConversation(apiUrl, apiKey, conversationId) {
    const headers = {
        'X-FreeScout-API-Key': apiKey,
        'Content-Type': 'application/json'
    };

    try {
        // Fetch conversation details
        const url = `${apiUrl}/conversations/${conversationId}`;
        const data = await httpsGet(url, headers);

        // Fetch threads
        try {
            const threadsUrl = `${apiUrl}/conversations/${conversationId}/threads`;
            const threadsData = await httpsGet(threadsUrl, headers);

            if (threadsData._embedded && threadsData._embedded.threads) {
                data.threads = threadsData._embedded.threads;
            }
        } catch (e) {
            data.threads = [];
        }

        return data;
    } catch (error) {
        console.error('Error fetching conversation:', error.message);
        return null;
    }
}

// Save conversation to JSON file
function saveConversation(data, conversationId) {
    const outputDir = path.join(__dirname, '..', 'data', 'single-conversations');

    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    const outputFile = path.join(outputDir, `conversation_${conversationId}.json`);
    fs.writeFileSync(outputFile, JSON.stringify(data, null, 2));

    return outputFile;
}

// Main function
async function main() {
    const args = process.argv.slice(2);

    if (args.length === 0) {
        console.log('Usage: node fetch-conversation.js <conversation_id_or_url>');
        console.log('');
        console.log('Examples:');
        console.log('  node fetch-conversation.js 9505');
        console.log('  node fetch-conversation.js https://helpdesk.veronalabs.com/conversation/9505');
        process.exit(1);
    }

    const input = args[0];
    const conversationId = extractConversationId(input);

    if (!conversationId) {
        console.error(`Error: Could not extract conversation ID from: ${input}`);
        process.exit(1);
    }

    // Load environment
    const env = loadEnv();
    const apiUrl = env.FREESCOUT_API_URL || 'https://helpdesk.veronalabs.com/api';
    const apiKey = env.FREESCOUT_API_KEY;

    if (!apiKey) {
        console.error('Error: FREESCOUT_API_KEY not found in .env file');
        process.exit(1);
    }

    console.log(`Fetching conversation #${conversationId}...`);

    // Fetch and save
    const data = await fetchConversation(apiUrl, apiKey, conversationId);

    if (data) {
        const outputFile = saveConversation(data, conversationId);
        console.log(`Success! Conversation saved to: ${outputFile}`);
    } else {
        console.error('Failed to fetch conversation');
        process.exit(1);
    }
}

main();
