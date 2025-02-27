import http from 'k6/http';
import { check, sleep } from 'k6';
import { randomIntBetween, randomString } from 'https://jslib.k6.io/k6-utils/1.2.0/index.js';

export let options = {
    stages: [
        { duration: '30s', target: 100 }, // Ramp up to 100 users over 30 seconds
        { duration: '20s', target: 1000 },   // Stay at 100 users for 1 minute
        { duration: '30s', target: 0 },   // Ramp down to 0 users over 30 seconds
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    },
};

export default function () {
    // Generate a random JSON payload
    const payload = JSON.stringify({
        messageId: randomString(10),
        content: `This is a random message: ${randomString(20)}`,
        timestamp: new Date().toISOString(),
        priority: randomIntBetween(1, 5),
    });

    const headers = { 'Content-Type': 'application/json' };

    // Send the POST request
    const res = http.post('http://127.0.0.1:5000/msg', payload, { headers: headers });

    // Check if the request was successful
    check(res, {
        'status is 200': (r) => r.status === 200,
    });

    // Sleep to achieve the desired rate of 100 requests per second
    sleep(0.01); // 100 requests per second = 0.01 seconds between requests
}