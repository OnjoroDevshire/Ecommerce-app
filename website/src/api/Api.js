// api.js
import axios from 'axios';

export async function productsData() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/store/"); // Update the API endpoint
        return response.data; // Ensure you access the data directly
    } catch (error) {
        console.error("Error fetching data:", error);
        throw error;
    }
}
