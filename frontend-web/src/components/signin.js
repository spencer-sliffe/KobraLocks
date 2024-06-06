// frontend-web/src/components/signin.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext'; // Ensure the path is correct based on your project structure
import { signIn as apiSignIn } from '../api'; // Import the signIn function from api

const SignIn = () => {
    const [credentials, setCredentials] = useState({
        username: '',
        password: ''
    });
    const [error, setError] = useState('');
    const navigate = useNavigate();
    const { signIn } = useAuth(); // This uses the signIn function from your authentication context

    const handleChange = (e) => {
        setCredentials({ ...credentials, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await apiSignIn(credentials.username, credentials.password);
            signIn(response.username); // Update authentication state
            navigate('/tempdashboard'); // Navigate to another page upon successful login
        } catch (error) {
            setError(error.message || 'Invalid username or password');
        }
    };

    return (
        <div className="container">
            <h1>Sign In</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={credentials.username}
                    onChange={handleChange}
                    required
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={credentials.password}
                    onChange={handleChange}
                    required
                />
                <button type="submit">Sign In</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <p>Don't have an account? <a href="/sign-up">Sign Up</a></p>
            <p><a href="/forgot-password">Forgot Password?</a></p>
        </div>
    );
};

export default SignIn;