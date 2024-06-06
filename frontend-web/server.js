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
/*const dbConfig = {
    connectionString: process.env.AZURE_SQL_CONNECTION_STRING, // Use the connection string from the application settings
    options: {
        encrypt: true, // for Azure SQL Database
        trustServerCertificate: false, // change to true for local dev / self-signed certs
    }
};*/
const dbConfig = {
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    server: process.env.DB_SERVER,
    database: process.env.DB_DATABASE,
    options: {
        encrypt: true, // for Azure SQL Database
        trustServerCertificate: true, // change to true for local dev / self-signed certs
    }
};
// Sign In Endpoint
app.post('/api/signin', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Authenticate user by checking credentials against the database
        let pool = await sql.connect(dbConfig);
        let result = await pool.request()
            .input('Username', sql.VarChar, username)
            .input('Password', sql.VarChar, password)
            .query('SELECT * FROM Users WHERE Username = @Username AND Password = @Password');

        if (result.recordset.length > 0) {
            // User found, authentication successful
            res.status(200).json({ message: 'Sign In Successful' });
        } else {
            // User not found or incorrect password
            res.status(401).json({ message: 'Invalid username or password' });
        }
    } catch (err) {
        // Internal server error
        console.error('Error during sign in:', err);
        res.status(500).send('An error occurred during sign in.');
    }
});


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