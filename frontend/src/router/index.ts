import { createRouter, createWebHistory } from 'vue-router'

import articulosView from '@/views/articulosView.vue'
import categoriasView from '@/views/categoriasView.vue'
import proveedoresView from '@/views/proveedoresView.vue'
import marcasView from '@/views/marcasView.vue'

const routes = [
  {
    path: '/',
    redirect: '/articulos'
  },
  {
    path: '/articulos',
    name: 'Articulos',
    component: articulosView
  },
  {
    path: '/categorias',
    name: 'Categorias',
    component: categoriasView
  },
  {
    path: '/proveedores',
    name: 'Proveedores',
    component: proveedoresView
  },
  {
    path: '/marcas',
    name: 'Marcas',
    component: marcasView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
