import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/home/Index'
import serviceIntro from '@/components/home/serviceIntro'
import Signup_1 from '@/components/auth/Signup_1'
import Signup from '@/components/auth/Signup'
import setPassword from '@/components/auth/setPassword'
import setProfile from '@/components/auth/setProfile'
import Login from '@/components/auth/Login'
import ViewProfile from '@/components/profile/ViewProfile'

Vue.use(Router)

const router = new Router({
    routes: [{
            path: '/',
            name: 'serviceIntro',
            component: serviceIntro
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/signup',
            name: 'Signup',
            component: Signup
        },
        {
            path: '/signup_1',
            name: 'Signup_1',
            component: Signup_1
        },
        {
            path: '/index',
            name: 'Index',
            component: Index
        },
        {
            path: '/setPassword',
            name: 'SetPassword',
            component: setPassword
        },
        {
            path: '/setProfile', 
            name: 'SetProfile',
            component: setProfile
        },
        {
            path: '/profile/:id',
            name: 'ViewProfile',
            component: ViewProfile,
        }
    ]
})

export default router