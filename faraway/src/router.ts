import { createWebHistory, createRouter } from 'vue-router'

import InspectorView from './views/InspectorView.vue'

const routes = [
  { path: '/', component: InspectorView },
  // { path: '/inspector', component: LogInScreen },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})