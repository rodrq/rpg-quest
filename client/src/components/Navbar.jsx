import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import HomeIconSvg from '../assets/rpg-quest.svg';
import Modal from './Modal';
import { useHistory } from 'react-router-dom';

const Navbar = () => {

  const history = useHistory();

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
    history.replace('/')
    setLogoutModalOpen(false);
  };

  const cancelLogout = () => {
    setLogoutModalOpen(false);
  };

  return (
    <nav className="bg-gray-800 p-4 text-white ">
      <div className="container mx-auto flex items-center justify-between">
        <div className="flex items-center font-bold text-lg py-1 pl-5">
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
        </div>
        <div className="flex items-center font-bold text-lg py-1 pl-5">
          {authenticated && (
            <div>
              <Link to="/play" className="pr-4">
                Play
              </Link>
              <Link to="/all_quests" className="pl-4">
                Quests
              </Link>
            </div>
          )}
          <Link to="/about" className="flex items-center  font-bold text-lg py-1 pl-5">
            About
          </Link>
        </div>
        <div>
          {authenticated ? (
            <div className="flex items-center text-lg py-1 pl-5">
              <div className="">
                Welcome 
              </div>
              <button onClick={handleLogout} className="flex items-center  font-bold text-lg py-1 pl-5">
                Log out
              </button>
            </div>
          ) : (
            <div className="flex items-center  font-bold text-lg py-1 px-5 ">
              <Link to="/register" >
                Create Character
              </Link>
              <Link to="/login" className="py-1 pl-5 text-yellow-500 hover:text-yellow-300">
                Log in
              </Link>
            </div>
          )}
        </div>
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
