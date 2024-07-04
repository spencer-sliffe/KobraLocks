// frontend-web/src/components/Dashboard/dashboard.js

import React from 'react';
import { Routes, Route } from 'react-router-dom';
import DashboardNavbar from './DashboardNavbar';
import Home from './Home/Home';
import SlipCenter from './SlipCenter';
import MySlips from './MySlips';
import './Dashboard.css'; // Import CSS for layout adjustments

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <DashboardNavbar />
      <div className="dashboard-main-content">
        <Routes>
          <Route path="home" element={<Home />} />
          <Route path="slipcenter" element={<SlipCenter />} />
          <Route path="myslips" element={<MySlips />} />
        </Routes>
      </div>
    </div>
  );
};

export default Dashboard;