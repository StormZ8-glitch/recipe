import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';

const NavBar: React.FC = () => {
    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <Link to="/">Money Manager</Link>
            </div>
            <ul className="navbar-links">
                <li>
                    <Link to="/dashboard">Dashboard</Link>
                </li>
                <li>
                    <Link to="/transactions">Transactions</Link>
                </li>
                <li>
                    <Link to="/add-transaction">Add Transaction</Link>
                </li>
                <li>
                    <Link to="/savings-goals">Savings Goals</Link>
                </li>
            </ul>
        </nav>
    );
};

export default NavBar;