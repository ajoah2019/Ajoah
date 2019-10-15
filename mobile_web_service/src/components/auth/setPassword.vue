<template>
  <div class="signup container">    
    <form class="card-panel" @submit.prevent="setPassword">        
      <h2 class="center deep-purple-text">Set Password</h2>
      <div class="row">        
        <div class="field col s12">         
          <label for="password">Enter Password</label>
          <input id="password" type='password' v-model="password">                                     
        </div>                   
      </div>      
      <div class="row">        
        <div class="field col s12">         
          <label for="password_2">Re-enter Password</label>
          <input id="password_2" type='password' v-model="password_2">           
        </div>      
      </div>     
       <div class="field center">
        <button class="btn deep-purple">Set Password</button>
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
      return {
        password : '',
        password_2 : ''
      }
    },
    methods:{
      setPassword(){
        if(this.password != this.password_2){
          alert('입력하신 비밀번호와 확인 비밀번호가 일치 하지 않습니다.')
        }else if(this.password.length < 6){
          alert('패스워드가 너무 짧습니다. 패스워드는 적어도 6자리 이상 입력해 주세요.')
        }else{
          let vm = this
          var user = firebase.auth().currentUser;          
          let newEmail = firebase.auth().currentUser.phoneNumber + '@ajoah2019.com'
          console.log("newEmail" + newEmail);
          let newPassword = this.password
          // 
          user.updateEmail(newEmail).then(function() {
            user.updatePassword(newPassword).then(function() {
              alert('패스워드 설정이 성공했습니다. 앞으로는 핸드폰번호와 설정하신 비밀번호로 로그인이 가능합니다.')
              vm.$router.push('/')  //route to app home !
            }).catch(function(error) {
              alert('Error :' + error.message)
            });
          }).catch(function(error) {
            //Logout if session expires !
            if(error.code == 'auth/requires-recent-login'){
              alert("세션이 만료 되었습니다. 재 접속해 주세요.")
              //
              vm.signout()
            }
          });
        }
      },
      signout(){
        firebase.auth().signOut();
        this.$router.push({path:'/'})
        window.location.reload();  //reload on signout !
      }
    }
  }
</script>
