<template>
  <div>
    <form @submit.prevent="crearCategoria">
      <input v-model="nueva.nombre" placeholder="Nombre de la categoría" />
      <button type="submit">Crear</button>
    </form>
    <ul>
      <li v-for="c in categorias" :key="c.id">
        {{ c.nombre }}
        <button v-if="c.id !== undefined" @click="eliminar(c.id)">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useCategoriasStore } from '@/stores/categorias'

const store = useCategoriasStore()
const categorias = store.categorias
const nueva = ref({ nombre: '' })

onMounted(() => store.fetchCategorias())

const crearCategoria = async () => {
  const nombreLimpio = nueva.value.nombre.trim()
  if (!nombreLimpio) {
    alert('El nombre de la categoría no puede estar vacío.')
    return
  }
  try {
    await store.createCategoria({ nombre: nombreLimpio })
    nueva.value.nombre = ''
  } catch (error) {
    console.error('Error al crear la categoría:', error)
    alert('No se pudo crear la categoría. Intenta nuevamente.')
  }
}

const eliminar = async (id: number) => {
  try {
    await store.deleteCategoria(id)
  } catch (error) {
    console.error('Error al eliminar la categoría:', error)
    alert('No se pudo eliminar la categoría. Intenta nuevamente.')
  }
}
</script>