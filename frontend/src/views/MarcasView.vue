<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-8 font-sans">
    <header class="flex flex-col items-center mb-8">
      <img
        class="w-24 h-24 rounded-full shadow-md mb-4">
        <img class="logo" src="@/assets/logo2.png" alt="Logo" />
      <h1 class="text-4xl font-bold text-gray-800">Marcas</h1>
    </header>

    <div class="w-full max-w-3xl bg-white p-6 rounded-2xl shadow-xl">
      <Marcas />
    </div>
  </div>
</template>

<script setup lang="ts">
import Marcas from '@/components/marcas.vue'
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

.font-sans {
  font-family: 'Inter', sans-serif;
}
</style>