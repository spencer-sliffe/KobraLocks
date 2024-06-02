// src/components/SignUp.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signUp as apiSignUp } from '../api'; // Import the signUp function from api

const SignUp = () => {
    const [userData, setUserData] = useState({
        username: '',
        email: '',
        password: ''
    });
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleChange = (e) => {
        setUserData({ ...userData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await apiSignUp(userData.username, userData.email, userData.password);
            console.log('Sign Up Successful:', response);
            navigate('/sign-in');
        } catch (error) {
            setError(error.message || 'Sign Up Failed');
        }
    };

    return (
        <div className="container">
            <h1>Sign Up</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" name="username" placeholder="Username" value={userData.username} onChange={handleChange} required />
                <input type="email" name="email" placeholder="Email" value={userData.email} onChange={handleChange} required />
                <input type="password" name="password" placeholder="Password" value={userData.password} onChange={handleChange} required />
                <button type="submit">Sign Up</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <p>Already have an account? <a href="/sign-in">Sign In</a></p>
        </div>
    );
};

export default SignUp;
