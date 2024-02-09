// Navbar.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import HomeIconSvg from '../assets/rpg-quest.svg';
import Modal from './Modal';

const Navbar = () => {
  const { authenticated, logout } = useAuth();

  const [isLogoutModalOpen, setLogoutModalOpen] = useState(false);

  const handleLogout = () => {
    setLogoutModalOpen(true);
  };

  const confirmLogout = () => {
    document.cookie.split(';').forEach((cookie) => {
      const eqPos = cookie.indexOf('=');
      const name = eqPos > -1 ? cookie.substr(0, eqPos).trim() : cookie.trim();
      document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
    });
    logout();
    setLogoutModalOpen(false);
  };

  const cancelLogout = () => {
    setLogoutModalOpen(false);
  };

  return (
    <nav className="bg-gray-800 p-4 text-white ">
      <div className="container mx-auto flex items-center">
      <Link to="/" className="flex items-center font-bold text-lg py-1 pl-5">
          <img
            className="w-10 h-10 mr-2 "
            src={HomeIconSvg}
            alt="Home Icon"
          />
        </Link>
        <Link to="/" className="flex items-center  font-bold text-lg py-1 pl-5">
          Home
        </Link>
        {authenticated && (
          <div className="flex items-center font-bold text-lg py-1 pl-5">
            <Link to="/play" className="pr-4">
              Play
            </Link>
            <button onClick={handleLogout} className="pl-4">
              Log out
            </button>
          </div>
        )}


        {!authenticated && (
          <div className="flex items-center  font-bold text-lg py-1 px-5">
            <Link to="/register" >
              Create Character
            </Link>
            <Link to="/login" className="py-1 pl-5">
              Log in
            </Link>
          </div>
        )}
        
      </div>
      <Modal
        isOpen={isLogoutModalOpen}
        onClose={cancelLogout}
        onConfirm={confirmLogout}
        message="Are you sure you want to log out?"
      />
    </nav>
  );
};

export default Navbar;
