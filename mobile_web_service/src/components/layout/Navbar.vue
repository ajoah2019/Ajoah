f<template>
<div> 
  <div class="navbar-fixed">
        <nav class="nav-wrapper indigo">
            <div class="container"> 
                <a href="#" class="brand-logo">AJOAH~!</a>
                <!-- <a href="#" class="brand-logo"  @click="goMain()">AJOAH~!</a> 
                <router-link :to="{ name: 'Signup_1' }">회원가입</router-link> -->
                <a href="#" class="sidenav-trigger" data-target="mobile-links_login" v-if="user">
                    <i class="material-icons">menu</i>  
                </a>
                <a href="#" class="sidenav-trigger" data-target="mobile-links_init" v-else>
                    <i class="material-icons">menu</i> 
                </a>
                <ul class="right hide-on-med-and-down">                                        
                    <li v-if="!user" class="sidenav-close"><router-link :to="{ name: 'Signup_1' }">회원가입</router-link></li>
                    <li v-if="!user" class="sidenav-close"><router-link :to="{ name: 'Login' }">로그인</router-link></li>                    
                    <li v-if="user" class="sidenav-close"><a class="dropdown-trigger" href="#" data-target='dropdown1'>{{ this.toilet_nickname }}</a></li>                    
                    <li v-if="user" class="sidenav-close"><a @click="logout()">로그아웃</a></li>                    
                    <li><a class="sidenav-close modal-trigger" href="#about">About</a></li>                    
                </ul>
            </div>
        </nav> 
    </div> 
 
    <ul class="sidenav" id="mobile-links_init">
        <li  class="sidenav-close" @click="closeAbout()"><router-link :to="{ name: 'Signup_1' }">회원가입</router-link></li>
        <li  class="sidenav-close" @click="closeAbout()"><router-link :to="{ name: 'Login' }">로그인</router-link></li>
        <li ><a class="sidenav-close modal-trigger" href="#about">About</a></li>        

    </ul>

    <ul class="sidenav" id="mobile-links_login">         
        <li ><a class="dropdown-trigger" href="#" data-target='dropdown1'>{{ this.toilet_nickname }}</a></li>                     
        <li class="sidenav-close"><a @click="logout()">로그아웃</a></li>
        <li class="sidenav-close"><a class="sidenav-close modal-trigger" href="#about">About</a></li>                
    </ul> 

    <ul id='dropdown1' class='dropdown-content' style="top:50px">  
        <!-- <li><a href="#!">one</a></li>
        <li><a href="#!">two</a></li>
        <li class="divider" tabindex="-1"></li>
        <li><a href="#!">three</a></li> -->
        <li><a href="#" class="sidenav-close" @click="SetProfile"><i class="material-icons">face</i>이름(닉네임)변경</a></li>
        <li><a href="#" class="sidenav-close" @click="SetPassword"><i class="material-icons">https</i>패스워드변경</a></li>
    </ul>

    <!-- <div class="row" v-if="this.$store.state.select_view">            
            <div class="col s12">
                <select id="toilet_select" @change="onChange($event)">
                    <optgroup label="연호빌딩 8층">
                    <option value="Y8.M" selected>연호8층 남자</option>
                    <option value="Y8.F">연호8층 여자</option>
                    </optgroup>
                    <optgroup label="연호빌딩 7층">
                    <option value="Y7.M">연호7층 남자</option>
                    <option value="Y7.F">연호7층 여자</option>
                    </optgroup>
                </select>
            </div>            
    </div> -->
    <!-- About Modal Structure -->
    <!-- 잠시 주석 -->
    <!-- <div id="about" class="modal ">
        <div class="modal-content" styple="padding : 0 0 0 0">            
            <div class="container">
                <div class="row">
                <div class="col l6 s12">
                    <h5 class="black-text">Ajoah는 여러분의 쾌적한 화장실 이용을 응원합니다!</h5>
                    <p class="black-text text-lighten-4"></p>
                </div>
                <div class="col l4 offset-l2 s12">                    
                    <ul>
                    <li><a class="black-text text-lighten-3" >* 만든이: 송준수, 윤경민, 정종현</a></li>
                    <li><a class="black-text text-lighten-3" >* 만든날짜: 2019년 10월</a></li>                                        
                    </ul>
                </div>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="container" style="padding : 0 0 0 15px">
                Copyright 2019. 송-윤-정.<br/>All Right Reserved.                
                </div>
            </div>            
        </div>
        <div class="modal-footer ">              
            <a href="#" class="modal-close waves-effect waves-green btn-flat ">확인</a>
        </div>
    </div> -->
    <!-- 잠시 주석 -->
 
    <div id="about" class="modal" style="padding : 0 0 0 0">
        <div class="modal-content" style="margin: 0; padding : 0 0 0 0">                        
                <div class="row">
                    <div class="col s12 m7">
                    <div class="card">
                        <div class="card-image">
                        <img src="../../img/toilet_service.jpg">          
                        </div>
                        <div class="card-content center-align" style="padding:20px 5px 5px 5px">
                        <span class="" style="font-size:19px;">Ajoah에 오신 것을 환영합니다.</span>          
                        </div>
                        <div class="card-content center-left" style="margin: 5px 5px 5px 5px;padding:5px 5px 5px 5px">          
                        <p style="font-size:13px">* 만든이: 송준수, 윤경민, 정종현<br/>
                        * 만든날짜: 2019년 10월</p>
                        </div> 
                        <div class="card-action center-left" style="margin: 5px 5px 5px 5px;padding:5px 5px 5px 5px">          
                            <a href="#" style="font-size:10px">Copyright 2019. 송-윤-정. All Right Reserved. </a>                        
                        </div>
                    </div>
                    </div> 
                </div>
             </div>                    
        <div class="modal-footer" style="margin: 0; padding : 0 0 0 0">              
            <a href="#" class="modal-close waves-effect waves-green btn-flat">확인</a>
        </div>
    </div>
    <!-- About Modal Structure -->

    <!-- About Div Image-->    
   <!-- <div id="about" class="card" v-if="about_view">
        <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../../img/about_low.jpg">
        </div>
        <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">기관개발부 ETAX Unit<i class="material-icons right">more_vert</i></span>
            <p><a class="right" @click="closeAbout()">닫기</a></p>
        </div>
        <div class="card-reveal">
            <span class="card-title grey-text text-darken-4">기관개발부 ETAX Unit<i class="material-icons right">close</i></span>
            <p>기관개발부 송준수, 윤경민, 정종현이 만들었어요.</p>
        </div>
    </div>             -->
    <!-- About Div Image-->    
 
</div>
</template>

<script>

const STR_KEY_PHONE_PW = "ajoah_pw";
const STR_KEY_AUTOLOGIN = "ajoah_auto_login";

import db from '@/firebase/init'
import firebase from 'firebase'
window.$ = window.jQuery = window.jquery = require('jquery')

export default {
  name: 'Navbar',  
  data(){
    return {        
        user: null,
        toilet_nav_reserves : [],
        toilet_nickname : '',    
        login_yubu : false
    }
  },
  created(){
    
    //  this.select_view = true
    // console.log("Navbar this.$store.state.select_view = " + this.$store.state.select_view)

    // let user = firebase.auth().currentUser
    firebase.auth().onAuthStateChanged((user) => {
      if(user){
        this.user = user
        // console.log("this.user.name =>" + this.user.name)
        // console.log("this.user.email =>" + this.user.email)
        // console.log("this.user.uid =>" + this.user.uid)
        // console.log("this.user.phoneNumber =>" + this.user.phoneNumber)

            var user = firebase.auth().currentUser;          
            let phoneNumber = firebase.auth().currentUser.phoneNumber;

            console.log("phoneNumber = " + phoneNumber);

            let ref = db.collection('users').doc(phoneNumber)
             
         
            ref.get().then(doc => {

            if(doc.exists){                
                
                this.login_yubu = true;
                this.toilet_nickname = doc.data().nickname;                
                console.log("toilet_nickname = " + this.toilet_nickname);                

            }else{            
               
               this.login_yubu = false;               
            }
            })


      } else {
        this.user = null
      }
    })    
  },
  mounted(){
    //   console.log("Navbar this.select_view = " + this.select_view) 
  },
  methods: {
        dropdown(){ 
                var elems = document.querySelectorAll('.dropdown-trigger');
                var instances = M.Dropdown.init(elems, {
                    alignment: 'left',
                    autoTrigger: true
                });
        },       
        showReserve(){
            
            // toilet_nav_reserves 초기화
            this.toilet_nav_reserves.splice(0);
                                   
            db.collection("reservation").get()    
                    .then(snapshot => {
                snapshot.forEach(doc => {
                let toilet_nav_reserve = doc.data()
                // console.clear()        
                // console.table(doc.data())                
                this.toilet_nav_reserves.push(toilet_nav_reserve)   
            })
            })                        
        }, 
        SetProfile(){
            let vm = this
            // 패스워드 설정 화면 이동
            vm.$router.push({path:'/setProfile'})                   
        },
        SetPassword(){
            let vm = this
            // 패스워드 설정 화면 이동
            vm.$router.push({path:'/setPassword'})             
        },
        logout(){
            firebase.auth().signOut().then(() => {
                let vm = this
                // 패스워드 설정 화면 이동
                vm.$router.push({path:'/login'})                
                localStorage.removeItem(STR_KEY_PHONE_PW);
                localStorage.removeItem(STR_KEY_AUTOLOGIN);
                window.location.reload();    
            })
        },
        showAbout(){
            this.about_view = true;            
        },
        closeAbout(){
            this.about_view = false;            
        },
        goMain(){ 
            let vm = this
            // 메인화면 이동
            // vm.$router.push({path:'/index'})
            // window.location.reload();                
            vm.$router.push({path:'/index'})             
            // window.location.reload();
        },
        refresh(){            
            
            let vm = this
            let user = firebase.auth().currentUser
            firebase.auth().onAuthStateChanged((user) => {
            if(user){ 
                // alert(1)                
                // window.location.reload();  
                vm.$router.push({name:'Index'})
                //window.location.reload();
            } else {                
                // alert(2)                               
                let vm = this         
                vm.$router.push({path:'/'}).catch(e => {})                
            }  
            })
            
        }        
    }
}

document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('.dropdown-trigger');
        var instances = M.Dropdown.init(elems, {
            alignment: 'left',
            autoTrigger: true
        });
    });
</script>

<style>

</style>

