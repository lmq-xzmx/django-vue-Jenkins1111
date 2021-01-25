import Vue from 'vue'
import KKKKKKKKK from './APP.vue'
//import router from './router'
//import store from './store'
 
Vue.config.productionTip = false
 //import KKKKKKKKK from './APP.vue' 中的KKKKKKKKK 
 //应与render: h => h(KKKKKKKKK)中的KKKKKKKKK一致
new Vue({
  //router,
  //store,
  render: h => h(KKKKKKKKK)
}).$mount('#K')