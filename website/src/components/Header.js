import React, { useState, useEffect } from 'react';
import { logo, cartImg } from '../assets/index';
import { useSelector } from 'react-redux';
import { FaTimes, FaBars } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import Login from '../pages/Login';

import { addUser, userInfo } from '../redux/bazarSlice';

const Header = () => {
  const productData = useSelector((state) => state.bazar.productData);

  const Links = [
    { name: "HOME", link: "/" },
    { name: "REPAIRS", link: "/" },
    { name: "SHOP", link: "/" },
    { name: "BLOG", link: "/" },
    { name: "LOGIN", link: "/Login" },
  ];

  const [open, setOpen] = useState(false);

  const toggleMenu = () => {
    setOpen(!open);
  };

  // State to store the cart count
  const [cartCount, setCartCount] = useState(0);

  useEffect(() => {
    // Simulate fetching the cart count from your API
    // Replace this with an actual API call to get the cart count
    setTimeout(() => {
      const mockCartCount = 5; // Replace with the actual cart count
      setCartCount(mockCartCount);
    }, 1000); // Simulate an API call delay
  }, []);

  return (
    <div className='w-full h-20 bg-white border-b-[1px] border-b-gray-800 font-titleFont sticky top-0 z-50'>
      <div className='md:flex bg-white py-2'>
        <div className='font-bold text-2xl cursor-pointer flex items-center font-[Poppins] text-gray-800'>
          <Link to='/'>
            <span className='text-3xl text-indigo-600 nr-1 pt-2'>
              <img src={logo} alt='Logo' className='w-50' />
            </span>
          </Link>
          <Link to='/Cart'>
            <div className='relative flex items-center ml-45 right-12 top-2'>
              <img className='w-15 sm:w-16 md:w-20' src={cartImg} alt='cart' />
              {/* Display the cart count */}
              <span className='absolute w-15 sm:w-16 md:w-12 top-3.5 left-2 
              text-xs sm:text-sm md:text-base flex items-center justify-center font-semibold'>
                {productData.length}
              </span>
            </div>
          </Link>
        </div>
        <div onClick={toggleMenu} className='text-3xl absolute right-6 top-6 cursor-pointer md:hidden'>
          {open ? <FaTimes /> : <FaBars />}
        </div>

        <ul className={`
          md:flex md:items-center md:pb-0 pb-12 md-static bg-white md:z-auto z-[-1] left-0 w-full
          md:w-auto md:pl-0 pl-9 transition-all duration-500 ease-in 
          ${open ? 'top-20 opacity-100' : 'top-[-490px] opacity-0 md:opacity-100'}
        `}>
          {Links.map((link) => (
            <li key={link.name} className='md:ml-8 text-xl md:my-0 my-7'>
              <a href={link.link} className="text-gray-800 hover:text-gray-400 duration-500">{link.name}</a>
            </li>
          ))}
          {userInfo && <p>{userInfo.name}</p>} {/* Check if UserInfo exists before rendering */}
        </ul>
      </div>
    </div>
  );
};

export default Header;
