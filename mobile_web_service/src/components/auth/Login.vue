<template>
<div class="signup container">    
    <form class="card-panel" @submit.prevent="login">        
      <h3 class="center deep-purple-text">AJOAH~ Login</h3>
      <div class="row">        
        <div class="field col s12">         
          <label for="phNo">Enter Your HandPhone Number</label>
          <input id="phNo" type='number' v-model="phNo">                                     
        </div>                   
      </div>      
      <div class="row">        
        <div class="field col s12">         
          <label for="password">Enter Password</label>
          <input id="password" type='password' v-model="password">           
        </div>      
      </div>     
       <div class="field center">
        <button class="btn deep-purple">Login</button>
      </div>      
    </form> 
  </div>
</template>

<script>
import * as firebase from "firebase/app"
import "firebase/auth";
import "firebase/firestore";

  export default {
    data(){
      return{
        phNo: '6505551234',
        password: '123456'
      }
    },
    methods:{
      login(){
        let vm = this
        // let countryCode = '+82' //대한민국
        let countryCode = '+1' //미국
        let email = countryCode + this.phNo + '@ajoah2019.com'
        let password = this.password
        //
        firebase.auth().signInWithEmailAndPassword(email, password).then(function(){
          //route to home on success !
          vm.$router.push({path:'/main'})
        }).catch(function(error) { 
          // Handle Errors here.
          var errorCode = error.code;
          var errorMessage = error.message;
          // ...
          let errMsg = error.message.toLowerCase()
          while(errMsg.indexOf('email') != -1){
            errMsg = errMsg.replace("email address", "phone number");
          }
          //
          alert('Error: ' + errMsg)
        });
      }
    }
  }
</script>
