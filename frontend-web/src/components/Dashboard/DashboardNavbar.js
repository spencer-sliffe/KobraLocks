// frontend-web/src/components/Dashboard/DashboardNavbar.js
import React, { useState } from 'react';
import {
  DashboardNav,
  DashboardNavbarContainer,
  DashboardNavMenu,
  DashboardNavItem,
  DashboardNavLinks,
  SidebarToggleButton, // Import the new styled component
} from './DashboardNavbarElements';

const DashboardNavbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <DashboardNav isOpen={isOpen}>
      <SidebarToggleButton onClick={toggleSidebar}>
        {isOpen ? 'Close' : 'Menu'}
      </SidebarToggleButton>
      <DashboardNavbarContainer>
        <DashboardNavMenu>
          <DashboardNavItem>
            <DashboardNavLinks to="/dashboard/home" onClick={toggleSidebar}>
              Home
            </DashboardNavLinks>
          </DashboardNavItem>
          <DashboardNavItem>
            <DashboardNavLinks to="/dashboard/slipcenter" onClick={toggleSidebar}>
              SlipCenter
            </DashboardNavLinks>
          </DashboardNavItem>
          <DashboardNavItem>
            <DashboardNavLinks to="/dashboard/myslips" onClick={toggleSidebar}>
              MySlips
            </DashboardNavLinks>
          </DashboardNavItem>
        </DashboardNavMenu>
      </DashboardNavbarContainer>
    </DashboardNav>
  );
};

export default DashboardNavbar;
