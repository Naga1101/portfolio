import { createApp } from 'vue'

import App from './App.vue';
import router from '../router/index.js';

createApp(App)
  .use(router) // Use the router
  .mount('#app');
