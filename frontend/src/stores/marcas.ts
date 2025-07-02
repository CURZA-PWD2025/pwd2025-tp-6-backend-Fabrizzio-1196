import { defineStore } from 'pinia'
import axios from 'axios'
import type { Marca } from '@/interfaces/marcas'

export const useMarcasStore = defineStore('marcas', {
  state: () => ({
    marcas: [] as Marca[],
    marca: null as Marca | null
  }),

  actions: {
    async fetchMarcas() {
      const res = await axios.get('http://localhost:5000/marcas/')
      this.marcas = res.data
    },

    async fetchMarca(id: number) {
      const res = await axios.get(`http://localhost:5000/marcas/${id}`)
      this.marca = res.data
    },

    async createMarca(data: Marca) {
      await axios.post('http://localhost:5000/marcas/', data)
      await this.fetchMarcas()
    },

    async updateMarca(id: number, data: Marca) {
      await axios.put(`http://localhost:5000/marcas/${id}`, data)
      await this.fetchMarcas()
    },

    async deleteMarca(id: number) {
    await axios.delete(`http://localhost:5000/marcas/${id}`)
    await this.fetchMarcas()
}
  }
})