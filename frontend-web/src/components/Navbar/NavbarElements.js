import styled from 'styled-components';
import { NavLink as Link } from 'react-router-dom';
import { FaBars } from 'react-icons/fa';

export const Nav = styled.nav`
  background: transparent;
  height: 40px; /* Reduced height */
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1rem;
  position: sticky;
  top: 0;
  z-index: 10;
`;

export const NavbarContainer = styled.div`
  display: flex;
  justify-content: space-between;
  height: 40px; /* Reduced height */
  z-index: 1;
  width: 100%;
  max-width: 1100px;
  padding: 0 24px;
`;

export const NavLogo = styled(Link)`
  color: #fff;
  justify-self: flex-start;
  cursor: pointer;
  font-size: 1.2rem; /* Slightly smaller font size */
  display: flex;
  align-items: center;
  margin-left: 24px;
  font-weight: bold;
  text-decoration: none;
`;

export const MobileIcon = styled.div`
  display: none;

  @media screen and (max-width: 768px) {
    display: block;
    position: absolute;
    top: 50%;
    right: 0;
    transform: translate(-100%, -50%);
    font-size: 1.8rem;
    cursor: pointer;
    color: #fff;
  }
`;

export const NavMenu = styled.ul`
  display: flex;
  align-items: center;
  list-style: none;
  text-align: center;
  margin-right: -22px;

  @media screen and (max-width: 768px) {
    display: ${({ isOpen }) => (isOpen ? 'flex' : 'none')};
    flex-direction: column;
    position: absolute;
    top: 20px; /* Adjusted top position */
    right: 0; /* Align to the right */
    background: transparent;
    padding: 10px;
    width: 100%; /* Ensure it covers the full width of the viewport */
    box-sizing: border-box; /* Ensure padding is included in the width */
  }
`;

export const NavItem = styled.li`
  height: 40px; /* Reduced height */
`;

export const NavLinks = styled(Link)`
  color: #fff;
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 5px 20px; /* Adjusted padding */
  height: 100%;
  cursor: pointer;
  transition: color 0.2s ease-in-out;

  &:hover {
    color: #000;
  }

  &.active {
    border-bottom: 3px solid #000;
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
  padding: 8px 16px; /* Adjusted padding */
  color: #000;
  font-size: 14px; /* Slightly smaller font size */
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

