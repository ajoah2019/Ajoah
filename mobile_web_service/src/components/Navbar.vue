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
                    <!-- <li><a href="" class="btn white indigo-text">새로고침</a></li> -->
                    <li><a href="" class="">새로고침</a></li>
                    <li><a href="#view_nav_reservation" class="modal-trigger" @click="showReserve()">예약자보기</a></li>
                    <li><a href="#reserve" class="modal-trigger">예약하기</a></li>
                    <li><a href="#about" class="modal-trigger">About</a></li>
                    <li><a href="#contact" class="modal-trigger">Contact</a></li>
                    <li><a href="https://t.me/ajoah_bot" target="_blank">텔레그램봇 바로가기</a></li>
                </ul>
            </div>
        </nav>
    </div>

    <ul class="sidenav" id="mobile-links">
        <li><a href="#view_nav_reservation" class="modal-trigger" @click="showReserve()">예약자보기</a></li>
        <li><a href="#reserve" class="modal-trigger">예약하기</a></li>
        <li><a href="#about" class="modal-trigger">About</a></li>
        <li><a href="#contact" class="modal-trigger">Contact</a></li>
        <li><a href="https://t.me/ajoah_bot" target="_blank">텔레그램봇 바로가기</a></li>
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
 
</div>
</template>

<script>
import db from '@/firebase/init_firestore'

export default {
  name: 'Navbar',
  data(){
    return {
        toilet_nav_reserves : []       
    }
  },
  methods: {        
        showReserve(){
            
            // toilet_nav_reserves 초기화
            this.toilet_nav_reserves.splice(0);
                                   
            db.collection("reservation").get()    
                    .then(snapshot => {
                snapshot.forEach(doc => {
                let toilet_nav_reserve = doc.data()
                console.clear()        
                console.table(doc.data())                
                this.toilet_nav_reserves.push(toilet_nav_reserve)   
            })
            })                        
        }
    }
}
</script>

<style>

</style>

