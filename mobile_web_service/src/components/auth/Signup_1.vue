<template>
  <div class="container">
    <div id="recaptcha-container"></div>       
    <form class="card-panel" @submit.prevent="verifyOtp">        
      <h4 class="center deep-purple-text">Ajoah 회원가입 1단계</h4>
      <div style="height:30px"></div>           
      <div class="row">
        <div class="field col s12">                  
          <label for="answer">가입질문 : AJOAH 만든이 3명의 중간글자를 입력하세요.<br/>(힌트 : 송*수, 윤*민, 정*현)</label>
          <input id="answer" type="text" v-model="answer" value="" data-length="3" @keyup="getChk(answer)">
          <span class="helper-text" data-error="wrong" data-success="right"></span> 
          <!-- <span id='#help'>{{this.gaipPos}}</span>                  -->
        </div>
      </div> 
       <div class="field center">
        <button class="btn deep-purple">질문에 답하기</button>
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
  name: 'Signup_1',
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
      vefication_code : false,
      gaipPos :  ''
    }
  },
  created(){
    this.gaipPos = ''
    this.$store.commit('select_view_false')       
    // console.log("SetPassword this.$store.state.select_view" + this.$store.state.select_view)
  },
  methods: {
    getChk(val) {        
        console.log(val + "--" + val.length)  
      if(val.length >= 3) {
                      
        if(val != '준경종'){          
          this.gaipPos = "틀렸습니다."
          // this.gaipPos = ''         
        }else{
          this.gaipPos = "정답입니다."          
          // this.gaipPos = ''
        } 
      }  
        //서버 전송 값에는 '-' 를 제외하고 숫자만 저장
        // this.model.phNo = this.phNo.replace(/[^0-9]/g, '')
    },
     getPhoneChk(val) {
        let res = this.getGaipYubu(val)
        this.gaipPos = res
        //서버 전송 값에는 '-' 를 제외하고 숫자만 저장
        // this.model.phNo = this.phNo.replace(/[^0-9]/g, '')
    },
    getGaipYubu( phoneNumber ) {
      if(!phoneNumber) return phoneNumber
      phoneNumber = phoneNumber.replace(/[^0-9]/g, '')
  
      let res = ''
      if(phoneNumber.length < 3) {
          
      }
      else {
          if(phoneNumber.substr(0, 2) =='02') {
      
              if(phoneNumber.length <= 5) {//02-123-5678
                  
              }
              else if(phoneNumber.length > 5 && phoneNumber.length <= 9) {//02-123-5678
                  
              }
              else if(phoneNumber.length > 9) {//02-1234-5678
                  
              }
      
          } else {
              
              if(phoneNumber.length > 9) { //010-1234-5678
                  this.chksignup()                                
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
              // alert(this.phNo + ' 핸드폰번호로 이미 가입 되었습니다.');
              this.gaipPos = "이미 회원가입 되어 있습니다."
              return;
           }else{                          
              // alert(this.phNo + ' 핸드폰번호로 가입이 가능합니다.');              
              this.gaipPos = "회원가입 가능합니다."
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
        if(this.answer != '준경종'){          
          alert('가입질문 힌트를 확인하시어 3자리 가입질문 답을 입력해 주세요.\n(힌트 : 송*수, 윤*민, 정*현)');
        }else{ 
          let vm = this
          M.toast({html: '정답입니다. 회원가입해주세요..', classes: 'rounded'}) 
          vm.$router.push({name:'Signup'})                      
        } 
        //잠시주석
      }
  },
    created(){     
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

