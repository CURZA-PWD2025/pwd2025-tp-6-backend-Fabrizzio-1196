<template>
  <div class="container">

    <form @submit.prevent="guardarArticulo">
      <div>
        <label>Descripción:</label>
        <input v-model="form.descripcion" required />
      </div>
      <div>
        <label>Precio:</label>
        <input type="number" v-model="form.precio" required />
      </div>
      <div>
        <label>Stock:</label>
        <input type="number" v-model="form.stock" required />
      </div>
      <div>
        <label>Marca:</label>
        <select v-model="form.marca_id" required>
          <option v-for="marca in marcas" :key="marca.id" :value="marca.id">
            {{ marca.nombre }}
          </option>
        </select>
      </div>
      <div>
        <label>Proveedor:</label>
        <select v-model="form.proveedor_id" required>
          <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor.id">
            {{ proveedor.nombre }}
          </option>
        </select>
      </div>
      <div>
        <label>Categorías:</label>
        <div v-for="cat in categorias" :key="cat.id">
          <input type="checkbox" :value="cat.id" v-model="form.categorias" /> {{ cat.nombre }}
        </div>
      </div>

      <button type="submit">{{ form.id ? 'Actualizar' : 'Crear' }}</button>
      <button type="button" @click="resetForm">Cancelar</button>
    </form>

    <hr />

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Descripción</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Marca</th>
          <th>Proveedor</th>
          <th>Categorías</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="art in articulos" :key="art.id">
          <td>{{ art.id }}</td>
          <td>{{ art.descripcion }}</td>
          <td>{{ art.precio }}</td>
          <td>{{ art.stock }}</td>
          <td>{{ getMarcaNombre(art.marca_id) }}</td>
          <td>{{ getProveedorNombre(art.proveedor_id) }}</td>
          <td>
            <ul>
              <li v-for="catId in art.categorias" :key="catId">
                {{ getCategoriaNombre(catId) }}
              </li>
            </ul>
          </td>
          <td>
            <button @click="editar(art)">Editar</button>
            <button @click="eliminarArticulo(art.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticulosStore } from '@/stores/articulos'
import { useMarcasStore } from '@/stores/marcas'
import { useProveedoresStore } from '@/stores/proveedores'
import { useCategoriasStore } from '@/stores/categorias'

const store = useArticulosStore()
const marcasStore = useMarcasStore()
const proveedoresStore = useProveedoresStore()
const categoriasStore = useCategoriasStore()

const form = ref({
  id: null,
  descripcion: '',
  precio: 0,
  stock: 0,
  marca_id: '',
  proveedor_id: '',
  categorias: []
})

const resetForm = () => {
  form.value = {
    id: null,
    descripcion: '',
    precio: 0,
    stock: 0,
    marca_id: '',
    proveedor_id: '',
    categorias: []
  }
}

const guardarArticulo = async () => {
  if (form.value.id) {
    await store.updateArticulo(form.value.id, form.value)
  } else {
    await store.createArticulo(form.value)
  }
  resetForm()
  await store.fetchArticulos()
}

const editar = (articulo) => {
  form.value = {
    id: articulo.id,
    descripcion: articulo.descripcion,
    precio: articulo.precio,
    stock: articulo.stock,
    marca_id: articulo.marca_id,
    proveedor_id: articulo.proveedor_id,
    categorias: articulo.categorias_ids || []  // asegurate de que viene como array de IDs
  }
}

const eliminarArticulo = async (id) => {
  await store.deleteArticulo(id)
  await store.fetchArticulos()
}

const getMarcaNombre = (id) => {
  const marca = marcas.value.find(m => m.id === id)
  return marca ? marca.nombre : '—'
}

const getProveedorNombre = (id) => {
  const proveedor = proveedores.value.find(p => p.id === id)
  return proveedor ? proveedor.nombre : '—'
}

const getCategoriaNombre = (id) => {
  const cat = categorias.value.find(c => c.id === id)
  return cat ? cat.nombre : '—'
}

const articulos = store.articulos
const marcas = marcasStore.marcas
const proveedores = proveedoresStore.proveedores
const categorias = categoriasStore.categorias
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: auto;
}

form div {
  margin-bottom: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

td,
th {
  border: 1px solid #ccc;
  padding: 8px;
}
</style>