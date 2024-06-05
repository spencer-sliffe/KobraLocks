//frontend-web/src/components/VerifyResetCode.js

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { verifyResetCode } from '../api';

const VerifyResetCode = () => {
    const [email, setEmail] = useState('');
    const [code, setCode] = useState('');
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await verifyResetCode(email, code);
            navigate('/reset-password', { state: { email, code } });
        } catch (error) {
            setMessage('Invalid code. Please try again.');
        }
    };

    return (
        <div className="container">
            <h1>Verify Reset Code</h1>
            <form onSubmit={handleSubmit}>
                <input type="email" name="email" placeholder="Enter your email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                <input type="text" name="code" placeholder="Enter reset code" value={code} onChange={(e) => setCode(e.target.value)} required />
                <button type="submit">Verify Code</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default VerifyResetCode;
