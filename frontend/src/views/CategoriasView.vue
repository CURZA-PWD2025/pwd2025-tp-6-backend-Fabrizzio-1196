<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-8 font-sans">
    <header class="flex flex-col items-center mb-8">
      <img class="logo" src="@/assets/logo3.png" alt="Logo" />
      <h1 class="text-4xl font-bold text-gray-800 mt-4">Categorías</h1>
    </header>

    <div class="w-full max-w-7xl bg-white p-6 rounded-3xl shadow-xl">
      <Categorias />
    </div>
  </div>
</template>

<script setup lang="ts">
import Categorias from '@/components/categorias.vue'
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

.font-sans {
  font-family: 'Inter', sans-serif;
}

.logo {
  width: 60px;
  height: 60px;
  object-fit: contain;
}
</style>
