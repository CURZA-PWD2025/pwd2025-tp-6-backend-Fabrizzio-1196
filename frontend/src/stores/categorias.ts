import { defineStore } from 'pinia'
import axios from 'axios'
import type { Categoria } from '@/interfaces/categorias'

export const useCategoriasStore = defineStore('categorias', {
  state: () => ({
    categorias: [] as Categoria[],
    categoria: null as Categoria | null
  }),

  actions: {
    async fetchCategorias() {
      const res = await axios.get('http://localhost:5000/categorias/')
      this.categorias = res.data
    },

    async fetchCategoria(id: number) {
      const res = await axios.get(`http://localhost:5000/categorias/${id}`)
      this.categoria = res.data
    },

    async createCategoria(data: Categoria) {
      await axios.post('http://localhost:5000/categorias/', data)
      await this.fetchCategorias()
    },

    async updateCategoria(id: number, data: Categoria) {
      await axios.put(`http://localhost:5000/categorias/${id}`, data)
      await this.fetchCategorias()
    },

    async deleteCategoria(id: number) {
      await axios.delete(`http://localhost:5000/categorias/${id}`)
      await this.fetchCategorias()
    },
    
  }
})