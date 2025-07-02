<template>
  <div>
    <form @submit.prevent="crearMarca">
      <input v-model="nueva.nombre" placeholder="Nombre de la marca" />
      <button type="submit">Crear</button>
    </form>
    <ul>
      <li v-for="m in marcas" :key="m.id">
        {{ m.nombre }}
        <button @click="eliminar(m.id)">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useMarcasStore } from '@/stores/marcas'

const store = useMarcasStore()
const nueva = ref({ nombre: '' })

onMounted(() => store.fetchMarcas())

const marcas = computed(() => store.marcas)

const crearMarca = async () => {
  await store.createMarca(nueva.value)
  nueva.value.nombre = ''
}

const eliminar = async (id: number | undefined) => {
  if (!id) return
  try {
    await store.deleteMarca(id)
  } catch (error) {
    console.error("Error eliminando marca:", error)
  }
}
</script>
