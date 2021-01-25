// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AAAAAA from '@/package/bookapi/bookapi.vue'
//import router from '@/router'
import router from '@/router/index.router'

import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
//import 'element-ui/lib/theme-default/index.css'
import 'element-ui/lib/theme-chalk/index.css'
Vue.config.productionTip = false
import store from '@/vuex/store'

Vue.use(ElementUI)
Vue.use(VueResource)

/* eslint-disable no-new */


// vue有两种形式的代码 compiler（模板）模式和runtime模式（运行时）,以下模式是compiler
//https://blog.csdn.net/wxl1555/article/details/83187647
//new Vue({
//  el: '#app',
//  router,
//  template: '<App/>',
//  components: { App }
//})

//runtime
//import store from '../src/vuex/store'
new Vue({
  router,
  store,
  render: h => h(AAAAAA)
}).$mount("#aaaa")
