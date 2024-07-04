//frontend-web/src/components/Navbar/NavbarElements.js

import styled from 'styled-components';
import { NavLink as Link } from 'react-router-dom';

export const Nav = styled.nav`
  background: #000;
  height: 30px; /* Reduced height */
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1rem; /* Slightly reduced font size */
  position: sticky;
  top: 0;
  z-index: 11;
`;

export const NavbarContainer = styled.div`
  display: flex;
  justify-content: space-between;
  height: 30px; /* Reduced height */
  z-index: 1;
  width: 100%;
  max-width: 1350px;
  padding: 20px;
`;

export const NavLogo = styled(Link)`
  color: #fff;
  justify-self: flex-start;
  cursor: pointer;
  font-size: 1rem; /* Unified font size */
  display: flex;
  align-items: center;
  font-weight: bold;
  text-decoration: none;
  padding: 0; /* Ensures no extra padding */
`;

export const MobileIcon = styled.div`
  display: none;

  @media screen and (max-width: 768px) {
    display: block;
    position: absolute;
    top: 60%;
    right: 0;
    transform: translate(-100%, -50%);
    font-size: 1rem;
    cursor: pointer;
    color: #fff;
  }
`;

export const NavMenu = styled.ul`
  display: flex;
  align-items: center;
  list-style: none;
  text-align: center;

  @media screen and (max-width: 768px) {
    display: ${({ isOpen }) => (isOpen ? 'flex' : 'none')};
    flex-direction: column;
    position: absolute;
    top: 30px; /* Adjusted top position */
    right: 0; /* Align to the right */
    background: transparent;
    padding: 0;
    width: 100%; /* Ensure it covers the full width of the viewport */
    box-sizing: border-box; /* Ensure padding is included in the width */
  }
`;

export const NavItem = styled.li`
  height: 25px; /* Reduced height */
`;

export const NavLinks = styled(Link)`
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
    border-bottom: 2px solid #fff;
  }
`;

export const NavBtn = styled.nav`
  display: flex;
  align-items: center;

  @media screen and (max-width: 768px) {
    display: none;
  }
`;

export const NavBtnLink = styled(Link)`
  border-radius: 50px;
  background: #fff;
  white-space: nowrap;
  padding: 4px 8px; /* Adjusted padding */
  color: #000;
  font-size: 1rem; /* Unified font size */
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
`;
