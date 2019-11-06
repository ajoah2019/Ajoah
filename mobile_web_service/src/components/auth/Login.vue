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
          <p>
          <label>
          <input type="checkbox" name="autologin"/>
          <span>자동로그인</span>
          </label>
        </p>             
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

    <ul id='dropdown1' class='dropdown-content'>
        <li><a href="#!">one</a></li>
        <li><a href="#!">two</a></li>
        <li class="divider" tabindex="-1"></li>
        <li><a href="#!">three</a></li>
        <li><a href="#!"><i class="material-icons">view_module</i>four</a></li>
        <li><a href="#!"><i class="material-icons">cloud</i>five</a></li>
    </ul>
  </div>
</template>

<script>


var localStorage = window.localStorage;
const STR_KEY_PHONE_NO = "phoneNo";
const STR_KEY_PHONE_PW = "ajoah_pw";
const STR_KEY_AUTOLOGIN = "ajoah_auto_login";

import * as firebase from "firebase/app"
import "firebase/auth";
import "firebase/firestore";
window.$ = window.jQuery = window.jquery = require('jquery')

  export default { 
    data(){
      return{
        phNo: '',
        password: '',
        auto_login : false
      }
    },
    created(){

      //  console.log("Login this.$store.state.select_view = " + this.$store.state.select_view)
      
    },
    mounted(){
      
      // console.log("Login this.select_view = " + this.select_view)        
      let phoneNo = localStorage.getItem(STR_KEY_PHONE_NO);
      if(phoneNo != null)
      {
        this.phNo = phoneNo;
      }

      let phoneNo_PW = localStorage.getItem(STR_KEY_PHONE_PW);
      if(phoneNo_PW != null)
      {
        this.password = phoneNo_PW;
      }

      let ajoah_autologin = localStorage.getItem(STR_KEY_AUTOLOGIN);
      
      if(ajoah_autologin == "true")
      {  
          $('input:checkbox[name="autologin"]').attr("checked", ajoah_autologin);
          this.login(); 
      }else{        
         $('input:checkbox[name="autologin"]').attr("checked", false);

      }

    },
    methods:{ 
      login(){
        let vm = this
        let countryCode = '+82' //대한민국
        // let countryCode = '+1' //미국
        let email = countryCode + this.phNo.substring(1) + '@ajoah2019.com'
        let password = this.password
        let ajoah_password = this.password
        let phNo = this.phNo;
        let auto_login = this.auto_login;

        $("input:checkbox[name='autologin']").each(function(){
                    
          // //자동로그인 체크 
          // if($(this).is(":checked") == true) {             
          //     auto_login = true;
          // //자동로그인 uncheck    
          // }else{
          //     auto_login = false;
          // }

          auto_login = $(this).is(":checked");

        });
                       
        firebase.auth().signInWithEmailAndPassword(email, password).then(function(){
          //route to home on success !          
          localStorage.setItem(STR_KEY_PHONE_NO, phNo); 
          localStorage.setItem(STR_KEY_PHONE_PW, password);
          localStorage.setItem(STR_KEY_AUTOLOGIN, auto_login);          

          vm.$store.commit('select_view_true')                   
          vm.$router.push({path:'/index'})
          //window.location.reload();
          //window.location.reload(); // <--- 느림의 원인 
                    
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
