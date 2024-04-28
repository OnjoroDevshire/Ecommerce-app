import React from 'react';
import { createBrowserRouter, Outlet, ScrollRestoration } from 'react-router-dom'; // Import createBrowserRouter and Outlet
import { RouterProvider } from 'react-router-dom';
import Header from './components/Header';
import Fouter from './components/Fouter';
import { productsData } from './api/Api';
import Home from './pages/Home'; // Import Home component
import Cart from './pages/Cart'; // Import Cart component
import Product from './components/Product';
import Login from './pages/Login';

const Layout = () => {
  return (
    <div>
      <Header />
      <ScrollRestoration/>
      <Outlet />
      <Fouter />
    </div>
  );
};

const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        path: '/',
        element: <Home />,
        loader: productsData,
      },
      {
        path: '/Product/:id',
        element: <Product />,
      },
      {
        path: '/Cart',
        element: <Cart />,
      },
      {
        path: '/Login',
        element: <Login />,
      },
    ],
  },
]);

function App() {
  return (
    <div className='font-bodyFont'>
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
