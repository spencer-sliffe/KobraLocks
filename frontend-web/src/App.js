import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import Home from './pages';
import About from './pages/about';
import SignUp from './pages/signup';
import Contact from './pages/contact';
import Success from './pages/success';
import SignIn from './pages/signin';
import TempDashBoard from './pages/tempdashboard';
import './App.css';

function App() {
  return (
    <Router>
      <AuthProvider>
        <div className="video-background">
          <video autoPlay muted loop id="myVideo">
            <source src="/images/Music - 35889.mp4" type="video/mp4" />
          </video>
          <div className="green-overlay"></div>
          <div className="overlay">
            <Navbar />
            <div className="main-content">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/contact" element={<Contact />} />
                <Route path="/sign-up" element={<SignUp />} />
                <Route path="/sign-in" element={<SignIn />} />
                <Route path="/success" element={<Success />} />
                <Route path="/tempdashboard" element={<TempDashBoard />} />
              </Routes>
            </div>
          </div>
        </div>
      </AuthProvider>
    </Router>
  );
}

export default App;
