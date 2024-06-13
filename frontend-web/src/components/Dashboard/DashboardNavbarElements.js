//frontend-web/src/components/Dashboard/DashboardNavbarElements.js

import styled from 'styled-components';
import { NavLink as Link } from 'react-router-dom';

export const DashboardNav = styled.nav`
  background: #000; /* Set background color for sidebar */
  width: ${({ isOpen }) => (isOpen ? '200px' : '0')}; /* Adjust width based on isOpen state */
  height: 100vh; /* Full viewport height */
  position: fixed; /* Fixed position */
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column; /* Arrange items vertically */
  padding-top: 60px; /* Space for logo */
  z-index: 10;
  transition: width 0.3s ease-in-out; /* Smooth transition for collapsing */
  overflow-x: hidden; /* Hide overflow when collapsed */

  @media screen and (min-width: 768px) {
    width: 13vw; /* Fixed width for larger screens */
  }
`;

export const SidebarToggleButton = styled.button`
  background: #000;
  color: #fff;
  border: none;
  padding-right: 10px;
  cursor: pointer;
  position: fixed;
  top: 24px;
  left: 0;
  z-index: 10;


  @media screen and (min-width: 768px) {
    display: none; /* Hide toggle button on larger screens */
  }
`;

export const DashboardNavbarContainer = styled.div`
  display: flex;
  flex-direction: column; /* Arrange items vertically */
  align-items: flex-start;
  padding: 10px;
`;

export const DashboardNavMenu = styled.ul`
  display: flex;
  flex-direction: column; /* Arrange items vertically */
  list-style: none;
  width: 100%;
  padding: 0;
`;

export const DashboardNavItem = styled.li`
  width: 100%;
`;

export const DashboardNavLinks = styled(Link)`
  color: #fff;
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 16px;
  width: 100%;
  cursor: pointer;
  transition: color 0.2s ease-in-out;

  &:hover {
    background-color: #333;
  }

  &.active {
    background-color: #555;
  }
`;

export const DashboardNavBtn = styled.nav`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 16px;
`;

export const DashboardNavBtnLink = styled(Link)`
  border-radius: 50px;
  background: #fff;
  padding: 10px 20px;
  color: #000;
  font-size: 1.1rem;
  outline: none;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  text-decoration: none;
  margin: 10px 0;

  &:hover {
    background: #000;
    color: #fff;
  }
`;
