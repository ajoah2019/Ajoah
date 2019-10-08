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
                    <li><a href="#view_reservation" class="modal-trigger">예약자보기</a></li>
                    <li><a href="#reserve" class="modal-trigger">예약하기</a></li>
                    <li><a href="#about" class="modal-trigger">About</a></li>
                    <li><a href="#contact" class="modal-trigger">Contact</a></li>

                </ul>
            </div>
        </nav>
    </div>

    <ul class="sidenav" id="mobile-links">
        <li><a href="#view_reservation" class="modal-trigger">예약자보기</a></li>
        <li><a href="#reserve" class="modal-trigger">예약하기</a></li>
        <li><a href="#about" class="modal-trigger">About</a></li>
        <li><a href="#contact" class="modal-trigger">Contact</a></li>
    </ul>


    <!-- 예약하기 확인창 Modal Structure -->
    <div id="reserveconfirm" class="modal">
        <div class="modal-content">
            <h6>화장실 예약하시겠습니까?</h6>
        </div>
        <div class="modal-footer">
            <a href="#!" class="modal-close btn orange">취소</a>
            <a href="#reserve" class="modal-close btn orange modal-trigger">확인</a>
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
                        <a href="#!" class="modal-close btn orange">취소</a>
                        <a href="#!" class="modal-close btn orange" onclick="M.toast({html: '예약 신청 되었습니다.', classes: 'rounded', completeCallback: function(){alert( '예약이 완료되었습니다.')}}) ">예약</a>
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
                            <a href="#! " class="modal-close btn orange">취소</a>
                            <a href="#! " class="modal-close btn orange" onclick="M.toast({html: '인증 신청 되었습니다.', classes: 'rounded', completeCallback: function(){alert( '인증 성공 되었습니다.')}}) ">인증하기</a>
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
            <a href="#! " class="modal-close btn orange">확인</a>
        </div>
    </div>
    <!-- About Modal Structure -->

    <!-- Contact Modal Structure -->
    <div id="contact" class="modal ">
        <div class="modal-content ">
            <h6>송준수, 윤경민, 정종현</h6>
        </div>
        <div class="modal-footer ">
            <a href="#! " class="modal-close btn orange">확인</a>
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

</div>
</template>

<script>
export default {
  name: 'Navbar',
  data(){
    return {

    }
  }
}
</script>

<style>

</style>

