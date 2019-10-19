<template>
<div class="signup container">    
    <form class="card-panel" @submit.prevent="login">        
      <h5 class="center deep-purple-text">Ajoah 서비스에 오신 것을<br/>환영합니다.</h5>
      <div style="height:50px"></div>
      <ul>
            <li><a class="deep-purple-text"><h6>Ajoah 서비스를 사용하시려면 회원가입이 필요합니다.</h6></a></li>
            <li><a class="deep-purple-text"><h6>회원가입이 되어 있으시면 로그인하여 사용해 주세요.</h6></a></li>
            <!-- <li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>
            <li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li> -->
      </ul>      
      <div style="height:100px"></div>      
       <div class="field center">
        <button class="btn deep-purple" @click="signup()">회원가입</button>   
        <button class="btn deep-purple" @click="login()">로그인</button> 
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

        this.$store.commit('select_view_false')       
        // console.log("servieIntro this.$store.state.select_view" + this.$store.state.select_view)
    },
    methods:{ 
      login(){
        let vm = this
   
        vm.$router.push({path:'/login'})
        window.location.reload();
      },
      signup(){
            let vm = this
            // 패스워드 설정 화면 이동
            vm.$router.push({path:'/signup'}) 
            window.location.reload();    
      }
    }
  }
</script>
