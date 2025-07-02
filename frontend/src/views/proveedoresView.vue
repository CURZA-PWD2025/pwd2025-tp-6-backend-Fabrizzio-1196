<template>
  <div class="container">
    <header class="header">
      <img class="logo" src="@/assets/logo.jpg" alt="Logo" />
      <h1>Proveedores</h1>
    </header>
    <Proveedores />
  </div>
</template>

<script setup lang="ts">
import Proveedores from '@/components/proveedores.vue'
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.container {
  max-width: 900px;
  margin: 40px auto;
  padding: 20px;
  font-family: 'Poppins', sans-serif;
  color: #333;
  background: #f9f9fb;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
}

.logo {
  width: 60px;
  height: 60px;
  object-fit: contain;
}

h1 {
  font-weight: 600;
  font-size: 2.5rem;
  margin: 0;
  color: #2c3e50;
}
</style>