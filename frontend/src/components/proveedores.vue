<template>

  <div>
    <form @submit.prevent="crearProveedor">
      <input v-model="nuevo.nombre" placeholder="Nombre" />
      <input v-model="nuevo.telefono" placeholder="Teléfono" />
      <input v-model="nuevo.direccion" placeholder="Dirección" />
      <input v-model="nuevo.email" placeholder="Email" />
      <button type="submit">Crear</button>
    </form><ul>
  <li v-for="p in proveedores" :key="p.id">
    {{ p.nombre }} - {{ p.telefono }} - {{ p.email }}
    <button @click="eliminar(p.id)">Eliminar</button>
  </li>
</ul>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useProveedoresStore } from '@/stores/proveedores'
const store = useProveedoresStore()
const nuevo = ref({ nombre: '', telefono: '', direccion: '', email: '' })
onMounted(() => store.fetchProveedores())
const crearProveedor = async () => {
  await store.createProveedor(nuevo.value)
  nuevo.value = { nombre: '', telefono: '', direccion: '', email: '' }
}
const eliminar = (id: number) => store.deleteProveedor(id)
const proveedores = store.proveedores
</script>
