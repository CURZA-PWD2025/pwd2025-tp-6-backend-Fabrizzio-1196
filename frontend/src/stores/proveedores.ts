import { defineStore } from 'pinia'
import axios from 'axios'

export const useProveedoresStore = defineStore('proveedores', {
  state: () => ({
    proveedores: [] as any[],
    proveedor: null as any,
  }),

  actions: {
    async fetchProveedores() {
      const res = await axios.get('http://localhost:5000/proveedores/')
      this.proveedores = res.data
    },

    async fetchProveedor(id: number) {
      const res = await axios.get(`http://localhost:5000/proveedores/${id}`)
      this.proveedor = res.data
    },

    async createProveedor(data: any) {
      await axios.post('http://localhost:5000/proveedores/', data)
      await this.fetchProveedores()
    },

    async updateProveedor(id: number, data: any) {
      await axios.put(`http://localhost:5000/proveedores/${id}`, data)
      await this.fetchProveedores()
    },

    async deleteProveedor(id: number) {
      await axios.delete(`http://localhost:5000/proveedores/${id}`)
      await this.fetchProveedores()
    },
    
  }
})