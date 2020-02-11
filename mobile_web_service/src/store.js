/* store.js */
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