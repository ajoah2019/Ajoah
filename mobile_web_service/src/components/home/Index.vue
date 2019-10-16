<template>
 <div class="index container">    
     
    <!-- [2] 화장실 현황 리스트-->
     <div class="container">
         <div class="row" style="">            
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
        </div>
        <div class="row" >             
            <div class="col s12 l12"> 
                    <span class="card-title right">[변경사항은 실시간 업데이트 됩니다. - 테스트]</span>
            </div> 
        </div> 
         <div class="row">             
            <div class="col s12">
                <div class="card">
                    <div class="card-card-image">                       
                        <a class="btn-floating halfway-fab waves-effect waves-light teal modal-trigger" href="#reserveconfirm">
                            <i class="material-icons">add</i>
                         </a>
                    </div>                    
                    <div class="card-content">
                         <span class="card-title">{{toilet_selected_nm}}</span>                        
                         <!-- <span class="badge white-text pink" v-if="toilet_current.using">사용중</span>
                         <span class="badge black-text yellow pulse" v-else>비었음</span>                          -->
                    </div>                     
                </div>
            </div>            
        </div>
        <div class="row"> 
        <div class="col s12 center" v-if="showPreloader">
            <div class="preloader-wrapper big active center">
                <div class="spinner-layer spinner-blue-only center">
                    <div class="circle-clipper left">
                        <div class="circle"></div>
                    </div><div class="gap-patch">
                        <div class="circle"></div>
                    </div><div class="circle-clipper right">
                        <div class="circle"></div>
                    </div>
                </div>
            </div>              
        </div>              
        </div>              
        <div class="row" v-for="toilet_current in toilet_currents" :key="toilet_current.id">             
            <div class="col s12 l6">
                <div class="card">
                    <div class="card-image">
                        <img src="../../img/toilet_ing_6_low.jpg" alt="" v-if="toilet_current.using">
                        <img src="../../img/toilet_low.jpg" alt="" v-else>
                        <a href="" class="halfway-fab btn-floating red pulse" v-if="toilet_current.using">
                            <i class="material-icons">clear</i>                            
                        </a>
                        <a href="" class="halfway-fab btn-floating yellow pulse" v-else>
                            <i class="material-icons">sentiment_satisfied_alt</i>
                        </a>                        
                    </div>
                    <div class="card-content">
                        <span class="card-title">{{toilet_current.name}}</span>                        
                         <span class="badge white-text pink" v-if="toilet_current.using">사용중</span>
                         <span class="badge black-text yellow pulse" v-else>비었음</span>                         
                    </div>                    
                </div>
            </div>            
        </div>
     </div> 
    <!-- 화장실 현황 리스트-->

    <!-- [3] Index Vue Footer-->
     <footer class="page-footer">
          <div class="container">
            <div class="row">
              <div class="col l6 s12">
                <h5 class="white-text">Another Joy Of Ah~!</h5>
                <p class="grey-text text-lighten-4">화장실을 스마트하게 사용해 보세요.</p>
              </div>
              <!-- <div class="col l4 offset-l2 s12">
                <h5 class="white-text">Links</h5>
                <ul>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 1</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 2</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li>
                </ul>
              </div> -->
            </div>
          </div>
          <div class="footer-copyright">
            <div class="container">
           © 2019 Copyright Ajoah   
            <!-- <a class="grey-text text-lighten-4 right" href="#!">More Links</a> -->
            </div>
          </div>
     </footer>

    <!-- <div class="container" v-if="show">
    <div class="row" >
     <div class="col s12 l12">
        <nav class="nav-extended">
            <div class="nav-wrapper"> 
            <a href="#!" class="brand-logo center text-center">3명 예약중</a>      
            </div>
            <div class="nav-content">            
            <a class="btn-floating btn-large halfway-fab waves-effect waves-light teal left modal-trigger" href="#view_reservation" @click="showReserve()">
                <i class="material-icons">add</i>
            </a>
            </div>
            <div class="footer-copyright">
                <div class="container center text-align">
                    © 2019 Copyright Ajoah            
                </div>
            </div>
        </nav>
        </div>
    </div>
    </div> -->
    <!-- Index Vue Footer-->

    <!-- 예약하기 전 Confirm 확인창 Modal-->
    <div id="reserveconfirm" class="modal">
        <div class="modal-content">
            <h6>화장실 예약하시겠습니까?</h6>
        </div>
        <div class="modal-footer">
            <a href="#!" class="modal-close btn orange">취소</a>
            <a class="modal-close btn orange" @click="DoReserve()">확인</a>
        </div>
    </div>
    <!-- 예약하기 전 Confirm 확인창 Modal-->

   <!-- 예약자보기 하단 모달 -->
    <div id="view_reservation" class="modal bottom-sheet">        
        <ul class="collection with-header">
            <li class="collection-header">
                <h4>Subscribers</h4>
            </li>
            <li class="collection-item avatar" v-for="toilet_reserve in toilet_reserves" :key="toilet_reserve.id">
                <i class="material-icons circle blue" v-if="toilet_reserve.gender='M'">person</i>
                <i class="material-icons circle pink" v-else>person</i>
                <span class="title">{{toilet_reserve.nickname}}</span>
                <p class="grey-text">{{toilet_reserve.resv_channel}}</p>
                <p class="grey-text">{{toilet_reserve.resv_dttm}}</p>
                <!-- <a href="" class="secondary-content">
                    <i class="material-icons light-blue-text">email</i>
                </a>  -->
            </li>            
        </ul>
    </div> 
    <!-- 예약자보기 하단 모달 -->

    <!-- Floating Button Menu 버튼 -->   
    <!-- <div class="fixed-action-btn">
        <a class="btn-floating btn-large red">
            <i class="large material-icons">mode_edit</i>
        </a> 
        <ul>
            <li><a class="btn-floating red modal-trigger" href="#verify"><i class="material-icons">insert_chart</i></a></li>
            <li><a class="btn-floating yellow darken-1 modal-trigger" href="#reserve"><i class="material-icons">format_quote</i></a></li>
            <li><a class="btn-floating green modal-trigger" href="#view_reservation" @click="showReserve()"><i class="material-icons">publish</i></a></li>
            <li><a class="btn-floating blue modal-trigger" href="#about"><i class="material-icons">attach_file</i></a></li>
            <li><a class="btn-floating blue modal-trigger" href="https://t.me/ajoah_bot" target="_blank"><i class="material-icons">all_inclusive</i></a></li>
     </ul>
    </div>  -->
    <!-- Floating Button Menu 버튼 -->

    

  </div>
</template>

<script>
import db from '@/firebase/init'
import moment from 'moment'
import * as firebase from "firebase/app"
import "firebase/auth";
import "firebase/firestore";

export default {
  name: 'Index',
  props:['user'],
  data(){
    return{
      
      toilet_currents : [],
      toilet_reserves : [],
      toilet_selected_nm : '',
      toilet_selected_val : '',
      nickname: null,
      phone_num : null,
      feedback: null,      
      showPreloader : false,
      toilet_reserve_nickname : '',
      toilet_reserve_phone_no : '',   
      toilet_reserve_seq : 0   
    }
  },
  created(){    
       
   let ref = db.collection("current")
    
    // subscribe to changes to the 'messages' collection
    ref.onSnapshot(snapshot => {
      snapshot.docChanges().forEach(change => {
        if(change.type == 'modified'){
           console.table("Modified Toilet Detected: ");
           this.doJohoi();
        }
      })
    })    
  },
  mounted(){
    
    this.toilet_currents.splice(0);                     
    var target = document.getElementById("toilet_select");
    var target_value = target.options[target.selectedIndex].value;
    var target_name = target.options[target.selectedIndex].text;

    this.toilet_selected_val = target_value; 
    this.toilet_selected_nm = target_name; 

    this.doJohoi();    
  }, 
  methods: {

        onChange(event) {
            
            this.showPreloader = true;
             // toilet_currents 초기화
            this.toilet_currents.splice(0);                     
            // console.log(event.target.value)
            var target = document.getElementById("toilet_select");
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;

            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;            
            this.doJohoi();            
                                                                            
        }, 
        doJohoi(){
            
            this.toilet_currents.splice(0);                                 

            var target = document.getElementById("toilet_select");
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;

            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;    
            
            db.collection("current").where("group","==",target_value).get()    
                    .then(snapshot => {
                snapshot.forEach(doc => {
                let toilet_current = doc.data()        
                //console.table(doc.data())                
                this.toilet_currents.push(toilet_current)   
            })
            })
            
            this.showPreloader = false ;          
            this.show = true;
        },
        showReserve(){
            
            // toilet_nav_reserves 초기화
            this.toilet_reserves.splice(0);
                                   
            db.collection("reservation").get()    
                    .then(snapshot => {
                snapshot.forEach(doc => {
                let toilet_reserve = doc.data()
                console.clear()        
                console.table(doc.data())                
                this.toilet_reserves.push(toilet_reserve)   
            })
            })                         
        },
        DoReserve(){
            
            var user = firebase.auth().currentUser;          
            let phoneNumber = firebase.auth().currentUser.phoneNumber;

            console.log("phoneNumber = " + phoneNumber);

            let ref = db.collection('users').doc(phoneNumber)
             
         
            ref.get().then(doc => {

            if(doc.exists){                
                this.toilet_reserve_nickname = doc.data().nickname;
                this.toilet_reserve_phone_no = doc.data().sms_phone_number;

                console.log("toilet_reserve_nickname = " + this.toilet_reserve_nickname);
                console.log("toilet_reserve_phone_no = " + this.toilet_reserve_phone_no);
                
                //db.collection("reservation").where("location","==","Y8.M").orderBy("seq", "desc").limit(1).get()    
                db.collection("reservation").where("location","==",this.toilet_selected_val).get()    
                    .then(snapshot => {
                    
                     this.toilet_reserve_seq = snapshot.size + 1;                                         
                     console.log("this.toilet_reserve_seq = " + this.toilet_reserve_seq)
 
                    db.collection('reservation').add({
                        nickname: this.toilet_reserve_nickname,
                        phone_num : this.toilet_reserve_phone_no,
                        resv_dttm: Date.now(),
                        resv_channel : "MobileWeb",
                        location: this.toilet_selected_val,                                                
                        seq : this.toilet_reserve_seq                     
                    }).catch(err => { 
                        console.log(err)
                    })         
 
                    M.toast({html: '예약 신청 되었습니다.', classes: 'rounded'})
                })
 
                

            }else{            
                
                alert('회원가입이 되어 있지 않습니다.');                

            }
            })
             
                                          
            
            
        }
    }
}
 
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
        direction: 'top'        
    });
});
</script>

<style>
</style>
