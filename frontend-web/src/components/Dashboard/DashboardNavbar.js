// frontend-web/src/components/Dashboard/DashboardNavbar.js

import React, { useState } from 'react';
import {
  DashboardNav,
  DashboardNavbarContainer,
  DashboardNavMenu,
  DashboardNavItem,
  DashboardNavLinks,

} from './DashboardNavbarElements';

const DashboardNavbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <DashboardNav>
      <DashboardNavbarContainer>
        <DashboardNavMenu isOpen={isOpen}>
          <DashboardNavItem>
            <DashboardNavLinks to="/dashboard/home" onClick={toggle}>
              Home
            </DashboardNavLinks>
          </DashboardNavItem>
          <DashboardNavItem>
            <DashboardNavLinks to="/dashboard/slipcenter" onClick={toggle}>
              SlipCenter
            </DashboardNavLinks>
          </DashboardNavItem>
          <DashboardNavItem>
            <DashboardNavLinks to="/dashboard/myslips" onClick={toggle}>
              MySlips
            </DashboardNavLinks>
          </DashboardNavItem>
        </DashboardNavMenu>
      </DashboardNavbarContainer>
    </DashboardNav>
  );
};

export default DashboardNavbar;
