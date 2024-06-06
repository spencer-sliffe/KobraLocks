//frontend-web/src/api.js

import axios from 'axios';

const API_URL = 'https://kobralocksbackend.azurewebsites.net/api'; // Ensure the correct API endpoint

// Make sure each function correctly sends and receives data from the backend API
export const signIn = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/signin/`, { username, password });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};


export const signUp = async (username, email, password) => {
    try {
        const response = await axios.post(`${API_URL}/signup/`, { username, email, password });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const forgotPassword = async (email) => {
    try {
        const response = await axios.post(`${API_URL}/forgot-password/`, { email });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const verifyResetCode = async (email, code) => {
    try {
        const response = await axios.post(`${API_URL}/verify-reset-code/`, { email, code });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const resetPassword = async (email, code, password) => {
    try {
        const response = await axios.post(`${API_URL}/reset-password/`, { email, code, password });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};
