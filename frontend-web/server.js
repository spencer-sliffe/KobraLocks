const express = require('express');
const bodyParser = require('body-parser');
const path = require('path'); // Add this line to fix the error
require('dotenv').config();
const cors = require('cors');
const sql = require('mssql');
const app = express();


// Middleware
app.use(cors());
app.use(bodyParser.json());

// Serve static files from the React app
app.use(express.static(path.join(__dirname, 'build')));

// Azure SQL connection configuration
const dbConfig = {
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    server: process.env.DB_SERVER,
    database: process.env.DB_DATABASE,
    options: {
        encrypt: true, // for Azure SQL Database
        trustServerCertificate: false, // change to true for local dev / self-signed certs
    }
};

// Sign Up Endpoint
app.post('/api/signup', async (req, res) => {
    try {
        let pool = await sql.connect(dbConfig);
        let { username, email, password } = req.body;
        // Here you should encrypt the password before saving it to the database
        let result = await pool.request()
            .input('Username', sql.VarChar, username)
            .input('Email', sql.VarChar, email)
            .input('Password', sql.VarChar, password) // Hash password before storing
            .query('INSERT INTO Users (Username, Email, Password) VALUES (@Username, @Email, @Password);');
        res.json({ message: 'Sign Up Successful' });
    } catch (err) {
        res.status(500).send(err.message);
    }
});

// Handles any requests that don't match the ones above
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname+'/build/index.html'));
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});