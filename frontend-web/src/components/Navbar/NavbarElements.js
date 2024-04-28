import styled from "styled-components";
import { FaBars } from "react-icons/fa";
import { NavLink as Link } from "react-router-dom";

export const Nav = styled.nav`
    background: #121212;
    height: 65px;
    display: flex;
    justify-content: space-between;
    padding: 0.5rem calc((100vw - 1000px) / 2);
    align-items: center;
`;

export const NavLink = styled(Link)`
    color: #DA70D6; // Purple
    display: flex;
    align-items: center;
    text-decoration: none;
    padding: 0 1rem;
    height: 100%;
    cursor: pointer;
    transition: color 0.3s;
    font-family: 'Courier New', monospace;

    &:hover, &.active {
        color: #32CD32; // Lime green
    }
`;

export const Bars = styled(FaBars)`
    display: none;
    color: #32CD32; // lime
    @media screen and (max-width: 768px) {
        display: block;
        position: absolute;
        top: 0;
        right: 0;
        transform: translate(-100%, 50%);
        font-size: 1.8rem;
        cursor: pointer;
        font-family: 'Courier New', monospace;
    }
`;

export const NavMenu = styled.div`
    display: flex;
    align-items: center;
    margin-right: -24px; // Ensure links are pushed to the right

    @media screen and (max-width: 768px) {
        display: flex;
        flex-direction: column;
        width: 100%; // Full width for dropdown
        height: auto;
        position: absolute;
        top: 65px; // Start below the navbar
        left: 0;
        background: #121212; // Match navbar background
        font-family: 'Courier New', monospace;
        transition: max-height 0.3s ease-in;
        max-height: ${({ isOpen }) => (isOpen ? "300px" : "0")}; // Animate open/close
        overflow: hidden;
    }
`;

export const StaticLink = styled.div`
    padding: 10px;
    color: #32CD32; //lime
    font-family: 'Courier New', monospace;
    font-size: 1rem;
    cursor: pointer;
`;
