import Vue from 'vue'
import wwwwwww from '@/package/echartsmap/echartsmap.vue'
import router from '@/router/echartsmap.router'
//import router from '@/router/wechat.router'
//import router from '@/router/index.router'
import * as echarts from 'echarts';
Vue.prototype.$echarts = echarts
//import '@/assets/js/china.js';
//import '@/assets/js/fujian.js';


import axios from 'axios'
import VueAxios from 'vue-axios'
import vuex from 'vue'
import store from '@/vuex/store'
import FastClick from 'fastclick' //使用 fastclick 解决移动端 300ms 点击延迟

Vue.use(VueAxios, axios, vuex, echarts)
// 注册全局过滤器


Vue.config.productionTip = false //将此值设置为 false ,会关闭 Vue 启动时的提示信息，推荐

FastClick.attach(document.body)

new Vue({
  router,
  store,
  render: h => h(wwwwwww)
}).$mount("#rrrr")


//new Vue({
//    //el: '#wechat',
//    router,
//    store,
//    render: h => h(wechat)
//}).$mount("#wechat")
// 运行 vue init webpack命令新建项目时 可以选择关闭 ESLint
// 若新建项目时开启了 ESLint .eslintignore 文件，告诉 ESLint 去忽略特定的文件和目录。
// .eslintignore 文件是一个纯文本文件，其中的每一行都是一个 glob 模式表明哪些路径应该忽略检测