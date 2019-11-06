<template>
  <div id="app">
      <Navbar :select_view="select_view"></Navbar>      
      <router-view ></router-view>
  </div>
</template>

<script>

import Navbar from '@/components/layout/Navbar'
import firebase from 'firebase'
import Vue from 'vue'
import Vuex from 'vuex'
 
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        select_view: false
    },
    mutations: {
        select_view_true(state) {
            state.select_view = true
        },
        select_view_false(state) {
            state.select_view = false
        }
    }
})

export default {
  store,
  name: 'App',
  data(){
    return {
        select_view : false,         
    }
  },
  mounted(){

    // document.addEventListener('DOMContentLoaded', function() {
    //     var elems = document.querySelectorAll('select');
    //     var instances = M.FormSelect.init(elems,  {
    //             classes: '',
    //             dropdownOptions: {}
    //         });
    // });    
  },
  props:['user'],
  components: {
    Navbar    
  }  
}
</script>

<style>

</style>
