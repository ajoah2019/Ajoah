<template>
 <div>    
    <!-- [2] 화장실 현황 리스트-->
    <div class="container">
 
         
    <div class="row">            
        <div class="input-field col s12">
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
        <!-- <div class="row" >             
            <div class="col s12 l12"> 
                    <span class="card-title right">[변경사항은 실시간 업데이트 됩니다.]</span>
            </div> 
        </div>  -->
    <div class="row" style="border: 1px solid; margin: 1px 1px">
       <div class="col s12">  
         <div class="row" style="border: 1px solid">             
            <div class="col s12">
                <div class="card">
                    <div class="card-card-image">                       
                        <a class="btn-floating halfway-fab waves-effect waves-light teal modal-trigger" href="#reserveconfirm">
                            <i class="material-icons">add</i>
                         </a>
                    </div>                    
                    <div class="card-content">
                         <!-- <span class="card-title">{{toilet_selected_nm}} <a href="#view_reservation" class="sidenav-close modal-trigger" @click="showReserve()">예약자 : 3명</a></span>                         -->
                         <span class="card-title">{{toilet_selected_nm}} <a href="#view_reservation" class="sidenav-close modal-trigger">예약자 : {{this.toilet_reserves_cnt}} 명</a></span>                         
                         <span class="badge white-text yellow pulse left" v-if="true">예약중</span>
                         <span class="badge black-text yellow pulse" v-else>비었음</span>                                                                           
                    </div>                     
                </div>
            </div>            
        </div>        
        <div class="row" style="border: 1px solid">             
            <div class="col s12 m6 l6" v-for="toilet_current in toilet_currents_state" :key="toilet_current.id">
                <div class="card">
                    <div class="card-image"> 
                        <img src="../../img/toilet_ing_6_low.jpg" alt="" v-if="toilet_current.using">
                        <img src="../../img/toilet_low.jpg" alt="" v-else>
                        <!-- <img v-bind:src="toilet_ing" alt="" v-if="toilet_current.using">
                        <img v-bind:src="toilet_empty" alt="" v-else> -->
                        <a href="" class="halfway-fab btn-floating red pulse" v-if="toilet_current.using">
                            <i class="material-icons">clear</i>                            
                        </a>
                        <a href="" class="halfway-fab btn-floating green pulse" v-else>
                            <i class="material-icons">sentiment_satisfied_alt</i>
                        </a>                        
                    </div>
                    <div class="card-content">
                        <span class="card-title">{{toilet_current.name}}</span>                        
                         <span class="badge white-text pink" v-if="toilet_current.using">사용중</span>
                         <span class="badge black-text green pulse" v-else>비었음</span>                         
                    </div>
                    <div class="card-action">
                        <a href="#">지속시간 : 3분</a>
                        <a href="#">금일 3명 이용</a>
                    </div>             
                </div> 
            </div>            
        </div>
       </div>  
     </div>      
    </div>           
    <!-- 화장실 현황 리스트-->
<!-- channel : toilet_noti.channel,
                    nickname : toilet_noti.nickname,
                    send_datetime : toilet_noti.send_datetime, 
                    send_message : toilet_noti.send_message,
                    send_type :toilet_noti.send_type ,
                    sms_phone_number : toilet_noti.sms_phone_number,
                    users_fid : toilet.users_fid    -->

    <div class="row"> 
    <div class="col s12 m6">
      <div class="card red lighten-5">
        <div class="card-content  brown-text darken-1">
          <span class="card-title brown-text darken-4">공개 메시지</span>
           <ul class="collapsible">
                <li v-for="toilet_noti in toilet_noties" :key="toilet_noti.id">
                <div class="collapsible-header"><i class="material-icons">filter_drama</i>{{toilet_noti.nickname}}</div>
                <div class="collapsible-body "><span>{{toilet_noti.send_message}}</span></div>
                </li>        
            </ul>
        </div>
        <!-- <div class="card-action">
          <a href="#">This is a link</a>
          <a href="#">This is a link</a>
        </div> -->
      </div>
    </div>
  </div>

   

    <!-- [3] Index Vue Footer-->
     <footer class="page-footer">
          <div class="container">
            <div class="row">
              <div class="col l6 s12">
                <h5 class="white-text">Ajoah는 여러분의 쾌적한 화장실 이용을 응원합니다!</h5>
                <!-- <p class="white-text text-lighten-4">화장실을 스마트하게 사용해 보세요.</p> -->
                <!-- <a href="https://t.me/ajoah_bot" class="white-text text-lighten-4" target="_blank">텔레그램봇 바로가기</a> -->
              </div>
              <div class="col l4 offset-l2 s12">
                <!-- <h5 class="white-text">텔레그램봇 바로가기</h5> --> 
                <ul>
                  <li><a href="https://t.me/ajoah_bot" class="grey-text text-lighten-3" target="_blank" cursor="hand">텔레그램봇 바로가기</a></li>
                  <!-- <li><a class="grey-text text-lighten-3" href="#!">Link 2</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li> -->
                </ul>
              </div>
            </div>
          </div>
          <div class="footer-copyright">
            <div class="container">
           Copyright 2019. 송-윤-정. All Right Reserved.
            <!-- <a class="grey-text text-lighten-4 right" href="#!">More Links</a> -->
            </div>
          </div>
     </footer>

    <!-- 예약하기 전 Confirm 확인창 Modal-->
    <div id="reserveconfirm" class="modal">
        <div class="modal-content">
            <h6>화장실 예약하시겠습니까?</h6>
        </div>
        <div class="modal-footer">
            <a href="#!" class="modal-close btn orange">취소</a>
            <a class="modal-close btn orange" @click="DoReserve()">확인</a>
            <a class="modal-close btn orange" @click="ChkTest()">확인2</a>
        </div>
    </div>
    <!-- 예약하기 전 Confirm 확인창 Modal-->

   <!-- 예약자보기 하단 모달 -->
    <div id="view_reservation" class="modal bottom-sheet">        
        <ul class="collection with-header">
            <li class="collection-header">
                <h4>{{toilet_selected_nm}} 예약자</h4>
            </li>
            <li class="collection-item avatar" v-for="toilet_reserve in toilet_reserves" :key="toilet_reserve.id">
                <!-- <i class="material-icons circle blue" v-if="toilet_reserve.gender='M'">person</i>
                <i class="material-icons circle pink" v-else>person</i> -->
                <i class="material-icons circle blue">person</i>
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
  </div>
</template>

<script>
import db from '@/firebase/init'
import moment from 'moment'
import * as firebase from "firebase/app"
import "firebase/auth";
import "firebase/firestore";
// 참조 오브젝트 초기화
var tmpObj = {};
var tmpGroupObj = {};

export default {
  name: 'Index',  
  data(){
    return{      
      toilet_currents_state : [],
      toilet_reserves : [],
      toilet_noties : [],
      toilet_noties_cnt : 0,
      toilet_selected_nm : '',
      toilet_selected_val : '',
      nickname: null,
      phone_num : null,
      feedback: null,      
      showPreloader : false,
      toilet_reserve_nickname : '',
      toilet_reserve_phone_no : '',   
      toilet_reserve_seq : 0,   
      toilet_reserves_cnt : 0,
      toilet_current_using_state : 0,
      publicPath: process.env.BASE_URL,
      toilet_ing : process.env.BASE_URL + "static/img/toilet_ing_6_low.jpg",    
      toilet_empty : process.env.BASE_URL + "static/img/toilet_low.jpg"      
    }
  },
  created(){        
    
    this.$store.commit('select_view_true')       
    // console.log("Index this.$store.state.select_view = " + this.$store.state.select_view)

    let baseUrl = ''
    if (process.env.NODE_ENV === 'production') {
        this.toilet_ing = process.env.BASE_URL + "static/img/toilet_ing_6_low.jpg"
        this.toilet_empty = process.env.BASE_URL + "static/img/toilet_low.jpg"
    }else {
        this.toilet_ing = "/static/img/toilet_ing_6_low.jpg"
        this.toilet_empty = "/static/img/toilet_low.jpg"
    }
    
    let user = firebase.auth().currentUser
    firebase.auth().onAuthStateChanged((user) => {
      if(user){
        this.user = user        
      } else {
        this.user = null
        
        let vm = this
   
        vm.$router.push({path:'/login'})
        window.location.reload();
      }  
    })
  },
  mounted(){

    var target = document.getElementById("toilet_select");
    var target_value = target.options[target.selectedIndex].value;
    var target_name = target.options[target.selectedIndex].text;


    this.toilet_selected_val = target_value; 
    this.toilet_selected_nm = target_name;    

    let ref = db.collection("current")  
    
    console.log("mounted");

    // subscribe to changes to the 'messages' collection
    ref.onSnapshot(snapshot => {
      snapshot.docChanges().forEach(change => {

        if (change.type === "added") {
                
                // console.log("added : ", change.doc.data());                
                let toilet_current = change.doc.data()                    

                // 참조 오브젝트에 화장실 정보 맵핑                
                tmpObj[toilet_current.id] = toilet_current;
                this.toilet_currents_state.push(toilet_current);

                if(tmpGroupObj[toilet_current.group] == null){

                    tmpGroupObj[toilet_current.group] = [];                    
                }

                tmpGroupObj[toilet_current.group] = toilet_current;
                
                // console.log("change.doc.data() =" + change.doc.data());
                // console.log("toilet_current = " + toilet_current.id);
                // console.log("tmpObj = " + tmpObj[toilet_current.id].id);
                //console.log("toilet_current.group = " + toilet_current.group);
                //console.log("tmpGroupObj = " + tmpGroupObj[toilet_current.group].id);               
        }

        if (change.type === "modified") {
                console.log("modified : ", change.doc.data());
                // console.log("Modified city: ", change.doc.data().id);

                // 변경된 오브젝트만 새로 맵핑
                tmpObj[change.doc.data().id] = change.doc.data();

                // var found = toilet_currents.find(function(change.doc.data().id) {
                //   return change.doc.data().id;
                // });

             //this.toilet_currents.splice(0);      
             //this.doJohoi();    
        }
      })
    }) 
        

    // tmpGroupObj.forEach(doc => {
    //     // let toilet_current_state = doc.data();       
    //     //console.table(doc.data())                        
    //     this.toilet_current_states.push(tmpGroupObj[this.toilet_selected_val])        
    //     // console.log("test ===>" + doc.data());        
    // })

    // this.doJohoi();
    //  this.toilet_currents = tmpGroupObj[this.toilet_selected_val]
    this.select_view = true;
    console.log("this.select_view" + this.select_view)
    this.showReserve();
    this.showNoties();
  },
  methods: {

        onChange(event) {
            
            this.showPreloader = true;
             // toilet_currents 초기화
            // this.toilet_currents.splice(0);                     
            // console.log(event.target.value)
            var target = document.getElementById("toilet_select");
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;

            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;            
            this.doJohoi();             
                                                                            
        }, 
        doJohoi(){
             
            // this.toilet_currents.splice(0);                                 

            var target = document.getElementById("toilet_select");
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;

            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;    
            
            db.collection("current").where("group","==",target_value).get()    
                    .then(snapshot => {
                tmpObj = {};
                snapshot.forEach(doc => {
                    let toilet_current = doc.data();       
                    //console.table(doc.data())                
                    this.toilet_currents_state.push(toilet_current);                    
                    console.log("---");
                    console.log(this.toilet_currents);
                    tmpObj[doc.data().id] = doc.data();
                })
            })
            
            this.toilet_currents = tmpGroupObj[this.toilet_selected_val]

            this.showPreloader = false ;          
            this.show = true;
        },
        showReserve(){
            
            // toilet_reserves 초기화
            this.toilet_reserves.splice(0);

            var target = document.getElementById("toilet_select");
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;

            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;    

            db.collection("reservation").where("location","==",this.toilet_selected_val).get()
                    .then(snapshot => {
                this.toilet_reserves_cnt = snapshot.size
                snapshot.forEach(doc => {
                let toilet_reserve = doc.data()                
                console.log("toilet_reserve = " + doc.data())                
                this.toilet_reserves.push({
                    location : toilet_reserve.location,
                    nickname : toilet_reserve.nickname,
                    phone_num : toilet_reserve.phone_num, 
                    resv_channel : toilet_reserve.resv_channel,
                    resv_dttm : moment(toilet_reserve.resv_dttm).format('lll') ,
                    seq : toilet_reserve.seq   
                    }) 
                })
            })                         
        },
        showNoties(){
           // toilet_reserves 초기화
            this.toilet_noties.splice(0);

            var target = document.getElementById("toilet_select");
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;

            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;    

            let cnt = 0

            db.collection("noties").orderBy('send_datetime','desc').get()
                    .then(snapshot => {
                this.toilet_noties_cnt = snapshot.size
                console.log("this.toilet_noties_cnt = " + this.toilet_noties_cnt)  
                snapshot.forEach(doc => {
                
                let toilet_noti = doc.data()                
                                              
                if(cnt < 5){
                    this.toilet_noties.push({
                        channel : toilet_noti.channel,
                        nickname : toilet_noti.nickname,
                        send_datetime : toilet_noti.send_datetime, 
                        send_message : toilet_noti.send_message,
                        send_type :toilet_noti.send_type ,
                        sms_phone_number : toilet_noti.sms_phone_number,
                        users_fid : toilet_noti.users_fid,
                        id : doc.id   
                        }) 
                    cnt = cnt + 1
                    console.log("this.cnt = " + cnt)  
                }

                })
                
            })     
        },
        ChkTest()
        {
            console.log("------------");
            console.log(tmpObj);
            if(tmpObj["Y7.M.01"].using) 
                tmpObj["Y7.M.01"].using = false;
            else
                tmpObj["Y7.M.01"].using = true;
            // console.log(tmpObj["Y7.M.01"].using = true);
        },
        DoReserve(){
                        
            db.collection("current").where("group","==",this.toilet_selected_val).where("using","==",false).get()
                    .then(snapshot => {                
                this.toilet_current_using_state = snapshot.size

                if(this.toilet_current_using_state > 0){
                    M.toast({html: '지금 화장실이 비어있어요. 바로 달려가세요~', classes: 'rounded'})
                }
            })

            return;

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
