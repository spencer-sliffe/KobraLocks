//frontend-web/src/components/account.js

import React from 'react';
import { useAuth } from '../context/AuthContext';
import { signOut } from '../api'; // Import the signOut function from api

const Account = () => {
    const { signOut: contextSignOut } = useAuth();

    const handleSignOut = () => {
        signOut();
        contextSignOut();
        window.location.href = '/'; // Redirect to home page
    };

    return (
        <div className="container">
            <h1>Account Page</h1>
            <button onClick={handleSignOut}>Sign Out</button>
        </div>
    );
};

export default Account;
