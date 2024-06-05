// frontend-web/src/components/ResetPassword.js

import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { resetPassword } from '../api';

const ResetPassword = () => {
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [message, setMessage] = useState('');
    const location = useLocation();
    const navigate = useNavigate();
    const { email, code } = location.state;

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (password === confirmPassword) {
            try {
                await resetPassword(email, code, password);
                setMessage('Password reset successful. Redirecting to sign in...');
                setTimeout(() => navigate('/sign-in'), 3000);
            } catch (error) {
                setMessage('An error occurred. Please try again.');
            }
        } else {
            setMessage('Passwords do not match.');
        }
    };

    return (
        <div className="container">
            <h1>Reset Password</h1>
            <form onSubmit={handleSubmit}>
                <input type="password" name="password" placeholder="Enter new password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                <input type="password" name="confirmPassword" placeholder="Confirm new password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required />
                <button type="submit">Reset Password</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default ResetPassword;

