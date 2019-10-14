// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import firebase from 'firebase'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App :user="user" ></App>',

    data() {
        return {
            user: {}
        }
    },
    methods: {
        getLoginStatus() {
            let vm = this
            firebase.auth().onAuthStateChanged(function(user) {
                if (user) {
                    vm.user = user
                    console.log("// User is signed in by Phone Number : ", user.phoneNumber)
                } else {
                    vm.user = null
                    console.log("// No user is signed in.")
                }
            });
        }
    },
    updated() {
        this.getLoginStatus()
    },
    created() {
        this.getLoginStatus()
    }
})