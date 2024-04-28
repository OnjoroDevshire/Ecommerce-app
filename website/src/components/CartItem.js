import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { BiTrash } from 'react-icons/bi';
import { decrementQuantity, deleteItem, incrementQuantity, resetCart } from '../redux/bazarSlice';
import { Link } from 'react-router-dom';
import { BiArrowToLeft } from 'react-icons/bi';
import { ToastContainer, toast } from 'react-toastify';

const CartItem = () => {
  const dispatch = useDispatch();
  const productData = useSelector((state) => state.bazar.productData);
  const [totalAmt, setTotalAmt] = useState("");

  useEffect(()=>{
    let price = 0;
    productData.map((item)=>{
      price += item.price * item.quantity;
      return price
    })
    console.log(price)
  }, [productData]);

  // State for quantity (initialize with 1)
  const [baseQty, setBaseQty] = useState(1);

  return (
    <div className="w-2/3 pr-10">
      <div className="w-full">
        <h2 className="font-titleFont text-2xl">Shopping Cart</h2>
      </div>
      <div>
        {productData.map((item) => (
          <div key={item.id} className="flex items-center justify-between gap-6 mt-6">
            <div className="flex items-center gap-2">
              <BiTrash
                onClick={() => {
                  dispatch(deleteItem(item.id));
                  toast.error('Item deleted');
                }}
                className="text-xl text-gray-600 hover:text-red-600 cursor-pointer duration-300"
              />
              <img
                className="w-32 h-32 object-cover"
                src={`http://127.0.0.1:8000${item.image}`}
                alt="productimg"
              />
            </div>
            <h2 className='w-52'>{item.title}</h2>
            <div className='w-52 flex items-center justify-between text-gray-500 gap-4 border p-3'>
              <p className='text-sm'>Quantity</p>
              <div className='flex items-center gap-4 text-sm font-semibold'>
                <button
                  onClick={() => {
                    dispatch(
                      decrementQuantity({
                        id: item.id,
                        title: item.title,
                        image: item.image,
                        price: item.price,
                        quantity: 1,
                        description: item.description
                      })
                    );
                    // Handle quantity decrement logic here
                    setBaseQty(baseQty === 1 ? baseQty : baseQty - 1);
                  }}
                  className='border h-5 font-normal text-lg flex items-center justify-center px-2 hover-bg-gray-700
                    hover-text-white cursor-pointer duration-300 active-bg-black'
                >
                  -
                </button>
                <span>{item.quantity}</span>
                <button
                  onClick={() => {
                    dispatch(
                      incrementQuantity({
                        id: item.id,
                        title: item.title,
                        image: item.image,
                        price: item.price,
                        quantity: 1,
                        description: item.description
                      })
                    );
                    setBaseQty(baseQty + 1);
                  }}
                  className='border h-5 font-normal text-lg flex items-center justify-center px-2 hover-bg-gray-700
                    hover:text-white cursor-pointer duration-300 active-bg-black'
                >
                  +
                </button>
              </div>
            </div>
            <p className='w-10'>Ksh {item.price}</p>
            <p className='w-14'>Total: Ksh {item.quantity * item.price}</p> {/* Calculate total cost */}
          </div>
        ))}
      </div>
      
      <ToastContainer
        position='top-left'
        autoClose={2000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme='dark'
      />
      <button
        onClick={() => {
          dispatch(resetCart());
          toast.error('Cart has been reset');
        }}
        className='bg-red-500 text-white mt-8 ml-7 py-1 px-6 hover:bg-red-800 duration-300'
      >
        Reset Cart
      </button>
      <Link to="/">
        <button className='mt-8 ml-7 text-gray-100 flex items-center bg-black gap-1 hover:text-white duration-300'>
          <BiArrowToLeft />
          Go Shopping
        </button>
      </Link>
    </div>
  );
};

export default CartItem;
