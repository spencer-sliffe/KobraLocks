import React, { useState } from "react";
import { Nav, NavLink, NavMenu, Bars, StaticLink } from "./NavbarElements";

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
            <Nav>
                <StaticLink>kobracoding.tech</StaticLink>
                <Bars onClick={() => setIsOpen(!isOpen)} />
                <NavMenu isOpen={isOpen}> // Pass isOpen state to styled component
                    <NavLink to="/" activeStyle={{ color: "#32CD32" }}>
                        Home
                    </NavLink>
                    <NavLink to="/about" activeStyle={{ color: "#32CD32" }}>
                        About
                    </NavLink>
                    <NavLink to="/contact" activeStyle={{ color: "#32CD32" }}>
                        Contact Us
                    </NavLink>
                    <NavLink to="/sign-up" activeStyle={{ color: "#32CD32" }}>
                        Sign Up
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;
