import React from "react";
import { Nav, NavLink, NavMenu, Bars, StaticLink } from "./NavbarElements";
import { useAuth } from '../../context/AuthContext';

const Navbar = () => {
    const { user } = useAuth();
    const [isOpen, setIsOpen] = React.useState(false);

    return (
        <Nav>
            <StaticLink>kobracoding.tech</StaticLink>
            <Bars onClick={() => setIsOpen(!isOpen)} />
            <NavMenu isOpen={isOpen}>
                <NavLink to="/" activeStyle={{ color: "#32CD32" }}>Home</NavLink>
                <NavLink to="/about" activeStyle={{ color: "#32CD32" }}>About</NavLink>
                <NavLink to="/contact" activeStyle={{ color: "#32CD32" }}>Contact Us</NavLink>
                {user ? (
                    <NavLink to="/account" activeStyle={{ color: "#32CD32" }}>
                        Account:{user.username}
                    </NavLink>
                ) : (
                    <NavLink to="/sign-in" activeStyle={{ color: "#32CD32" }}>Sign In</NavLink>
                )}
            </NavMenu>
        </Nav>
    );
};

export default Navbar;
