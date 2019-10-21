<template>
  <div class="container">
    <div id="recaptcha-container"></div>       
    <form class="card-panel" @submit.prevent="verifyOtp">        
      <h3 class="center deep-purple-text">Ajoah 회원가입</h3>
      <div style="height:30px"></div>      
      <div class="row">
          <div class="field col s12">              
              <label for="icon_prefix">이름(별명)</label>
              <input id="icon_prefix" type="text" class="validate" data-length="20" v-model="nickname">              
              <span class="helper-text" data-error="wrong" data-success="right"></span>
          </div>
      </div> 
      <div class="row">        
        <div class="field col s12">         
          <label for="icon_prefix">핸드폰번호</label>
          <!-- <input id="icon_prefix" type="number" class="validate" data-length="12" v-model="phNo" @keyup="getPhoneMask(phNo)"> -->
          <input id="icon_prefix" type="number" class="validate" data-length="12" v-model="phNo">           
          <span class="helper-text" data-error="wrong" data-success="right"></span>                                     
        </div>             
        <div class="field right">
            <a class="waves-effect waves-teal btn-flat" @click="sendOtp">인증코드받기</a>
        </div>          
      </div>      
      <div class="row">        
        <div class="field col s12">         
          <label for="otp">인증코드</label>
          <input id="otp" type="number" v-model="otp" value="">           
        </div>      
        <!-- <div class="field right col s12">            
            <a class="waves-effect waves-teal btn-flat" @click="sendOtp">인증코드다시받기</a>                         
            <a class="waves-effect waves-teal btn-flat" @click="verifyOtp">인증하기</a>               
        </div>         --> 
      </div>
      <div class="row">
        <div class="field col s12">                  
          <label for="answer">가입질문 : AJOAH 만든이 3명의 중간글자를 입력하세요.<br/>(힌트 : 송*수, 윤*민, 정*현)</label>
          <input id="answer" type="text" v-model="answer" value="">         
        </div>
      </div>
       <div class="field center">
        <button class="btn deep-purple">회원가입 하기</button>
      </div>      
    </form>        
  </div>  
</template>

<script>
import db from '@/firebase/init'
import moment from 'moment'
import slugify from 'slugify'
import * as firebase from "firebase/app"
import "firebase/auth";
import "firebase/firestore";

export default {
  name: 'Signup',
  data(){
    return{
      email: null,
      password: null,
      alias: null,
      feedback: null,
      slug: null,
      phNo: null,
      appVerifier : '',
      otp : '',
      answer : '',
      nickname : '',
      vefication_code : false
    }
  },
  created(){
    this.$store.commit('select_view_false')       
    // console.log("SetPassword this.$store.state.select_view" + this.$store.state.select_view)
  },
  methods: {
     getPhoneMask(val) {
        let res = this.getMask(val)
        this.phNo = res
        //서버 전송 값에는 '-' 를 제외하고 숫자만 저장
        this.model.phNo = this.phNo.replace(/[^0-9]/g, '')
    },
    getMask( phoneNumber ) {
      if(!phoneNumber) return phoneNumber
      phoneNumber = phoneNumber.replace(/[^0-9]/g, '')
  
      let res = ''
      if(phoneNumber.length < 3) {
          res = phoneNumber
      }
      else {
          if(phoneNumber.substr(0, 2) =='02') {
      
              if(phoneNumber.length <= 5) {//02-123-5678
                  res = phoneNumber.substr(0, 2) + '-' + phoneNumber.substr(2, 3)
              }
              else if(phoneNumber.length > 5 && phoneNumber.length <= 9) {//02-123-5678
                  res = phoneNumber.substr(0, 2) + '-' + phoneNumber.substr(2, 3) + '-' + phoneNumber.substr(5)
              }
              else if(phoneNumber.length > 9) {//02-1234-5678
                  res = phoneNumber.substr(0, 2) + '-' + phoneNumber.substr(2, 4) + '-' + phoneNumber.substr(6)
              }
      
          } else {
              if(phoneNumber.length < 8) {
                  res = phoneNumber
              }
              else if(phoneNumber.length == 8)
              {
                  res = phoneNumber.substr(0, 4) + '-' + phoneNumber.substr(4)
              }
              else if(phoneNumber.length == 9)
              {
                  res = phoneNumber.substr(0, 3) + '-' + phoneNumber.substr(3, 3) + '-' + phoneNumber.substr(6)
              }
              else if(phoneNumber.length == 10)
              {
                  res = phoneNumber.substr(0, 3) + '-' + phoneNumber.substr(3, 3) + '-' + phoneNumber.substr(6)
              }
              else if(phoneNumber.length > 10) { //010-1234-5678
                  res = phoneNumber.substr(0, 3) + '-' + phoneNumber.substr(3, 4) + '-' + phoneNumber.substr(7)
              }
          }
      }
      return res
      },
    chksignup(){
         
         let vm = this
         let countryCode = '+82' //대한민국
        //  let countryCode = '+1'
         let phoneNumber = countryCode + this.phNo.substring(1)
         let ref = db.collection('users').doc(phoneNumber)
         
         ref.get().then(doc => {

           if(doc.exists){
              alert(this.phNo + ' 핸드폰번호로 이미 가입 되었습니다.');
              return;
           }else{                          
              alert(this.phNo + ' 핸드폰번호로 가입이 가능합니다.');              
           }
         })                                            
    },
    signup(){
         
         let vm = this
         let countryCode = '+82' //대한민국
        //  let countryCode = '+1'
         let phoneNumber = countryCode + this.phNo.substring(1)
         let ref = db.collection('users').doc(phoneNumber)
         
         ref.get().then(doc => {

           if(doc.exists){
              alert(this.phNo + ' 핸드폰번호로 이미 가입 되었습니다.');
           }else{            
              // Add a new document in collection "cities"
              ref.set({
                nickname: this.nickname,
                reg_datetime : Date.now(),
                sms_phone_number : this.phNo,
                sms_auth_number : this.otp,
                sms_auth_yn : 'Y',
                noti_req_channel : 'MobileWeb',
                sms_auth_datetime : Date.now() 
              }) 
              .then(function() {
                  console.log("Document successfully written!");
                  M.toast({html: '회원 가입 되었습니다. 패스워드를 설정해 주세요.', classes: 'rounded'})
                  
                  // 패스워드 설정 화면 이동
                  vm.$router.push({path:'/setPassword'})
              })
              .catch(function(error) {
                  console.error("Error writing document: ", error);
              });  

           }
         })                                            
    },    
    sendOtp(){

        let vm = this
         let countryCode = '+82' //대한민국
        //  let countryCode = '+1'
         let phoneNumber = countryCode + this.phNo.substring(1)
         let ref = db.collection('users').doc(phoneNumber)
         
         ref.get().then(doc => {

           if(doc.exists){              
              M.toast({html: '핸드폰번호로 이미 가입 되었습니다.<br/>로그인화면으로 이동합니다.', classes: 'rounded'})                 
              let vm = this
              // 메인화면 이동
              vm.$router.push({path:'/login'}) 
              
           }else{                          
              if(this.phNo.length == 0){
                alert('핸드폰번호를 입력해 주세요!');
              }else if(this.phNo.length < 10){
                alert('올바른 핸드폰번호인지 확인해 주세요. ['+this.phNo.length+']');
              }else{
                
                //let countryCode = '+1'
                let countryCode = '+82' //대한민국          
                let phoneNumber = countryCode + this.phNo
                //
                let appVerifier = this.appVerifier                    
                
                firebase.auth().signInWithPhoneNumber(phoneNumber, appVerifier)
                  .then(function (confirmationResult) {
                    // SMS sent. Prompt user to type the code from the message, then sign the
                    // user in with confirmationResult.confirm(code).
                    window.confirmationResult = confirmationResult;               
                    this.vefication_code = true;
                  }).catch(function (error) {
                  // Error; SMS not sent
                  // ...                        
                });
              }
           }
         })                        
      },
      //
      verifyOtp(){
        if(this.vefication_code){
        // if(!this.vefication_code){
          alert('인증코드 받기를 먼저 진행해 주세요.');
        }else if(this.phNo.length < 10){
          alert('핸드폰번호를 올바르게 입력해 주세요.');
        }else if(this.otp.length != 6){
          alert('인증코드 6자리를 입력해 주세요.');
        }else if(this.answer != '준경종'){          
          alert('가입질문 힌트를 확인하시어 3자리 가입질문 답을 입력해 주세요.\n(힌트 : 송*수, 윤*민, 정*현)');
        }else{
                    
          let vm = this
          let code = this.otp
          
          this.signup(); //가입 함수 호출

          //잠시주석 
          window.confirmationResult.confirm(code).then(function (result) {
            // User signed in successfully.
            var user = result.user;            
            //route to set password !
            
            this.signup(); //가입 함수 호출
            console.log("Success");
          }).catch(function (error) {
            // User couldn't sign in (bad verification code?)
            // ...
            console.log("Fail");
          });
        }
        //잠시주석
      },
      initReCaptcha(){
        setTimeout(()=>{
          let vm = this
          window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container', {
            'size': 'invisible',
            'callback': function(response) {
              // reCAPTCHA solved, allow signInWithPhoneNumber.
              // ...
            },
            'expired-callback': function() {
              // Response expired. Ask user to solve reCAPTCHA again.
              // ...
            }
          });
          //
          this.appVerifier =  window.recaptchaVerifier
        },1000)
      }
  },
    created(){
      this.initReCaptcha()
    }
} 
</script>

<style>
.signup{
  max-width: 400px;
  margin-top: 60px;
}
.signup h2{
  font-size: 2.4em;
}
.signup .field{
  margin-bottom: 16px;
}
</style>

