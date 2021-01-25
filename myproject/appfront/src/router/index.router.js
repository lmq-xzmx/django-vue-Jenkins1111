import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

const routes = [
    {
      path: '/',
      name: 'Home',
      component: Home
      //component: resolve => require(["../components/Home.vue"], resolve)
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
      //component: resolve => require(["../components/HelloWorld.vue"], resolve)
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home
      //component: resolve => require(["../components/Home.vue"], resolve)
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
