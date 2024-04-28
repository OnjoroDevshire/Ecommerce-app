import React, { useEffect, useState } from 'react';
import { useLocation, useHistory } from 'react-router-dom';
import axios from 'axios';

const Checkout = () => {
  const [details, setDetails] = useState({});
  const [quantity, setQuantity] = useState(1);
  const [shippingAddress, setShippingAddress] = useState({});
  const location = useLocation();
  const history = useHistory();

  useEffect(() => {
    setDetails(location.state.item);
  }, []);

  const handleQuantityChange = (value) => {
    // Handle quantity changes
    if (value >= 1) {
      setQuantity(value);
    }
  };

  const handleAddressChange = (e) => {
    // Handle address input changes
    const { name, value } = e.target;
    setShippingAddress({ ...shippingAddress, [name]: value });
  };

  const handlePlaceOrder = () => {
    // Make an API request to place the order
    axios
      .post('/api/orders/place/', {
        productId: details.id,
        quantity,
        shippingAddress,
      })
      .then((response) => {
        // Handle success, e.g., display order confirmation
        console.log('Order placed:', response.data);
        // Redirect to order confirmation page or show a success message
        history.push('/order-confirmation');
      })
      .catch((error) => {
        // Handle error, e.g., display an error message
        console.error('Error placing order:', error);
      });
  };

  return (
    <div>
      <h1>Checkout</h1>
      <div>
        <h2>Product Details</h2>
        {/* Display product details */}
        <p>Title: {details.title}</p>
        <p>Price: Ksh {details.price}</p>
      </div>
      <div>
        <h2>Shipping Information</h2>
        <div>
          <label htmlFor="address">Address:</label>
          <input
            type="text"
            id="address"
            name="address"
            value={shippingAddress.address || ''}
            onChange={handleAddressChange}
          />
        </div>
        <div>
          <label htmlFor="city">City:</label>
          <input
            type="text"
            id="city"
            name="city"
            value={shippingAddress.city || ''}
            onChange={handleAddressChange}
          />
        </div>
        <div>
          <label htmlFor="zipcode">Zip Code:</label>
          <input
            type="text"
            id="zipcode"
            name="zipcode"
            value={shippingAddress.zipcode || ''}
            onChange={handleAddressChange}
          />
        </div>
      </div>
      <div>
        <h2>Quantity</h2>
        {/* Handle quantity changes */}
        <button onClick={() => handleQuantityChange(quantity - 1)}>-</button>
        <span>{quantity}</span>
        <button onClick={() => handleQuantityChange(quantity + 1)}>+</button>
      </div>
      <div>
        {/* Place order button */}
        <button onClick={handlePlaceOrder}>Place Order</button>
      </div>
    </div>
  );
};

export default Checkout;
