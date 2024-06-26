import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux';
import CartItem from '../components/CartItem';
import { ToastContainer, toast } from 'react-toastify';

const Cart = () => {
  const productData = useSelector((state) => state.bazar.productData);
  const userInfo = useSelector((state)=> state.bazar.userInfo);
  const [totalAmt, setTotalAmt] = useState(0);

  useEffect(() => {
    let price = 0;
    productData.forEach((item) => {
      price += item.price * item.quantity;
    });
    setTotalAmt(price.toFixed(2)); // Format totalAmt to have 2 decimal places
  }, [productData]);
  const handleCheckout=()=>{
    if (userInfo){
      setPayNow(true)
    }else{
      toast.error("Please sign in to checkout!");

    }
  }

  return (
    <div>
      <div className='max-w-screen-xl mx-auto py-20 flex'>
        <CartItem />
        <div className='w-1/3 bg-[#fafafa] py-6 px-4'>
          <div className='flex flex-col gap-6 border-b-[1px] border-b-gray-400 pb-6'>
            <h2 className='text-2xl font-medium'>cart totals</h2>
            <p className='flex items-center gap-4 text-base'>
              Subtotal{" "}
              <span className='font-titleFont font-bold text-lg'>
                Ksh. {totalAmt}
              </span>
            </p>
            <p className='flex items-start gap-4 text-base'>
              {" "}
              Shipping {''}
              <span>
                fvhdjcsdcksdcklm cijicklsmc cscoocm ccmsklc cmscs cc slc
                alcmaca cccks cscksmcksd vsdvksk sc scmscmkc sdcss s smkvknv
                vmdmv
              </span>
            </p>
          </div>
          <p>
            {" "}
            Total{" "}
            <span className='text-xl font-bold'>Ksh. {totalAmt}</span>
          </p>
          <button onClick={handleCheckout} className='text-base bg-black text-white w-full py-3 mt-6 hover:bg-gray-800 duration-300'>
            Proceed to Checkout
          </button>
        </div>
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
    </div>
  );
};

export default Cart;
