const express = require('express');
const axios = require('axios');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');
const qs = require('querystring');
const cors = require('cors'); // ✅ Add this
const bodyParser = require('body-parser'); //  ADD THIS

const app = express();

// ✅ Enable CORS
app.use(cors()); // ✅ Allow all origins by default
app.use(express.json());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true })); // 🔥 ADD THIS
// ----------- gRPC Setup -----------
const PROTO_PATH = path.resolve(__dirname, 'grpc/transaction.proto');
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
});
const transactionProto = grpc.loadPackageDefinition(packageDefinition).transaction;

const grpcClient = new transactionProto.TransactionService(
    'transaction-service:50051',
    grpc.credentials.createInsecure()
);

// ----------- Service URLs -----------
const USER_SERVICE_URL = 'http://user-service:8000';
const ANALYTICS_SERVICE_URL = 'http://analytics-service:8002';

// ----------- User Routes -----------

// Get all users
app.get('/api/users', async (req, res) => {
    try {
        const response = await axios.get(`${USER_SERVICE_URL}/users`);
        res.json(response.data);
    } catch (error) {
        console.error('❌ User fetch error:', error.message);
        res.status(500).send('Error fetching users');
    }
});

// Register user
app.post('/api/users/register', async (req, res) => {
    try {
        const response = await axios.post(`${USER_SERVICE_URL}/users/register`, req.body);
        res.status(200).json(response.data);
    } catch (error) {
        console.error('❌ User register error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json(error.response?.data || { message: 'Error registering user' });
    }
});

// Login user
app.post('/api/users/login', async (req, res) => {
    try {
        const response = await axios.post(
            `${USER_SERVICE_URL}/users/login`,
            qs.stringify(req.body),
            { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
        );
        res.status(200).json(response.data);
    } catch (error) {
        console.error('❌ User login error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json(error.response?.data || { message: 'Error logging in' });
    }
});

// Get profile (requires token in Authorization header)
app.get('/api/users/profile', async (req, res) => {
    try {
        const token = req.headers.authorization;
        const response = await axios.get(`${USER_SERVICE_URL}/users/profile`, {
            headers: { Authorization: token }
        });
        res.status(200).json(response.data);
    } catch (error) {
        console.error('❌ Profile fetch error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json(error.response?.data || { message: 'Error fetching profile' });
    }
});

// Delete user
app.delete('/api/users/delete', async (req, res) => {
    try {
        const token = req.headers.authorization;
        const response = await axios.delete(`${USER_SERVICE_URL}/users/delete`, {
            headers: { Authorization: token }
        });
        res.status(200).json(response.data);
    } catch (error) {
        console.error('❌ User delete error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json(error.response?.data || { message: 'Error deleting user' });
    }
});


// ----------- gRPC Transaction Routes -----------
app.get('/api/transactions', (req, res) => {
    grpcClient.GetTransactions({ user_id: req.query.user_id }, (err, response) => {
        if (err) {
            console.error('❌ gRPC GetTransactions error:', err.message);
            return res.status(500).send('Error fetching transactions');
        }
        res.json(response.transactions);
    });
});

app.post('/api/transactions', (req, res) => {
    grpcClient.AddTransaction(req.body, (err, response) => {
        if (err) {
            console.error('❌ gRPC AddTransaction error:', err.message);
            return res.status(500).json({ error: err.message });  // ❗ More informative
        }
        res.json({ status: response.status, message: response.message });
    });
});

app.put('/api/transactions/:id', (req, res) => {
    const txnId = parseInt(req.params.id);
    const { category, amount, type } = req.body;

    grpcClient.UpdateTransaction(
        { id: txnId, category, amount, type },
        (err, response) => {
            if (err) {
                console.error('❌ gRPC UpdateTransaction error:', err.message);
                return res.status(500).send('Error updating transaction');
            }
            res.json({ status: response.status, message: response.message });
        }
    );
});

app.delete('/api/transactions/:id', (req, res) => {
    const txnId = parseInt(req.params.id);

    grpcClient.DeleteTransaction({ id: txnId }, (err, response) => {
        if (err) {
            console.error('❌ gRPC DeleteTransaction error:', err.message);
            return res.status(500).send('Error deleting transaction');
        }
        res.json({ status: response.status, message: response.message });
    });
});


// ----------- Analytics Routes -----------
app.get('/api/analytics/summary', async (req, res) => {
    try {
        const response = await axios.get(`${ANALYTICS_SERVICE_URL}/analytics/summary`);
        res.json(response.data);
    } catch (error) {
        console.error('❌ Analytics fetch error:', error.message);
        res.status(500).send('Error fetching summary');
    }
});

// ----------- Start Server -----------
app.listen(3000, () => {
    console.log('✅ Web API Gateway running on port 3000');
});
