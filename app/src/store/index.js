import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        theme: 'light'
    },
    actions: {
        changeTheme({commit}, value) {
            commit('CHANGETHEME', value)
        }
    },
    mutations: {
        CHANGETHEME (state, value) {
            state.theme = value
        }
    }
})