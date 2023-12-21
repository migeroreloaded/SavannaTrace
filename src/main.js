import Vue from 'vue';
import App from './App.vue';
import VueMqtt from 'vue-mqtt';

Vue.config.productionTip = false;

Vue.use(VueMqtt, 'wss://broker.emqx.io', {
  clientId: 'my-mqtt-app-client', 
});

new Vue({
  render: (h) => h(App),
}).$mount('#app');
