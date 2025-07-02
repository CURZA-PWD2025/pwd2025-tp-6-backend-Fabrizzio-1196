import { defineStore } from 'pinia'
import axios from 'axios'
import type { Articulo } from '@/interfaces/articulos'

export const useArticulosStore = defineStore('articulos', {
  state: () => ({
    articulos: [] as Articulo[],
    articulo: null as Articulo | null
  }),

  actions: {
    async fetchArticulos() {
      const res = await axios.get('http://localhost:5000/articulos/')
      this.articulos = res.data
    },

    async fetchArticulo(id: number) {
      const res = await axios.get(`http://localhost:5000/articulos/${id}`)
      this.articulo = res.data
    },

    async createArticulo(data: Articulo) {
      await axios.post('http://localhost:5000/articulos/', data)
      await this.fetchArticulos()
    },

    async updateArticulo(id: number, data: Articulo) {
      await axios.put('http://localhost:5000/categorias/', data)
      await this.fetchArticulos()
    },

    async deleteArticulo(id: number) {
      await axios.delete(`http://localhost:5000/articulos/${id}`)
      await this.fetchArticulos()
    }
    }
})