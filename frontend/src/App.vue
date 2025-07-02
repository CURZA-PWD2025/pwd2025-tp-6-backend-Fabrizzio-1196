<script setup lang="ts">
import { RouterView } from 'vue-router'
import Navbar from './components/navegador.vue'
</script>

<template>
  <div id="app">
    <header class="app-header">
      <Navbar />
    </header>

    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f4f6f8;
  color: #333;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background-color: #1e3a8a; 
  padding: 1.5rem 3rem; 
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.app-main {
  flex: 1;
  padding: 3rem 4rem; 
  max-width: 1200px; 
  margin: 0 auto; 
}
</style>
