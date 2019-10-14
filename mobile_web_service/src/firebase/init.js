import * as firebase from "firebase/app"
import "firebase/auth";
import "firebase/firestore";

const config = {
    // Ajoah
    apiKey: "AIzaSyDD84-nLqygHpqVN7jlZOjgZ4one6TdyUc",
    authDomain: "ajoah-2121f.firebaseapp.com",
    databaseURL: "https://ajoah-2121f.firebaseio.com",
    projectId: "ajoah-2121f",
    storageBucket: "ajoah-2121f.appspot.com",
    messagingSenderId: "512593003059",
    appId: "1:512593003059:web:a253df39ea0bd93b585946"

    // JUNSOO
    // apiKey: "AIzaSyAYma8PjVHuQOmESFtYQ2o5cbBgLJhhAEU",
    // authDomain: "junsoo-firestore-study.firebaseapp.com",
    // databaseURL: "https://junsoo-firestore-study.firebaseio.com",
    // projectId: "junsoo-firestore-study",
    // storageBucket: "junsoo-firestore-study.appspot.com",
    // messagingSenderId: "884104881711",
    // appId: "1:884104881711:web:e408b5bfe8101777a348da",
    // measurementId: "G-K0V4658MTQ"
};

firebase.initializeApp(config);
const db = firebase.firestore();

export default db;