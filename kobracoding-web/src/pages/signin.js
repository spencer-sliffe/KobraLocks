import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext'; // Ensure the path is correct based on your project structure

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
            const response = await fetch('/api/signin', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(credentials),
            });
            //const data = await response.json(); // This line is useful if the server sends back any data
            if (response.ok) {
                signIn(credentials.username); // Update authentication state
                navigate('/tempdashboard'); // Navigate to another page upon successful login
            } else {
                setError('Invalid username or password');
            }
        } catch (error) {
            console.error('Error during sign in:', error);
            setError('An error occurred. Please try again later.');
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
        </div>
    );
};

export default SignIn;
