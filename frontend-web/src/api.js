//frontend-web/src/api.js

import axios from 'axios';

const API_URL = 'http://localhost:8000/api';  // Ensure the correct API endpoint

const setAuthToken = (token) => {
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    localStorage.setItem('token', token);
  } else {
    delete axios.defaults.headers.common['Authorization'];
    localStorage.removeItem('token');
  }
};

export const signIn = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}/signin/`, { username, password });
    setAuthToken(response.data.access);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const signUp = async (username, email, password) => {
  try {
    const response = await axios.post(`${API_URL}/signup/`, { username, email, password });
    setAuthToken(response.data.access);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const signOut = () => {
  setAuthToken(null);
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

// New function to fetch games
export const fetchNCAABBGames = async () => {
  try {
    const response = await axios.get(`${API_URL}/ncaabbgames/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const fetchMLBGames = async () => {
  try {
    const response = await axios.get(`${API_URL}/mlbgames/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const fetchNFLGames = async () => {
  try {
    const response = await axios.get(`${API_URL}/nflgames/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const fetchNCAAFBGames = async () => {
  try {
    const response = await axios.get(`${API_URL}/ncaafbgames/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const fetchMLSGames = async () => {
  try {
    const response = await axios.get(`${API_URL}/mlsgames/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const fetchWNBAGames = async () => {
  try {
    const response = await axios.get(`${API_URL}/wnbagames/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const fetchNBAGames = async () => {
  try {
    const response = await axios.get(`${API_URL}/nbagames/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};