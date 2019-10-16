<template>
<div> 
  <div class="navbar-fixed">
        <nav class="nav-wrapper indigo">
            <div class="container">
                <a href="#" class="brand-logo">AJOAH~!</a>
                <a href="#" class="sidenav-trigger" data-target="mobile-links">
                    <i class="material-icons">menu</i>
                </a>
                <ul class="right hide-on-med-and-down">                                        
                    <li v-if="!user"><router-link :to="{ name: 'Signup' }">Signup</router-link></li>
                    <li v-if="!user"><router-link :to="{ name: 'Login' }">Login</router-link></li>                    
                    <li v-if="user"><a>{{ user.email }}</a></li>
                    <li v-if="user"><a @click="SetPassword">Set Password</a></li>
                    <li v-if="user"><a @click="logout">Logout</a></li>
                    <li v-if="user"><a class="sidenav-close" @click="showAbout()">About</a></li>        
                    <!-- <li v-if="user"><a href="#view_nav_reservation" class="modal-trigger" @click="showReserve()">예약자보기</a></li> -->
                    <!-- <li v-if="user"><a href="#reserve" class="modal-trigger">예약하기</a></li> -->
                    <li v-if="!user"><a class="sidenav-close" @click="showAbout()">About</a></li>        
                    <li><a href="https://t.me/ajoah_bot" target="_blank">텔레그램봇 바로가기</a></li>
                </ul>
            </div>
        </nav> 
    </div>
 
    <ul class="sidenav" id="mobile-links">
        <li v-if="!user" class="sidenav-close" @click="closeAbout()"><router-link :to="{ name: 'Signup' }">Signup</router-link></li>
        <li v-if="!user" class="sidenav-close" @click="closeAbout()"><router-link :to="{ name: 'Login' }">Login</router-link></li>
        <li v-if="user" class="sidenav-close"><a>{{ user.email }}</a></li>
        <li v-if="user" class="sidenav-close"  @click="closeAbout()"><router-link :to="{ name: 'Index' }">메인화면</router-link></li>
        <li v-if="user" class="sidenav-close"  @click="closeAbout()"><router-link :to="{ name: 'SetPassword' }">Set Password</router-link></li>
        <li v-if="user" class="sidenav-close"><a @click="logout">Logout</a></li>
        <li v-if="user"><a class="sidenav-close" @click="showAbout()">About</a></li>        
        <!-- <li v-if="user"><a href="#view_nav_reservation" class="modal-trigger sidenav-close" @click="showReserve()">예약자보기</a></li> -->
        <!-- <li v-if="user"><a href="#reserve" class="modal-trigger sidenav-close">예약하기</a></li> -->
        <li v-if="!user"><a class="sidenav-close" @click="showAbout()">About</a></li>        
        <li ><a href="https://t.me/ajoah_bot" target="_blank">텔레그램봇 바로가기</a></li>
    </ul>

  <!-- 예약자보기 하단 모달 -->
    <div id="view_nav_reservation" class="modal bottom-sheet">        
        <ul class="collection with-header">
            <li class="collection-header">
                <h4>Subscribers</h4>
            </li>
            <li class="collection-item avatar" v-for="toilet_nav_reserve in toilet_nav_reserves" :key="toilet_nav_reserve.id">
                <i class="material-icons circle blue" v-if="toilet_nav_reserve.gender='M'">person</i>
                <i class="material-icons circle pink" v-else>person</i>
                <span class="title">{{toilet_nav_reserve.nickname}}</span>
                <p class="grey-text">{{toilet_nav_reserve.resv_channel}}</p>
                <p class="grey-text">{{toilet_nav_reserve.resv_dttm}}</p>
                <!-- <a href="" class="secondary-content">
                    <i class="material-icons light-blue-text">email</i>
                </a>  -->
            </li>            
        </ul>
    </div> 
    <!-- 예약자보기 하단 모달 -->

    <!-- About Modal -->
    
   <div id="about" class="card" v-if="about_view">
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
    </div>            
    <!-- About Modal -->
 
</div>
</template>

<script>
import db from '@/firebase/init'
import firebase from 'firebase'

export default {
  name: 'Navbar',
  data(){
    return {
        about_view : false,
        user: null,
        toilet_nav_reserves : []       
    }
  },
  created(){
    
    // let user = firebase.auth().currentUser
    firebase.auth().onAuthStateChanged((user) => {
      if(user){
        this.user = user
        // console.log("this.user.name =>" + this.user.name)
        // console.log("this.user.email =>" + this.user.email)
        // console.log("this.user.uid =>" + this.user.uid)
        // console.log("this.user.phoneNumber =>" + this.user.phoneNumber)

      } else {
        this.user = null
      }
    })    
  },
  methods: {        
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
        SetPassword(){
            let vm = this
            // 패스워드 설정 화면 이동
            vm.$router.push({path:'/setPassword'})     
        },
        logout(){
            firebase.auth().signOut().then(() => {
                this.$router.push({ name: 'Login' })
            })
        },
        showAbout(){
            this.about_view = true;            
        },
        closeAbout(){
            this.about_view = false;            
        }
        
    }
}

</script>

<style>

</style>

