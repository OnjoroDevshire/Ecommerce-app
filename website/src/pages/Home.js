// Home.js
import React, { useState, useEffect } from 'react';
import { useLoaderData } from 'react-router-dom';
import Banner from '../components/Banner';
import Products from '../components/Products';
import { productsData } from '../api/Api'; // Import the updated API function

const Home = () => {
    const [products, setProducts] = useState([]);
    const data = useLoaderData();

    useEffect(() => {
        async function fetchData() {
            try {
                const data = await productsData(); // Use the updated API function
                setProducts(data);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }

        fetchData();
    }, []);

    return (
        <div>
            <Banner />
            <Products products={products} />
        </div>
    );
};

export default Home;
