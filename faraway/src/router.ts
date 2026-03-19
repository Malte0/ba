import { createWebHistory, createRouter } from 'vue-router'

import InspectorView from './views/InspectorView.vue'
import Game from './views/Game.vue'

const routes = [
  { path: '/', component: Game },
  { path: '/inspector', component: InspectorView },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})