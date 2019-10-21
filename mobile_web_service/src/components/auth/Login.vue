<template>
<div class="signup container">    
    <form class="card-panel" @submit.prevent="login">        
      <h3 class="center deep-purple-text">Ajoah 로그인</h3>
      <div class="row">        
        <div class="field col s12">         
          <label for="phNo">핸드폰번호를 입력해 주세요.</label>
          <input id="phNo" type='number' v-model="phNo">                                     
        </div>                   
      </div>      
      <div class="row">        
        <div class="field col s12">         
          <label for="password">패스워드를 입력해 주세요.</label>
          <input id="password" type='password' v-model="password">             
        </div>       
      </div>  
       <div class="row">        
        <div class="field col s12">         
          <a @click="goSignUp" style="cursor: hand">회원으로 가입하시려면 여기를 눌러주세요</a>         
        </div>       
      </div>        
       <div class="field center">
        <button class="btn deep-purple">로그인 하기</button>
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
        phNo: '',
        password: ''
      }
    },
    created(){

      //  console.log("Login this.$store.state.select_view = " + this.$store.state.select_view)
      
    },
    mounted(){
        
        // console.log("Login this.select_view = " + this.select_view)        
    },
    methods:{ 
      login(){
        let vm = this
        let countryCode = '+82' //대한민국
        // let countryCode = '+1' //미국
        let email = countryCode + this.phNo.substring(1) + '@ajoah2019.com'
        let password = this.password
        //
        firebase.auth().signInWithEmailAndPassword(email, password).then(function(){
          //route to home on success !
          vm.$store.commit('select_view_true')         
          vm.$router.push({name:'Index'})
          window.location.reload();          
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
      }, 
      goSignUp(){
            
            let vm = this
            // 메인화면 이동
            vm.$router.push({path:'/signup'})                      
        }
    }
  }
</script>
