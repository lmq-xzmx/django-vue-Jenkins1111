import Vue from 'vue'
import Router from 'vue-router'

import map  from '@/components/map/map'


Vue.use(Router)

const routes = [
    {
        path: '/',
        name: "map",
		component: map
        //component: resolve => require(["@/components/wechat/wechat.vue"], resolve)
    }
    
]
export default new Router({
    //base: "/vue-wechat/",
    routes,
    // scrollBehavior(to, from, savedPosition) {
    //     if (savedPosition) {
    //         return savedPosition
    //     } else {
    //         return { x: 0, y: 0 }
    //     }
    // }

})
