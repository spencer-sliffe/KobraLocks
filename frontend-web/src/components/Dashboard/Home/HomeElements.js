// frontend-web/src/components/Dashboard/Home/HomeElements.js

import styled from 'styled-components';
import { NavLink as Link } from 'react-router-dom';

export const LeagueNav = styled.nav`
  background: #000;
  height: 30px;
  display: flex;
  justify-content: flex-end; /* Align items to the right */
  align-items: center;
  font-size: 1rem;
  position: sticky;
  top: 0;
  z-index: 9;
`;

export const LeagueNavContainer = styled.div`
  display: flex;
  justify-content: flex-end; /* Align items to the right */
  height: 30px;
  z-index: 1;
  width: 100%;
  max-width: 1350px;
  padding: 20px;
`;

export const LeagueNavMenu = styled.ul`
  display: flex;
  align-items: center;
  list-style: none;
  text-align: center;
`;

export const LeagueNavItem = styled.li`
  height: 25px;
`;

export const LeagueNavLinks = styled(Link)`
  color: #fff;
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 0 20px;
  height: 100%;
  cursor: pointer;
  transition: color 0.2s ease-in-out;

  &:hover {
    color: #d3d3d3;
  }

  &.active {
    border-bottom: 2px solid #fff;
  }

  /* Ensure no bottom border for inactive links */
  &:not(.active) {
    border-bottom: none;
  }
`;

