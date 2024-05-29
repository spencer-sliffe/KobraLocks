// SignUp.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const SignUp = () => {
    const [userData, setUserData] = useState({
        username: '',
        email: '',
        password: ''
    });

    const navigate = useNavigate();

    const handleChange = (e) => {
        setUserData({ ...userData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('/api/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData),
            });
            if (response.ok) {
                const result = await response.json();
                console.log('Sign Up Successful:', result);
                navigate('/signin');
            } else {
                console.log('Sign Up Failed:', response);
            }
        } catch (error) {
            console.error('Error during sign up:', error);
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
            <p>Already have an account? <a href="/sign-in">Sign In</a></p>
        </div>
    );
};

export default SignUp;