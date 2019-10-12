<template>
 <div class="index container">    
     
     <!-- [1] 화장실 선택 Select Box-->      
     <div class="container">
      <div class="row" style="margin-bottom: 0px">            
        <div class="input-field col s6 left">
            <select @change="onChange($event)">
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
    </div>      
    <!-- 화장실 선택 Select Box-->       


    <!-- [2] 화장실 현황 리스트-->

    <div class="container">
        <div class="row" >             
            <div class="col s12 l12">
                    <span class="card-title right">10초 후 자동 새로고침</span>
            </div> 
        </div> 
    </div> 

     <div class="container">
        <!-- <h2>연호 8층</h2> --> 
        <div class="row" >             
            <div class="col s12 l6" v-for="toilet_current in toilet_currents" :key="toilet_current.id">
                <div class="card">
                    <div class="card-image">
                        <img src="../img/toilet.jpg" alt="">
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
    <div class="container" v-if="show">
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
    </div>
    <!-- Index Vue Footer-->

    <!-- 예약하기 전 Confirm 확인창 Modal-->
    <div id="reserveconfirm" class="modal">
        <div class="modal-content">
            <h6>화장실 예약하시겠습니까?</h6>
        </div>
        <div class="modal-footer">
            <a href="#!" class="modal-close btn orange">취소</a>
            <a href="#reserve" class="modal-close btn orange modal-trigger">확인</a>
        </div>
    </div>
    <!-- 예약하기 전 Confirm 확인창 Modal-->

    <!-- 예약하기 창 Modal-->
    <div id="reserve" class="modal">
        <div class="modal-content">            
            <div class="row">
                <form class="col s12">
                    <div class="row">
                        <div class="input-field col s12">
                            <i class="material-icons prefix">account_circle</i>
                            <input id="icon_prefix" type="text" class="validate" data-length="20" v-model="nickname">
                            <label for="icon_prefix">이름(별명)</label>
                            <span class="helper-text" data-error="wrong" data-success="right">이름(별명)입력해 주세요</span>
                        </div>
                    </div>
                    <div class="row ">
                        <div class="input-field col s12 ">
                            <i class="material-icons prefix">phone</i>
                            <input id="icon_telephone" type="tel" class="validate" data-length="12" v-model="phone_num">
                            <label for="icon_telephone">핸드폰번호</label>
                            <span class="helper-text" data-error="wrong" data-success="right">- 빼고 숫자만 입력</span>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s6">
                            <i class="material-icons prefix">mode_edit</i>
                            <input id="icon_verification_no" type="text" class="validate" data-length="6">
                            <label for="icon_verification_no">인증번호</label>
                            <span class="helper-text " data-error="wrong" data-success="right"></span>
                        </div>
                        <div class="input-field col s6">
                            <div class="btn">
                                <span>인증번호받기</span>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <a href="#!" class="modal-close btn orange">취소</a>
                        <a href="#!" class="modal-close btn orange" @click="DoReserve()">예약</a>
                    </div>
                    <p v-if="feedback" class="red-text">{{ feedback }}</p>
                </form> 
            </div>
        </div>
    </div>
    <!-- 예약하기 창 Modal-->

    <!-- AJOAH 최초 인증하기 Modal -->
    <div id="verify" class="modal">
        <div class="modal-content">
           <div class="row">
                <div class="row">
                    <div class="col s12 m6">
                        <div class="card blue-grey darken-1">
                            <div class="card-content white-text">                                
                                <h6>- 인증필요</h6>
                                <p>AJOAH 서비스를 사용하려면 인증이 필요합니다.</p>
                            </div>
                            <div class="card-content white-text">                                
                                <h6>- 인증질문</h6>
                                <p>AJOAH 만든이 3명의 중간글자를 입력하세요.<br/>(힌트 : 송*수, 윤*민, 정*현)</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <form class="col s12">
                        <div class="row">
                            <div class="input-field col s12">
                                <input placeholder="답변을 입력해 주세요" id="solution" type="text" class="validate" data-length="3">
                                <label for="solution">인증답변</label>
                                <span class="helper-text " data-error="wrong" data-success="right"></span>
                            </div>
                        </div>

                        <div class="modal-footer ">
                            <a href="#! " class="modal-close btn orange ">취소</a>
                            <a href="#! " class="modal-close btn orange " onclick="M.toast({html: '인증 신청 되었습니다.', classes: 'rounded', completeCallback: function(){alert( '인증 성공 되었습니다.')}}) ">인증하기</a>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    </div>
    <!-- AJOAH 최초 인증하기 Modal -->


    <!-- About Modal -->
    <div id="about" class="modal ">
        <div class="modal-content ">
            <h6>Another Joy Of Ah~~~!</h6>
        </div>
        <div class="modal-footer ">
            <a href="#! " class="modal-close btn orange ">확인</a>
        </div>
    </div>
    <!-- About Modal -->

    <!-- Contact Modal -->
    <div id="contact" class="modal ">
        <div class="modal-content ">
            <h6>송준수, 윤경민, 정종현</h6>
        </div>
        <div class="modal-footer ">
            <a href="#! " class="modal-close btn orange ">확인</a>
        </div>
    </div>
    <!-- Contact Modal -->

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
    <div class="fixed-action-btn">
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
    </div> 
    <!-- Floating Button Menu 버튼 -->

  </div>
</template>

<script>
import db from '@/firebase/init_firestore'
import moment from 'moment'

export default {
  name: 'Index',
  data(){
    return{
      toilet_currents : [],
      toilet_reserves : [],
      nickname: null,
      phone_num : null,
      feedback: null,
      show: false,      
      
    }
  },
  created(){     
    db.collection("current").where("group","==","Y8.M").get()    
    .then(snapshot => {
      snapshot.forEach(doc => {
        let toilet_current = doc.data()        
        console.table(doc.data())
        this.toilet_currents.push(toilet_current)   
      })
    })
  },
  mounted(){
        
        this.show = true;

  },
  methods: {
        onChange(event) {            
            // toilet_currents 초기화
            this.toilet_currents.splice(0);
                       
            console.log(event.target.value)
            db.collection("current").where("group","==",event.target.value).get()    
                    .then(snapshot => {
                snapshot.forEach(doc => {
                let toilet_current = doc.data()        
                //console.table(doc.data())                
                this.toilet_currents.push(toilet_current)   
            })
            })            
            this.show = false;
        },
        showReserve(){
            
            // this.toilet_reserves.push({
            //     id: doc.id,
            //     gender: doc.data().gender,
            //     nickname: doc.data().nickname,
            //     resv_channelamp: doc.data().resv_channel,
            //     resv_dttm : moment(doc.data().resv_dttm).format('lll'),
            // })

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
            // location : Y8.01
            // nickname : JUN SOO 
            // phone_num : 01077778888
            // resv_channel : MobileWeb
            // resv_dttm : timestamp
            // seq : 1
            // telegram_id : "1111111111"

            if(this.nickname && this.phone_num){
                db.collection('reservation').add({
                    location: "Y8.M",
                    nickname: this.nickname,
                    phone_num : this.phone_num,
                    resv_channel : "MobileWeb",
                    resv_dttm: Date.now()
                }).catch(err => {
                console.log(err)
                })
                this.nickname = null
                this.phone_num = null
                this.feedback = null
            } else {
                this.feedback = 'You must enter a message in order to send one'
            }

            M.toast({html: '예약 신청 되었습니다.', classes: 'rounded', completeCallback: function(){alert( '예약이 완료되었습니다.')}})
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
