
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-analytics.js";

  import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-auth.js";
  import { getFirestore, doc , setDoc  } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-firestore.js";
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
  const auth = getAuth(app);
  const db = getFirestore(app);



const submit = document.getElementById('submitBtn');


submit.addEventListener('click', function(event){ 
  event.preventDefault();

 const username = document.getElementById('fullName').value;
const email = document.getElementById('email').value; 
const password = document.getElementById('password').value;
const confirmPassword = document.getElementById('confirmPassword').value;


if (!email || !password) {
  alert("Email and password are required!");
  return;
}
if (password.length < 6) {
  alert("Password must be at least 6 characters!");
  return;
}
if (password !== confirmPassword) {
  alert("Passwords do not match!");
  return;
}


createUserWithEmailAndPassword(auth, email, password, username)
  .then((userCredential) => {

    // create user document in firestore
      const user = userCredential.user;
      setDoc(doc(db, "users", user.uid),{
        username: username,
        email: user.email,
        password: password,
        uid: user.uid
        }).then(() => {
          window.location.href = "Sign-in.html";
        })

  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert("Error: " + error.message);
    // ..
});


})





























  // const analytics = getAnalytics(app);

  // //input fields

  //   const email = document.getElementById('email').value;
  //   const password = document.getElementById('password').value;


  //   const submit = document.getElementById('submitBtn');
  //   submit.addEventListener("click", function(event){
  //       event.preventDefault(); //prevents the page from refreshing 
  //       alert(5);        
  //   })

