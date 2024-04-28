import React from 'react';
import {
  GoogleAuthProvider,
  getAuth,
  signInWithPopup,
  signOut,
} from 'firebase/auth';
import { useDispatch } from 'react-redux';
import { toast, ToastContainer } from 'react-toastify';
import { addUser, removeUser } from '../redux/bazarSlice';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate(); // Corrected useNavigate
  const auth = getAuth();
  const provider = new GoogleAuthProvider();

  const handleGoogleLogin = () => {
    signInWithPopup(auth, provider)
      .then((result) => {
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const token = credential.accessToken;
        const user = result.user;
        dispatch(addUser({
          id: user.id,
          name: user.displayName,
          email: user.email,
          image: user.photoURL,
        }));
        setTimeout(() => {
          navigate('/'); // Corrected navigate
        }, 1500);
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = GoogleAuthProvider.credentialFromError(error);
      });
  };

  const handleSignOut = () => {
    signOut(auth)
      .then(() => {
        toast.success('Log Out Successfully');
        dispatch(removeUser())
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className='w-full flex flex-col items-center justify-center gap-10 py-20'>

      <div className='w-full flex items-center justify-center gap-10'>

        <div onClick={handleGoogleLogin} className='text-base w-60 h-12 tracking-wide border-[1p] border-gray-400 rounded-md flex 
        items-center justify-center gap-2 hover-border-blue-600 cursor-pointer duration-300'>
          <img src='' className='w-8' alt='googlelogo' />
          <span className='text-sm text-gray-900'>Sign in with Google</span>
        </div>
        <button onClick={handleSignOut} className='bg-black text-white text-base py-3 px-8 
        tracking-wide rounded-md hover:bg-gray-800 duration-300 '>Sign Out</button>
      </div>
      <div className='w-full flex items-center justify-center gap-10'>

        <div className='text-base w-60 h-12 tracking-wide border-[1p] border-gray-400 rounded-md flex 
        items-center justify-center gap-2 hover-border-blue-600 cursor-pointer duration-300'>
          <img src='' className='w-8' alt='googlelogo' />
          <span className='text-sm text-gray-900'>Sign in with Github</span>
        </div>
        <button className='bg-black text-white text-base py-3 px-8 
        tracking-wide rounded-md hover:bg-gray-800 duration-300 '>Sign Out</button>
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
}

export default Login; 
