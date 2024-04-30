import React, { createContext, useState, useContext } from 'react';

const AuthContext = createContext(null);

// Export useAuth for easy access to context
export const useAuth = () => useContext(AuthContext);

// Define and export AuthProvider
export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null); // null when not logged in

    const signIn = (username) => {
        setUser({ username });
    };

    const signOut = () => {
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, signIn, signOut }}>
            {children}
        </AuthContext.Provider>
    );
};
