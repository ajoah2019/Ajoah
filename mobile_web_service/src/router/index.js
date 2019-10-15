import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/home/Index'
import Signup from '@/components/auth/Signup'
import setPassword from '@/components/auth/setPassword'
import Login from '@/components/auth/Login'
import ViewProfile from '@/components/profile/ViewProfile'

Vue.use(Router)

const router = new Router({
    routes: [{
            path: '/',
            name: 'Login',
            component: Login
        },
        {
            path: '/signup',
            name: 'Signup',
            component: Signup
        },
        {
            path: '/main',
            name: 'Index',
            component: Index
        },
        {
            path: '/setPassword',
            name: 'SetPassword',
            component: setPassword
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/profile/:id',
            name: 'ViewProfile',
            component: ViewProfile,
        }
    ]
})

export default router