<template>
 <div>    
    <!-- [2] 화장실 현황 리스트-->
    <div class="container">
            
    <div class="row" style="padding:0; margin:0">            
        <div class="input-field col s12" style="padding:5px 0 0 0; margin:0">
            <select id="toilet_select" class="browser-default" @change="onChange($event)">
                <!-- <select id="toilet_select" @change="onChange($event)"> -->
                <optgroup label="연호빌딩 7층">  
                <option value="Y7.M">연호7층 남자</option>                
                </optgroup> 
                <optgroup label="연호빌딩 8층">
                <option value="Y8.M">연호8층 남자</option>                
                </optgroup>
                <optgroup label="부영빌딩 17층"> 
                <option value="B17.M">부영17층 남자</option>
                </optgroup> 
                <optgroup label="부영빌딩 18층">
                <option value="B18.M">부영18층 남자</option>
                </optgroup> 
            </select> 
        </div>              
    </div>
        <!-- <div class="row" >             
            <div class="col s12 l12"> 
                    <span class="card-title right">[변경사항은 실시간 업데이트 됩니다.]</span>
            </div> 
        </div>  -->
    <!-- <div class="row" style="border: 1px solid; margin: 1px 1px"> -->
    <div class="row" style="margin:0px 0px 0px 00px;padding:0px 0px 0px 0px">
       <div class="col s12" style="margin:0px 0px 0px 0px;padding:0px 0px 0px 0px">  
           
         <!-- <div class="row" style="border: 1px solid">              -->
          <!-- <div class="row">
            <div class="col s12">
                <div class="card">
                    <div class="card-card-image">  
                         <a class="btn-floating halfway-fab waves-effect waves-light teal modal-trigger" href="#reserveconfirm"  v-if="chkResolve">
                            <i class="material-icons">add</i>                            
                         </a>  
                         <a class="btn-floating halfway-fab waves-effect waves-light teal modal-trigger" href="#cancelreserveconfirm" v-else>                            
                            <i class="material-icons">remove</i>
                         </a>
                    </div>                    
                    <div class="card-content"> 
                         
                         <div class="row valign-wrapper" style="margin:0px">
                            <div class="col s6 left" style="margin:0px">
                               <span class="card-title">{{toilet_selected_nm}}</span> 
                            </div> 
                            <div class="col s4" style="padding: 0 0 0 20px">  
                                <span v-if="chkResolve" ><a class='dropdown-trigger btn' href='#' data-target='dropdown_reserve' >예약</a></span>
                                <span v-if="!chkResolve"><a class='dropdown-trigger btn' href='#' data-target='dropdown_cancel'>예약중</a></span>
                            </div>
                        </div>       

                         <span class="card-title">{{toilet_selected_nm}} <a href="#view_reservation" class="sidenav-close modal-trigger">예약자 : {{this.toilet_reserves_cnt}} 명</a></span>                                                                           
                               
                         <span class="badge white-text yellow pulse left" v-if="!chkResolve">예약중</span>
                         
                    </div>                     
                </div>
            </div>            
        </div>        -->



        <!-- <ul id='dropdown_cancel' class='dropdown-content'>            
            <li><a  href="#cancelreserveconfirm" class="modal-trigger">예약취소</a></li>        
            <li><a href="#view_reservation" class="modal-trigger">예약자보기</a></li>        
        </ul> -->

        <!-- 1번째 기획화면 -->
        <!-- <div class="row" style="border: 1px solid">              -->
        <!-- <div class="row" >
            <div class="col s6 m6 l6" v-for="toilet_current in toilet_currents_state" :key="toilet_current.id">
                <div class="card">
                    <div class="card-image"> 
                        <!-- <img src="../../img/toilet_ing_6_low.jpg" alt="" v-if="toilet_current.using"> -->
                        <!-- <img src="../../img/toilet_on_low.jpg" alt="" v-if="toilet_current.using">
                        <img src="../../img/toilet_off_low.jpg" alt="" v-else> --> 
                         
                        <!-- <a class="halfway-fab btn-floating red pulse" v-if="toilet_current.using">
                            <i class="material-icons">clear</i>                            
                        </a> 
                        <a class="halfway-fab btn-floating green pulse" v-else>
                            <i class="material-icons">sentiment_satisfied_alt</i>
                        </a>                         -->
                    <!-- </div> -->
                    <!-- <div class="card-content">
                        <span class="card-title">{{toilet_current.name}}</span>                        
                         <span class="badge white-text pink" v-if="toilet_current.using">사용중</span>
                         <span class="badge black-text green pulse" v-else>비었음</span>                         
                    </div> -->
                    <!-- <div class="card-panel" style="padding:24px 0">
                        <div class="row valign-wrapper" style="margin:0px">
                            <div class="col s2 left" style="margin:0px">
                                <span class="" v-if="toilet_current.id=='Y8.M.01'" style="font-size: 25px">#1</span>
                                <span class="" v-if="toilet_current.id=='Y8.M.02'" style="font-size: 25px">#2</span>
                                <span class="" v-if="toilet_current.id=='Y7.M.01'" style="font-size: 25px">#1</span>
                                <span class="" v-if="toilet_current.id=='Y7.M.02'" style="font-size: 25px">#2</span>
                            </div> 
                            <div class="col s10" style="padding: 0 0 0 20px">  
                                <span class="black-text">
                                    <a href="#" class="orange-text text-darken-3">· 금일 {{toilet_current.usage}}명 이용</a><br/>
                                    <a href="#" class="orange-text text-darken-3" v-if="toilet_current.using">· {{toilet_current.elapsedTime}}</a>                                    
                                    <a href="#" class="orange-text text-darken-3" v-else></a>                         
                                </span>
                            </div>
                        </div>                                                 
                    </div>     

                </div> 
            </div>            
        </div> -->
        <!-- 1번째 기획화면 -->

        <!-- 2번째 화면 -->
        <!-- <div class="row" v-if="!toilet_possible_yubu">
            <div class="col s12 m12 l12" >
                <div class="card">           
                    <span class="card-panel align-left" style="font-size:16px">해당 화장실은 아직 지원하지 않습니다.</span>   
                </div>
            </div>
         </div> -->
        <div class="row" v-if="!toilet_possible_yubu">
        <div class="col s12 m12 l12" >
        <div class="card blue-grey darken-1">           
            <div class="grey lighten-5" style="padding:10px 10px">
                <div class="row valign-wrapper" style="margin:0;padding:0">
                    <div class="col s12 left" style="margin:0px;padding:0">
                        <span class="card-title" style="font-size:18px">서비스 미지원 화장실 입니다.</span> 
                    </div> 
                    <div class="col s4" style="padding: 0 0 0 20px">  
                    </div>
                </div>   
            </div>
         </div>
         </div>
         </div>

        <div class="row" v-if="toilet_possible_yubu" style="margin:0px 0px 0px 0px;padding:0px 0px 0px 0px">
        <div class="col s12 m12 l12" style="margin:0px 0px 0px 0px;padding:0px 0px 0px 0px">
        <!-- <div class="card blue-grey darken-1">            -->
            <div class="lighten-5" style="padding:10px 10px">
                <div class="row valign-wrapper" style="margin:0px">
                    <div class="col s6 left" style="margin:0px">
                        <!-- <span class="card-title">{{toilet_selected_nm}}</span>  -->
                    </div> 
                    <div class="col s4" style="padding: 0 0 0 20px">  
                        <span v-if="chkResolve" ><a class='dropdown-trigger btn' href='#' data-target='dropdown_reserve'>빈칸알림</a></span>
                        <span v-if="!chkResolve"><a class='dropdown-trigger btn' href='#' data-target='dropdown_reserve'>알림수신중</a></span>
                    </div>
                </div>   
            </div>  
            <div class="card-panel z-depth-0" style="padding: 3px 5px 0 7px; margin: 2px 0 0px 0">
                 <div class="row" > 
                    <div class="col s6 m6 l6 z-depth-0" v-for="toilet_current in toilet_currents_state" :key="toilet_current.id">
                        <div class="card">
                            <div class="card-image z-depth-0"> 
                                <!-- <img src="../../img/toilet_ing_6_low.jpg" alt="" v-if="toilet_current.using"> -->
                                <img src="../../img/toilet_on_low.jpg" alt="" v-if="toilet_current.using">
                                <img src="../../img/toilet_off_low.jpg" alt="" v-else>
                                
                                <a class="halfway-fab btn-floating red pulse" v-if="toilet_current.using">
                                    <i class="material-icons">clear</i>                            
                                </a> 
                                <a class="halfway-fab btn-floating green pulse" v-else>
                                    <i class="material-icons">sentiment_satisfied_alt</i>
                                </a>                        
                            </div>
                            <!-- <div class="card-content">
                                <span class="card-title">{{toilet_current.name}}</span>                        
                                <span class="badge white-text pink" v-if="toilet_current.using">사용중</span>
                                <span class="badge black-text green pulse" v-else>비었음</span>                         
                            </div> --> 
                            <!-- 2019.12.19 이전 UI -->
                            <!-- <div class="card z-depth-0" style="padding:24px 0">
                                <div class="row valign-wrapper z-depth-0" style="margin:0px;height:30px">
                                    <div class="col s2 left z-depth-0" style="margin:0px" v-if="toilet_current.using">
                                        <span class="orange-text text-darken-3" style="font-size: 25px">{{toilet_current.name}}</span>                                        
                                    </div> 
                                    <div class="col s2 left z-depth-0" style="margin:0px" v-else>
                                        <span class="green-text text-darken-2" style="font-size: 25px">{{toilet_current.name}}</span>
                                    </div> 
                                    <div class="col s10 z-depth-0" style="padding: 0 0 0 20px">  
                                        <span class="black-text" v-if="toilet_current.using">
                                            <a href="#" class="orange-text text-darken-3">· 금일 {{toilet_current.usage}}명 이용</a><br/>
                                            <a href="#" class="orange-text text-darken-3">· {{toilet_current.elapsedTime}}</a>                                                                                
                                        </span>
                                        <span class="black-text" v-else>
                                            <a href="#" class="green-text text-darken-2">· 금일 {{toilet_current.usage}}명 이용</a><br/>                                                                                                                       
                                        </span>
                                    </div>
                                </div>                                                 
                            </div>      -->

                            <!-- 2019.12.19 투비 UI -->
                            <div class="card z-depth-0" style="padding:24px 0"> 
                                <div class="row valign-wrapper z-depth-0" style="margin:5px;padding: 0px 0px;height:30px">
                                    <div class="col s12 left z-depth-0" style="margin:0px" v-if="toilet_current.using">
                                        <span class="orange-text text-darken-3" style="font-size: 23px">{{toilet_current.name}}</span>                                        
                                    </div>  
                                    <div class="col s12 left z-depth-0" style="margin:0px" v-else>
                                        <span class="green-text text-darken-2" style="font-size: 23px">{{toilet_current.name}}</span>
                                    </div>                                     
                                </div>                     
                                <div class="row valign-wrapper z-depth-0" style="margin:0px;height:30px">
                                    <!-- <div class="col s2 left z-depth-0" style="margin:0px" v-if="toilet_current.using">
                                        <span class="orange-text text-darken-3" style="font-size: 25px">{{toilet_current.name}}</span>                                        
                                    </div> 
                                    <div class="col s2 left z-depth-0" style="margin:0px" v-else>
                                        <span class="green-text text-darken-2" style="font-size: 25px">{{toilet_current.name}}</span>
                                    </div>  -->
                                    <div class="col s12 z-depth-0" style="padding: 10px 0 0 20px">  
                                        <span class="black-text" v-if="toilet_current.using">
                                            <a href="#" class="orange-text text-darken-3">· 금일 {{toilet_current.usage}}명 이용</a><br/>
                                            <a href="#" class="orange-text text-darken-3">· {{toilet_current.elapsedTime}}</a>                                                                                
                                        </span>
                                        <span class="black-text" v-else>
                                            <a href="#" class="green-text text-darken-2">· 금일 {{toilet_current.usage}}명 이용</a><br/>                                                                                                                       
                                        </span>
                                    </div>
                                </div>                                                 
                            </div> 



                        </div> 
                    </div>            
                </div>
            </div>                
        <!-- </div> -->
        </div>
        </div>


       </div>  
     </div>      
       

    <ul id='dropdown_reserve' class='dropdown-content'>
            <li v-if="chkResolve"><a href="#reserveconfirm" class="modal-trigger" style="font-size: 13px;">알림요청</a></li> 
            <li v-if="!chkResolve"><a  href="#cancelreserveconfirm" class="modal-trigger" style="font-size: 13px;">알림취소</a></li>             
            <!-- <li ><a href="#view_reservation" class="modal-trigger">예약자보기</a></li>         -->
            <li ><a href="#"  @click="showReserve()" style="font-size: 13px;">요청자보기</a></li>        
    </ul>

    <!-- 화장실 현황 리스트-->
<!-- channel : toilet_noti.channel,
                    nickname : toilet_noti.nickname,
                    send_datetime : toilet_noti.send_datetime, 
                    send_message : toilet_noti.send_message,
                    send_type :toilet_noti.send_type ,
                    sms_phone_number : toilet_noti.sms_phone_number,
                    users_fid : toilet.users_fid    -->

    <!-- <div class="row"> 
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
      </div>
    </div>
  </div> -->

  <!--
  <div class="container" v-if="toilet_possible_yubu">
        <h6>✽ 공개 메세지</h6>
        <div class="container" v-for="toilet_noti in toilet_noties" :key="toilet_noti.id">
            <blockquote>{{toilet_noti.send_message}}</blockquote>
            <div>
                &nbsp;
                <span class="right grey lighten-4 aj-shout-speaker">{{toilet_noti.nickname}} {{toilet_noti.send_datetime}}</span>
            </div>
             <div class="divider" style="margin:5px"></div>
        </div>
  </div> 
  -->

  <!-- <div class="container" style="margin:10px">        
        <div class="container">                         
        </div>
  </div> -->
  
   <div class="row" style="margin:7px;padding:0px 0px 0px 0px"> 
       <div class="col s12" style="margin:0px 0px 0px 0px;padding:0px 0px 0px 0px">
        <!-- <div class="row" style="padding: 0px; margin: 0px;"> -->
            <!-- <div class="col s12" style="padding:0; margin:0"> -->
                <div class="row">  
                    <div class="col s12 m12 l12">
                        <div class="card">           
                                <!-- <div class="grey lighten-5 z-depth-1" style="padding:10px 10px"> -->
                                <!-- <div class="grey lighten-5 z-depth-1" style="padding:10px 10px">
                                    <span class="card-title">Ajoah 챗봇을 이용하세요</span>
                                </div> -->
                                <!-- <div style="margin:0px 0px 0px 10px;padding:10px 0px 0px 30px"> -->
                                <div style="text-align:center">
                                    <span class="card-title">Ajoah 챗봇도 있어요</span>
                                </div>
                                <div class="container" style="text-align:center">        
                                    <hr>
                                </div>
                                <div class="card-panel grey lighten-5 z-depth-0" style="padding: 3px 5px 0px 7px; margin: 2px 0px 0px">                        
                                        <div class="row" style="margin:0px 0px 0px 0px;padding : 0px 0px 0px 0px">                                            
                                            <div class="col s4" style="margin:0px 0px 0px 0px;padding : 0px 0px  0px 10px">
                                                <div class="row valign-wrapper" style="margin:0px;padding:0 0 0px 0">                                                
                                                    <img src="../../img/chatbot_2.png" alt="" style="max-width:90%"> <!-- notice the "circle" class -->                                                
                                                </div>
                                            </div> 
                                            <div class="col s8" style="margin:0px 0px 0px 0px;padding : 0px 0px 0px 5px" >
                                            <ul style="list-style:disc">
                                                <li>· 챗봇으로 더 편리하게 이용</li>
                                                <li>· 빠른 예약 및 실시간 알림</li>
                                                <li>· 공개메시지 발송 가능</li>
                                            </ul>           
                                            </div> 
                                        </div> 
                                        <!-- <div class="row" style="margin:0px 0px 0px 0px; padding : 0px 0px 0px 0px">  -->
                                            <div class="row" style="text-align:center">
                                           <!-- <div class="col s12"  style="margin:0px 0px 0px 0px;padding:0px 10px 20px 80px"> -->
                                               <div class="col s12"  style="padding:0px 10px 15px 00px">
                                               <span class="black-text align-center" >
                                                    <a class="waves-effect indigo btn-small" href="https://t.me/ajoah_bot" target="_blank">
                                                    <i class="medium material-icons right">send</i>챗봇 바로가기</a> 
                                                </span>
                                            </div>             
                                        </div>     
                                </div>                
                        </div>
                    </div>
                </div>   
         </div>
     </div>     
    </div> <!-- end of container -->  
    
     <!-- [3] Index Vue Footer-->
     <footer class="page-footer">
          <div class="container">
            <div class="row">
              <div class="col l6 s12">
                <h6 class="white-text">Ajoah는 쾌적한 화장실 이용을 응원합니다!</h6>                
                 
                <!-- <p class="white-text text-lighten-4">화장실을 스마트하게 사용해 보세요.</p> -->
                <!-- <a href="https://t.me/ajoah_bot" class="white-text text-lighten-4" target="_blank">텔레그램봇 바로가기</a> -->
              </div>
              <!-- <div class="col l4 offset-l2 s12">                
                <ul>
                  <li><a href="https://t.me/ajoah_bot" class="grey-text text-lighten-3" target="_blank" cursor="hand">텔레그램봇 바로가기</a></li>                  
                </ul>
              </div> -->
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
            <p  style="font-size:15px">{{toilet_selected_nm}} 빈칸알림 신청하시겠습니까?</p>
        </div>
        <div class="modal-footer">
            <a href="#!" class="modal-close waves-effect waves-green btn-flat">취소</a>
            <a class="modal-close waves-effect waves-green btn-flat" @click="DoReserve()">확인</a>
            <!-- <a class="modal-close btn orange" @click="ChkTest()">확인2</a> -->
        </div>
    </div>
    <!-- 예약하기 전 Confirm 확인창 Modal-->

    <div id="cancelreserveconfirm" class="modal">
        <div class="modal-content">
             <p  style="font-size:15px">{{toilet_selected_nm}} 빈칸알림 취소하시겠습니까?</p>
        </div>
        <div class="modal-footer">
            <a href="#!" class="modal-close waves-effect waves-green btn-flat">취소</a>
            <a class="modal-close waves-effect waves-green btn-flat" @click="cancelReserve()">확인</a>
            <!-- <a class="modal-close btn orange" @click="ChkTest()">확인2</a> -->
        </div>
    </div>

    
   <!-- 예약자보기 하단 모달 -->
    <div id="view_reservation" class="modal bottom-sheet" >        
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
import { setInterval } from 'timers';
window.$ = window.jQuery = window.jquery = require('jquery')
//import $ from 'jquery'

// 참조 오브젝트 초기화
var tmpObj = {};
var tmpGroupObj = {};

// localStorage
var localStorage = window.localStorage;
const STR_KEY_SELECT_VALUE = "key_select_value";

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
      chkResolve : true,
      toilet_possible_yubu : true,
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
        let vm = this        
        vm.$router.push({name:'Login'})
        // window.location.reload();
      }  
    })
        
  },
  mounted(){
    
    $(document).ready(function(){
        $('select').formSelect();
    });

    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('select');
        var instances = M.FormSelect.init(elems,  {
                classes: '',
                dropdownOptions: {}
            });
    });

    // var instance = M.FormSelect.getInstance(elems);

    $(document).ready(function() {
        $('.modal').modal();
    });

    // $(document).ready(function() {
    //     $('input#icon_prefix, input#icon_telephone, input#icon_verification_no, input#solution').characterCounter();
    // });

    // $(document).ready(function() {
    //     $('.collapsible').collapsible();
    // });
   

    $('.dropdown-trigger').dropdown();
    
    // document.addEventListener('DOMContentLoaded', function() {
    //     var elems = document.querySelectorAll('.dropdown-trigger');
    //     var instances = M.Dropdown.init(elems, {
    //         alignment: 'left',
    //         autoTrigger: true
    //     });
    // });
    
    var target = document.getElementById("toilet_select");
    
    // 로컬 스토리지에 선택정보 저장 유무 확인
    console.log("# MOUNTED #");
    let savedSelectedItem = localStorage.getItem(STR_KEY_SELECT_VALUE);
    if(savedSelectedItem == null)
        localStorage.setItem(STR_KEY_SELECT_VALUE, target.options[target.selectedIndex].value);
    
    console.log(savedSelectedItem);
    
    var opts = target.options;

    for(var opt, j = 0; opt = opts[j]; j++) {
        if(opt.value == savedSelectedItem) {
            target.selectedIndex = j;
            break;
        }
    }

    var target_value = target.options[target.selectedIndex].value;
    var target_name = target.options[target.selectedIndex].text;



    this.toilet_selected_val = target_value; 
    this.toilet_selected_nm = target_name;    

    let ref = db.collection("current")  
    
    console.log("mounted");

    tmpGroupObj = {};
    tmpObj = {};

    // subscribe to changes to the 'messages' collection
    ref.onSnapshot(snapshot => {
      snapshot.docChanges().forEach(change => {
        console.log("###################################");
        console.log(change.type);
        console.log("###################################");
        if (change.type === "added") {
                
                let toilet_current = change.doc.data()                    

                // usage컬럼 추가
                toilet_current.usage = 0;
                toilet_current.elapsedTime = "";

                // 참조 오브젝트에 화장실 정보 맵핑                
                tmpObj[toilet_current.id] = toilet_current;

                if(tmpGroupObj[toilet_current.group] == null){

                    tmpGroupObj[toilet_current.group] = [];                    
                }

                tmpGroupObj[toilet_current.group].push(toilet_current);

                //  console.log("change.doc.data() =" + change.doc.data());
                //  console.log("toilet_current = " + toilet_current.id);
                //  console.log("tmpObj = " + tmpObj[toilet_current.id].id);
                //  console.log("toilet_current.group = " + toilet_current.group);
                //  console.log("tmpGroupObj = " + tmpGroupObj[toilet_current.group].id);               
        }

        if (change.type === "modified") {
                console.log("modified : ", change.doc.data());
                // console.log("Modified city: ", change.doc.data().id);

                // 변경된 오브젝트만 새로 맵핑
                var keySet = Object.keys(change.doc.data());
                var modifiedObj = change.doc.data();
                
                keySet.forEach(key => {
                    if(tmpObj[modifiedObj.id][key] != modifiedObj[key])
                        tmpObj[modifiedObj.id][key] = modifiedObj[key];
                });
                

                // var found = toilet_currents.find(function(change.doc.data().id) {
                //   return change.doc.data().id;
                // });

             //this.toilet_currents.splice(0);      
             //this.doJohoi();    
        }
      })
    this.chkReserve();
    this.doJohoi();
    this.doDrawToilet();

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
    // this.showReserve();
    this.showNoties();
  },
  methods: {

        onChange(event) {
            console.log(" # INIT CHANGE # ");
            this.showPreloader = true;
             // toilet_currents 초기화
            // this.toilet_currents.splice(0);                     
            // console.log(event.target.value)
            this.doDrawToilet();

            var target = document.getElementById("toilet_select");
            localStorage.setItem(STR_KEY_SELECT_VALUE, target.options[target.selectedIndex].value);
            
            // this.doJohoi();             
                                                                            
        },
        doDrawToilet(){
            var target = document.getElementById("toilet_select");
        
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;
            
            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;            

            this.toilet_currents_state.splice(0);

            console.log("# DO DRAW TOILET #");
            console.log(tmpGroupObj);

            if(tmpGroupObj[this.toilet_selected_val] == null){ 
                this.toilet_possible_yubu = false
                //M.toast({html: '해당 화장실은 아직 지원하지 않습니다.', classes: 'rounded'})
            }else
            {
                this.toilet_possible_yubu = true

                // 연호8층 선택시에 연호빌딩 남자화장실을 다 보여준다.(7층,8층) , 2019.12.19 정종현 선임 요청
                // if(this.toilet_selected_val == "Y8.M"){
                    
                //     tmpGroupObj[this.toilet_selected_val].forEach(childObject => {
                //     this.toilet_currents_state.push(childObject);
                //     });

                //     tmpGroupObj["Y7.M"].forEach(childObject => {
                //     this.toilet_currents_state.push(childObject);
                //     });

                // }else if(this.toilet_selected_val == "B17.M"){

                //     tmpGroupObj[this.toilet_selected_val].forEach(childObject => {
                //     this.toilet_currents_state.push(childObject);
                //     });

                //     tmpGroupObj["B18.M"].forEach(childObject => {
                //     this.toilet_currents_state.push(childObject);
                //     });

                // }else{

                //     tmpGroupObj[this.toilet_selected_val].forEach(childObject => {
                //     this.toilet_currents_state.push(childObject);
                //     });    

                // }

                    tmpGroupObj[this.toilet_selected_val].forEach(childObject => {
                    this.toilet_currents_state.push(childObject);
                    });  
                
            }
        }, 
        doJohoi(){
             
            var date = new Date();


            var today = moment().format("YYYY-MM-DD");

            console.log("today ==> " + today)

            //let ref = db.collection('statics').doc("usage");
            let ref = db.collection('statics').doc(today); 
                      
            ref.get().then(doc => {  
            if(doc.exists){                                 
                let toilet_current_static = doc.data()
 
                //console.log("test===>"+toilet_current_static);
                // this.toilet_current_statics.push(toilet_current_static);
                // 변경된 오브젝트만 새로 맵핑
                var keySet = Object.keys(toilet_current_static[today]);
                
                console.log("# START #");
                keySet.forEach(key => {
                    if(tmpObj[key] != null) 
                        tmpObj[key].usage = toilet_current_static[today][key];


                });
                console.log("# END #");


            }else{                                            


            }
            })

        },
        showReserve(){
                        
            // toilet_reserves 초기화
            this.toilet_reserves.splice(0);

            var target = document.getElementById("toilet_select");
            var target_value = target.options[target.selectedIndex].value;
            var target_name = target.options[target.selectedIndex].text;           
            
            this.toilet_selected_val = target_value; 
            this.toilet_selected_nm = target_name;    
            // db.collection("reservation").where("location","==",this.toilet_selected_val).orderBy("resv_dttm", "desc").get()

            let cnt = 0
            console.log("this.toilet_selected_val = " + this.toilet_selected_val)
            db.collection("reservation").where("location","==",this.toilet_selected_val).get()
                    .then(snapshot => {
                this.toilet_reserves_cnt = snapshot.size   
                //alert(snapshot.size)                             
                //if(this.toilet_reserves_cnt < 1) M.toast({html: '예약자가 없습니다. 지금 가세요~!', classes: 'rounded'}); return; 

                snapshot.forEach(doc => {
                let toilet_reserve = doc.data()                
                console.log("sjs ===> toilet_reserve = " + doc.data().nickname)                                 
                this.toilet_reserves.push({
                    location : toilet_reserve.location, 
                    nickname : toilet_reserve.nickname,
                    phone_num : toilet_reserve.phone_num, 
                    resv_channel : toilet_reserve.resv_channel,
                    resv_dttm : moment(toilet_reserve.resv_dttm).format("MM/DD HH:mm") ,
                    seq : toilet_reserve.seq   
                    }) 
                
                cnt = cnt + 1;
                console.log("this.cnt2 = " + cnt)
                })
                
                if(cnt == 0){
                   
                   M.toast({html: '예약자가 없습니다. 지금 가세요~!', classes: 'rounded'}); return;

                }else{
                  
                    var elem= document.querySelector('#view_reservation');
                    var instance = M.Modal.init(elem);
                    instance.open();

                }
                
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

                let mt = moment(toilet_noti.send_datetime, "YYYY-MM-DD hh:mm:ss");



                if(cnt < 5){
                    this.toilet_noties.push({
                        channel : toilet_noti.channel,
                        nickname : toilet_noti.nickname,
                        send_datetime : mt.format("MM/DD HH:mm"), 
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
        chkReserve(){
            
            var user = firebase.auth().currentUser;          
            let phoneNumber = firebase.auth().currentUser.phoneNumber;

            console.log("phoneNumber = " + phoneNumber);

            let ref = db.collection('reservation').doc(phoneNumber)
                            
            ref.get().then(doc => {

            if(doc.exists){                
                    this.chkResolve = false                                                                                
            }else{                                   
                    this.chkResolve = true
            }

            console.log("this.chkResolve : " + this.chkResolve)
            })                                                
           
        },
        cancelReserve(){
             
            var user = firebase.auth().currentUser;          
            let phoneNumber = firebase.auth().currentUser.phoneNumber;

            console.log("phoneNumber = " + phoneNumber);

            let ref = db.collection('reservation').doc(phoneNumber)
                            
            ref.delete().then(doc => { 
                console.log("Document successfully deleted!");
                M.toast({html: '예약 취소 되었습니다.', classes: 'rounded'})                 
                this.chkResolve = true  
            }).catch(function(error) { 
                console.error("Error removing document: ", error);
                 this.chkResolve = false  
            });      
           
        },
        DoReserve(){
            
            db.collection("current").where("group","==",this.toilet_selected_val).where("using","==",false).get()
                    .then(snapshot => {                
                this.toilet_current_using_state = snapshot.size
                
                // test 임시 로직
                // this.toilet_current_using_state = 0;

                if(this.toilet_current_using_state > 0){
                    M.toast({html: '지금 화장실이 비어있어요. 바로 달려가세요~', classes: 'rounded'})
                    return;
                }
                else
                {
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
        
                            db.collection('reservation').doc(phoneNumber).set({
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
                            this.chkResolve = false
                            // this.chkReserve();
                        })
        
                        

                    }else{            
                        
                        alert('회원가입이 되어 있지 않습니다.');                

                    }
                    })                    
                }
            })
           
        }
    }
    
}

function calcElapsedTime()
{
    for(var key in tmpObj)
    {   
        let mt = moment(tmpObj[key].using_from, "YYYY-MM-DD hh:mm:ss");

        if(tmpObj[key].using == true && tmpObj[key].using_from != null){
            tmpObj[key].elapsedTime = elapsedTimeStr(mt.unix());
        }else{
            tmpObj[key].elapsedTime = '' 
        }    
    }
}
 
function elapsedTimeStr(timestamp)
{
    if(timestamp == null) return "X";
    let timestamp_milli = timestamp.toString().length == 10 ? timestamp * 1000 : timestamp;
    let elapsed_sec = parseInt((new Date().getTime() - timestamp_milli) / 1000);
    let timeStr = "";

    if (elapsed_sec < 60) {
        timeStr = '방금 전';
    }
    else if (elapsed_sec < 60 * 60) {
        timeStr = parseInt(elapsed_sec / 60) + '분 경과';
    }
    else if (elapsed_sec < 60 * 60 * 24) {
        timeStr = parseInt(elapsed_sec / 60 / 60) + '시간 경과';
    } 
    else {
        timeStr = '하루 이상 경과';
    }

    return timeStr;
}

setInterval(calcElapsedTime, 1000);



document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
        direction: 'top'        
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, { 
        opacity: 0.5             
    });
});



</script>

<style>

</style>

