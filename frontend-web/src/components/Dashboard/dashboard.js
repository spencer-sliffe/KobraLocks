// frontend-web/src/components/Dashboard/Dashboard.js

import React from 'react';
import { Routes, Route } from 'react-router-dom';
import DashboardNavbar from './DashboardNavbar';
import Home from './Home';
import SlipCenter from './SlipCenter';
import MySlips from './MySlips';

const Dashboard = () => {
  return (
    <div>
      <DashboardNavbar />
      <Routes>
        <Route path="home" element={<Home />} />
        <Route path="slipcenter" element={<SlipCenter />} />
        <Route path="myslips" element={<MySlips />} />
      </Routes>
    </div>
  );
};

export default Dashboard;

