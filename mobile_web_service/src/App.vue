<template>
  <div id="app">
      <Navbar :user="user"></Navbar>      
      <router-view :user="user"></router-view>
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar'
import firebase from 'firebase'
 
export default {
  name: 'App',
  props:['user'],
  components: {
    Navbar
  }
}
</script>

<style>

</style>
