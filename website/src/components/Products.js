import React from 'react';
import ProductsCard from './ProductsCard'; // Correct import path and component name

const Products = ({ products }) => {
  // Check if products is defined and is an array
  if (!Array.isArray(products)) {
    // Handle the case where products is not defined or not an array
    console.error('Invalid or empty products data');
    return null; // You can return an appropriate component or message here
  }

  console.log(products);

  return (
    <div className='py-10'>
      <div className='flex flex-col items-center gap-4'>
        <h1 className='text-2xl bg-black text-white py-2 w-80 text-center'>
          Let's Shop!!
        </h1>
        <span className='w-20 h-[3px] bg-black'></span>
        <p className='max-w-[700px] text-gray-600 text-center'>
          ggfgjhhghb, hhhfgui;bjkyjgnbvjhdlmklcndjvjdcmdc uicednvsdjkbv cnincs
          csdchcviocv ccnuicjcnskc cniscnioascoasca ocjichuibvwdh sd scascsjcb
          sc svucisdcnks cscsdcnjsc smcscnsdisjkc scsucnsjc snc uivsjkd vsd
          vidnvjksc skvnsvs vsn cvsivs s
        </p>
      </div>
      <div className='max-w-screen-xl mx-auto py-10 grid grid-cols-4 gap-10 '>
      {products.map((product) => (
  <ProductsCard key={product.id} product={product} />
))}

      </div>
    </div>
  );
};

export default Products;
