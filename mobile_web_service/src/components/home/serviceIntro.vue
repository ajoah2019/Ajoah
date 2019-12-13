<template>
<div class="container">
  <div class="row">
    <div class="col s12 m7">
      <div class="card">
        <div class="card-image">
          <img src="../../img/toilet_service.jpg">          
        </div>
        <div class="card-content center-align" style="padding:20px 5px 5px 5px">
          <span class="" style="font-size:19px;">Ajoah에 오신 것을 환영합니다.</span>          
        </div>
        <div class="card-content center-align" style="margin: 5px 5px 5px 5px;padding:5px 5px 5px 5px">          
          <p style="font-size:13px">Ajoah 서비스를 사용하시려면 회원가입이 필요합니다.<br/>
          회원가입이 되어 있으시면 로그인하여 사용해 주세요.</p>
        </div>
        <div class="card-action center-align">
          <a href="#" @click="signup()">회원가입</a>
          <a href="#" @click="login()">로그인</a>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- <div class="signup container">    
    <form class="card-panel" @submit.prevent="login">        
      <h5 class="center deep-purple-text">Ajoah 서비스에 오신 것을<br/>환영합니다.</h5>
      <div style="height:50px"></div>
      <ul>
            <li><a class="deep-purple-text"><h6>Ajoah 서비스를 사용하시려면 회원가입이 필요합니다.</h6></a></li>
            <li><a class="deep-purple-text"><h6>회원가입이 되어 있으시면 로그인하여 사용해 주세요.</h6></a></li>            
      </ul>      
      <div style="height:100px"></div>      
       <div class="field center">
        <button class="btn deep-purple" @click="signup()">회원가입</button>   
        <button class="btn deep-purple" @click="login()">로그인</button> 
      </div>      
    </form> 
  </div> -->
</template>

<script>

var localStorage = window.localStorage;
const STR_KEY_PHONE_NO = "phoneNo";
const STR_KEY_PHONE_PW = "ajoah_pw";
const STR_KEY_AUTOLOGIN = "ajoah_auto_login";

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

        this.$store.commit('select_view_false')       
        // console.log("servieIntro this.$store.state.select_view" + this.$store.state.select_view)

      let ajoah_autologin = localStorage.getItem(STR_KEY_AUTOLOGIN);
      
      if(ajoah_autologin == "true")
      {            
          this.login(); 
      }else{        
         //
      }

    },
    methods:{ 
      login(){
        let vm = this
   
        vm.$router.push({path:'/login'})        
      },
      signup(){
            let vm = this
            // 패스워드 설정 화면 이동
            vm.$router.push({path:'/signup_1'}) 
      }
    }
  }
</script>
