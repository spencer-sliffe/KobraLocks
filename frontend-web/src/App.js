import React, { useState, useEffect } from 'react';
import './App.css';
import Navbar from "./components/Navbar";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./pages";
import About from './pages/About.js'; // or About.jsx if using JSX
import SignUp from "./pages/signup";
import Contact from "./pages/contact";

function App() {
  return (
      <Router>
          <Navbar />
          <Routes>
              <Route exact path="/" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route
                  path="/contact"
                  element={<Contact />}
              />
              <Route
                  path="/sign-up"
                  element={<SignUp />}
              />
          </Routes>
      </Router>
  );
}

export default App;


