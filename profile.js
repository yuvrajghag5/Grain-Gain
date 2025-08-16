import { initializeApp } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-analytics.js";

  import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-auth.js";
  import { getFirestore, doc , getDoc  } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-firestore.js";

  const firebaseConfig = {
    apiKey: "AIzaSyDi_kfB8y9f5gDhDkm7YfiSyVCgqrzrY3E",
    authDomain: "grain-gain.firebaseapp.com",
    projectId: "grain-gain",
    storageBucket: "grain-gain.firebasestorage.app",
    messagingSenderId: "680215356865",
    appId: "1:680215356865:web:fb629ccfede3ad117bbb40",
    measurementId: "G-BZT1WM5R2P"
  };


    const app = initializeApp(firebaseConfig);
    const auth = getAuth(app);
    const db = getFirestore(app);

    const username = document.getElementById('fullName');
    const email = document.getElementById('email');
    const signout = document.getElementById('sign-out-btn');


    onAuthStateChanged(auth, (user) => {
        if (user) {
            const userDocRef = doc(db, "users", user.uid);
            getDoc(userDocRef).then((docSnapshot)  => {
                if (docSnapshot.exists()) {
                    const userData = docSnapshot.data();
                    username.textContent = userData.displayname;
                    email.textContent = userData.email;
                } else {
                    alert("user not found");
                }

            })
            .catch((error) => {
                console.error(error);
                alert("failed to fetch data")
            })
        }

        
 });


    // logout functionality 
    signout.addEventListener('click', () => {
        signOut(auth).then(() => {  
            // Sign-out successful.
            window.location.href="sign-in.html";
            }).catch((error) => {
                // An error happened.
                console.error("error was occured".error);
                alert("logout failed");
                });
                });







