import React, { useState } from 'react';
import { FaArrowLeft, FaArrowRight } from 'react-icons/fa';
import smarttv from '../assets/smarttv.jpeg'; // Replace with actual image paths
import smartwatch from '../assets/smartwatch.jpeg';
import soundbar from '../assets/soundbar.jpeg';
import earbuds from '../assets/earbuds.png';
import smartphone from '../assets/smartphone.jpeg';

const Banner = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const data = [
    smarttv,
    smartwatch,
    soundbar,
    earbuds,
    smartphone,
  ];

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev === 0 ? data.length - 1 : prev - 1));
  };

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev === data.length - 1 ? 0 : prev + 1));
  };

  return (
    <div className= ' w-full h-auto overflow-x-hidden'>
      <div className='w-screen h-[650px] relative'>
        <div className='w-[400wv] h-full flex '>
          <img
            className='w-screen h-full object-cover'
            src={data[currentSlide]}
            alt={`banner-${currentSlide}`}
            loading='priority'
          />
        </div>
              </div>
      <div className='absolute w-fit left-0 right-0 mx-auto flex gap-8 bottom-44'>
          <div
            onClick={prevSlide}
            className=" w-12 h-10 border-[1px] border-gray-700 flex items-center 
            justify-center hover:cursor-pointer hover:bg-gray-700 hover:text-white active:bg-gray-900 duration-500">
            <FaArrowLeft />
          </div>
          <div
            onClick={nextSlide}
            className="w-12 h-10 border-[1px] border-gray-700 flex items-center justify-center hover:cursor-pointer
             hover:bg-gray-700 hover:text-white active:bg-gray-900 duration-500"
          >
            <FaArrowRight />
          </div>
        </div>

    </div>
  );
};

export default Banner;
