
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-analytics.js";
// import { GoogleauthProvider } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-auth.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-auth.js";
import { signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDi_kfB8y9f5gDhDkm7YfiSyVCgqrzrY3E",
  authDomain: "grain-gain.firebaseapp.com",
  projectId: "grain-gain",
  storageBucket: "grain-gain.firebasestorage.app",
  messagingSenderId: "680215356865",
  appId: "1:680215356865:web:fb629ccfede3ad117bbb40",
  measurementId: "G-BZT1WM5R2P"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
auth.languageCode = 'en'; 
const provider = new GoogleAuthProvider();



//input fields

const email = document.getElementById('email').value;
const password = document.getElementById('password').value;


const google_login = document.getElementById("social-btn");
google_login.addEventListener("click", function(event){
            
signInWithPopup(auth, provider)
.then((result) => {
  const credential = GoogleAuthProvider.credentialFromResult(result);
  const user = result.user;
  console.log(user);
  window.location.href = "Home.html";
  
}).catch((error) => {
  const errorCode = error.code;
  const errorMessage = error.message;
  
});
    
})
    

// login using creds 


const login = document.getElementById("submitBtn");

login.addEventListener("click", function(event){
    event.preventDefault();
     
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      // Signed in 
      const user = userCredential.user;

      localStorage.setItem("user", JSON.stringify({uid: user.uid, email: user.email}));
      window.location.href = "Home.html";

    })

    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      alert(errorMessage);
    });


  })
        