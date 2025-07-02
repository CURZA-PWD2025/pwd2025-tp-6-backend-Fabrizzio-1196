<template>
  <div class="page-container">
    <div class="card">
      <h1 class="title">Gestión de Artículos</h1>
      <Articulos />
    </div>
  </div>
</template>

<script setup lang="ts">
import Articulos from '@/components/Articulos.vue'
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

.page-container {
  background: linear-gradient(to right, #f0f4f8, #d9e2ec);
  min-height: 100vh;
  padding: 4rem 2rem;
  display: flex;
  justify-content: center;
  align-items: start;
  font-family: 'Inter', sans-serif;
}

.card {
  background-color: white;
  padding: 3rem;
  border-radius: 1.5rem;
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 1400px;
  transition: all 0.3s ease;
}

.title {
  font-size: 2.5rem;
  color: #1e293b;
  margin-bottom: 2rem;
  text-align: center;
  font-weight: 700;
}
</style>
