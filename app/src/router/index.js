import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes.js'
import {getCookie} from '../utils/cookie'
Vue.use(VueRouter)

const router = new VueRouter({
    routes
})

// 全局前置守卫
router.beforeEach((to, from, next) => {   
    const cookie = getCookie('xmut')
    if (cookie) {
        next()
    } else {
        if (to.path == '/login') {
            next()
        } else {
            next({path: '/login'})
        }
    }
})

export default router