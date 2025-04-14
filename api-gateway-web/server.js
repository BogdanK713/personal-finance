const express = require('express');
const axios = require('axios');
const app = express();

// User Service routes
app.get('/api/users', async (req, res) => {
    try {
        const response = await axios.get('http://user-service/api/users');
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error fetching users');
    }
});

app.post('/api/users/register', async (req, res) => {
    try {
        const response = await axios.post('http://user-service/api/users/register', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error registering user');
    }
});

app.post('/api/users/login', async (req, res) => {
    try {
        const response = await axios.post('http://user-service/api/users/login', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error logging in user');
    }
});

// Transaction Service routes
app.get('/api/transactions', async (req, res) => {
    try {
        const response = await axios.get('http://transaction-service/api/transactions');
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error fetching transactions');
    }
});

// Analytics Service routes
app.get('/api/analytics/summary', async (req, res) => {
    try {
        const response = await axios.get('http://analytics-service/api/analytics/summary');
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error fetching summary');
    }
});

app.listen(3000, () => {
    console.log('Web API Gateway running on port 3000');
});
