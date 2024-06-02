//api.js

import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Your Django backend URL

export const signIn = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/signin/`, {
            username,
            password
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const signUp = async (username, email, password) => {
    try {
        const response = await axios.post(`${API_URL}/signup/`, {
            username,
            email,
            password
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};
