// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBeWbfBJ7Ww3VHQroSpUJHqPOovKce1-ao",
    authDomain: "bazarapp-c1143.firebaseapp.com",
    projectId: "bazarapp-c1143",
    storageBucket: "bazarapp-c1143.appspot.com",
    messagingSenderId: "149344220224",
    appId: "1:149344220224:web:25fcf9b7fd4b3fcbebdba5",
    measurementId: "G-Z9HMJP46GG"
  };

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);