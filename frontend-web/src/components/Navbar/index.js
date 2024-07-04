// frontend-web/src/components/Navbar/index.js

import React, { useState } from 'react';
import { FaBars } from 'react-icons/fa';
import { useAuth } from '../../context/AuthContext';
import {
  Nav,
  NavbarContainer,
  NavLogo,
  MobileIcon,
  NavMenu,
  NavItem,
  NavLinks,
  NavBtn,
  NavBtnLink,
} from './NavbarElements';

const Navbar = () => {
  const { user } = useAuth();
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      <Nav>
        <NavbarContainer>
          <NavLogo to="/">KobraLocks</NavLogo>
          <MobileIcon onClick={toggle}>
            <FaBars />
          </MobileIcon>
          <NavMenu isOpen={isOpen}>
            {user ? (
              <>
                <NavItem>
                  <NavLinks to="/dashboard" onClick={toggle}>
                    Dashboard
                  </NavLinks>
                </NavItem>
                <NavItem>
                  <NavLinks to="/history" onClick={toggle}>
                    History
                  </NavLinks>
                </NavItem>
                <NavItem>
                  <NavLinks to="/contact" onClick={toggle}>
                    Contact
                  </NavLinks>
                </NavItem>
                <NavItem>
                  <NavLinks to="/account" onClick={toggle}>
                    Account
                  </NavLinks>
                </NavItem>
              </>
            ) : (
              <>
                <NavItem>
                  <NavLinks to="/" onClick={toggle}>
                    Home
                  </NavLinks>
                </NavItem>
                <NavItem>
                  <NavLinks to="/about" onClick={toggle}>
                    About
                  </NavLinks>
                </NavItem>
                <NavItem>
                  <NavLinks to="/contact" onClick={toggle}>
                    Contact
                  </NavLinks>
                </NavItem>
                <NavItem>
                  <NavLinks to="/sign-in" onClick={toggle}>
                    Sign In
                  </NavLinks>
                </NavItem>
              </>
            )}
          </NavMenu>
          {!user && (
            <NavBtn>
              <NavBtnLink to="/sign-up">Sign Up</NavBtnLink>
            </NavBtn>
          )}
        </NavbarContainer>
      </Nav>
    </>
  );
};

export default Navbar;
