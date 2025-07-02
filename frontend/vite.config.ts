import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src') // <== Para que @ funcione correctamente
    }
  },
  server: {
    proxy: {
      '/articulos': 'http://localhost:5000',
      '/marcas': 'http://localhost:5000',
      '/categorias': 'http://localhost:5000',
      '/proveedores': 'http://localhost:5000',
    }
  }
})
