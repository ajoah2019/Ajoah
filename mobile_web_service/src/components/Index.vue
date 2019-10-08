<template>
 <div class="index container">    
     <!-- 화장실 선택 Select Box-->
      
      <div class="row" style="margin-bottom: 0px">            
        <div class="input-field col s6 left">
            <select>
              <optgroup label="연호빌딩 8층">
              <option value="Y8-M">연호8층 남자</option>
              <option value="Y8-F">연호8층 여자</option>
              </optgroup>
              <optgroup label="연호빌딩 7층">
              <option value="Y7-M">연호7층 남자</option>
              <option value="Y7-F">연호7층 여자</option>
              </optgroup>
           </select>
        </div>            
      </div>

      <div class="container">
        <!-- <h2>연호 8층</h2> -->
        <div class="row" >
             <div class="col s12 l12">
                <span class="card-title right">10초 후 자동 새로고침</span>
            </div>
            <div class="col s12 l6">
                <div class="card hoverable" v-for="toilet_current in toilet_currents" :key="toilet_current.id">
                    <div class="card-image">
                        <img src="../img/toilet.jpg" alt="">
                        <a href="" class="halfway-fab btn-floating red pulse" v-if="toilet_current.using == 'true'" >
                            <i class="material-icons">clear</i>                            
                        </a>
                        <a href="" class="halfway-fab btn-floating yellow pulse" v-else>
                            <i class="material-icons">sentiment_satisfied_alt</i>
                        </a>                        
                    </div>
                    <div class="card-content">
                        <span class="card-title">{{toilet_current.name}}</span>
                        <!-- <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean quis aliquam orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p> -->
                         <span class="badge white-text pink" v-if="toilet_current.using == 'true'">사용중</span>
                         <span class="badge black-text yellow pulse" v-else>비었음</span>                         
                    </div>
                    <!-- <div class="divider black-text"></div>
                    <div class="card-action">
                        <a href="">3분 경과</a>
                        <a href="">오늘 3명 이용</a>
                    </div> -->
                </div>
            </div>            
        </div>
     </div> 

    <div class="container">
    <div class="row" >
     <div class="col s12 l12">
        <nav class="nav-extended">
            <div class="nav-wrapper"> 
            <a href="#!" class="brand-logo">3명 예약중</a>      
            </div>
            <div class="nav-content">
            <!-- <span class="nav-title">Title</span> -->
            <a class="btn-floating btn-large halfway-fab waves-effect waves-light teal left modal-trigger" href="#view_reservation">
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


    <!-- 예약하기 확인창 Modal Structure -->
    <div id="reserveconfirm" class="modal">
        <div class="modal-content">
            <h6>화장실 예약하시겠습니까?</h6>
        </div>
        <div class="modal-footer">
            <a href="#!" class="modal-close waves-effect waves-green btn-flat">취소</a>
            <a href="#reserve" class="modal-close waves-effect waves-green btn-flat modal-trigger">확인</a>
        </div>
    </div>
        
    <div id="reserve" class="modal">
        <div class="modal-content">            
            <div class="row">
                <form class="col s12">
                    <div class="row">
                        <div class="input-field col s12">
                            <i class="material-icons prefix">account_circle</i>
                            <input id="icon_prefix" type="text" class="validate" data-length="20">
                            <label for="icon_prefix">이름(별명)</label>
                            <span class="helper-text" data-error="wrong" data-success="right">이름(별명)입력해 주세요</span>
                        </div>
                    </div>
                    <div class="row ">
                        <div class="input-field col s12 ">
                            <i class="material-icons prefix">phone</i>
                            <input id="icon_telephone" type="tel" class="validate" data-length="12">
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
                        <a href="#!" class="modal-close waves-effect waves-green btn-flat">취소</a>
                        <a href="#!" class="modal-close waves-effect waves-green btn-flat" onclick="M.toast({html: '예약 신청 되었습니다.', classes: 'rounded', completeCallback: function(){alert( '예약이 완료되었습니다.')}}) ">예약</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <!-- 예약하기 Modal Structure -->

    <!-- 인증하기 Modal Structure -->
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
                            <a href="#! " class="modal-close waves-effect waves-green btn-flat ">취소</a>
                            <a href="#! " class="modal-close waves-effect waves-green btn-flat " onclick="M.toast({html: '인증 신청 되었습니다.', classes: 'rounded', completeCallback: function(){alert( '인증 성공 되었습니다.')}}) ">인증하기</a>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    </div>
    <!-- 인증하기 Modal Structure -->


    <!-- About Modal Structure -->
    <div id="about" class="modal ">
        <div class="modal-content ">
            <h6>Another Joy Of Ah~~~!</h6>
        </div>
        <div class="modal-footer ">
            <a href="#! " class="modal-close waves-effect waves-green btn-flat ">확인</a>
        </div>
    </div>
    <!-- About Modal Structure -->

    <!-- Contact Modal Structure -->
    <div id="contact" class="modal ">
        <div class="modal-content ">
            <h6>송준수, 윤경민, 정종현</h6>
        </div>
        <div class="modal-footer ">
            <a href="#! " class="modal-close waves-effect waves-green btn-flat ">확인</a>
        </div>
    </div>
    <!-- Contact Modal Structure -->


   <!-- 예약자보기 - materizecss 샘플 하단 모달 -->
    <div id="view_reservation" class="modal bottom-sheet">
        <!-- <h2>Collections</h2> -->
        <ul class="collection with-header">
            <li class="collection-header">
                <h4>Subscribers</h4>
            </li>
            <li class="collection-item avatar">
                <i class="material-icons circle blue">person</i>
                <span class="title">Ryu</span>
                <p class="grey-text">black-belt</p>
                <!-- <a href="" class="secondary-content">
                    <i class="material-icons light-blue-text">email</i>
                </a> -->
            </li>
            <li class="collection-item avatar">
                <i class="material-icons circle pink">person</i>
                <span class="title">Yoshi</span>
                <p class="grey-text">orange-belt</p>
                <!-- <a href="" class="secondary-content">
                    <i class="material-icons light-blue-text">email</i>
                </a> -->
            </li>
            <li class="collection-item avatar">
                <i class="material-icons circle blue">person</i>
                <span class="title">Crystal</span>
                <p class="grey-text">brown-belt</p>
                <!-- <a href="" class="secondary-content">
                    <i class="material-icons light-blue-text">email</i>
                </a> -->
            </li>
            <li class="collection-item">Mario</li>
            <li class="collection-item">Luigi</li>
            <li class="collection-item">Bowser</li>
        </ul>
    </div>
       
    <div class="fixed-action-btn">
        <a class="btn-floating btn-large red">
            <i class="large material-icons">mode_edit</i>
        </a> 
        <ul>
            <li><a class="btn-floating red modal-trigger" href="#verify"><i class="material-icons">insert_chart</i></a></li>
            <li><a class="btn-floating yellow darken-1 modal-trigger" href="#reserve"><i class="material-icons">format_quote</i></a></li>
            <li><a class="btn-floating green modal-trigger" href="#view_reservation"><i class="material-icons">publish</i></a></li>
            <li><a class="btn-floating blue modal-trigger" href="#about"><i class="material-icons">attach_file</i></a></li>
        </ul>
    </div> 

  </div>
</template>

<script>
import db from '@/firebase/init_firestore'

export default {
  name: 'Index',
  data(){
    return{
      toilet_currents : [],      
      
    }
  },
  created(){
    // fetch data from firestore
    db.collection('current').get()
    .then(snapshot => {
      snapshot.forEach(doc => {
        let toilet_current = doc.data()        
        this.toilet_currents.push(toilet_current)   
      })
    })
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
