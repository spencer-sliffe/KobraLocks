//frontend-web/src/components/Dashboard/DashboardNavbarElements.js

import styled from 'styled-components';
import { NavLink as Link } from 'react-router-dom';

export const DashboardNav = styled.nav`
  background: transparent;
  height: 35px; /* Reduced height */
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.1rem;
  position: sticky;
  top: 0;
  z-index: 9;
  @media screen and (max-width: 768px) {
    display: none
  }
`;

export const DashboardNavbarContainer = styled.div`
  display: flex;
  justify-content: flex-end; /* Align items to the right */
  height: 35px; /* Reduced height */
  z-index: 1;
  width: 100%;
  max-width: 1350px;
  padding: 20px;
  margin-right: 6%;

  @media screen and (max-width: 768px) {
    display: none
  }
`;


export const DashboardNavMenu = styled.ul`
  display: flex;
  align-items: center;
  list-style: none;
  text-align: center;

  @media screen and (max-width: 768px) {
    display: none
  }
`;

export const DashboardNavItem = styled.li`
  height: 35px; /* Reduced height */
  background: #000;
  @media screen and (max-width: 768px) {
    display: none
  }
`;

export const DashboardNavLinks = styled(Link)`
  color: #fff;
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 0 20px; /* Adjusted padding */
  height: 100%;
  cursor: pointer;
  transition: color 0.2s ease-in-out;

  &:hover {
    color: #d3d3d3;
  }

  &.active {
    border-bottom: 3px solid #fff;
  }

  @media screen and (max-width: 768px) {
    display: none
  }
`;

export const DashboardNavBtn = styled.nav`
  display: flex;
  align-items: center;

  @media screen and (max-width: 768px) {
    display: none;
  }
`;

export const DashboardNavBtnLink = styled(Link)`
  border-radius: 50px;
  background: #fff;
  white-space: nowrap;
  padding: 4px 8px; /* Adjusted padding */
  color: #000;
  font-size: 1.1rem; /* Unified font size */
  outline: none;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  text-decoration: none;
  margin-left: 24px;

  &:hover {
    transition: all 0.2s ease-in-out;
    background: #000;
    color: #fff;
  }
  @media screen and (max-width: 768px) {
  display: none
  }
`;
