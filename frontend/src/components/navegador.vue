<template>
  <nav class="navbar">
    <h1 class="navbar-title">Panel de Administración</h1>
    <ul class="nav-links">
      <li><RouterLink to="/">Inicio</RouterLink></li>
      <li><RouterLink to="/articulos">Artículos</RouterLink></li>
      <li><RouterLink to="/categorias">Categorías</RouterLink></li>
      <li><RouterLink to="/marcas">Marcas</RouterLink></li>
      <li><RouterLink to="/proveedores">Proveedores</RouterLink></li>
    </ul>
  </nav>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.navbar {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  color: white;
}

.navbar-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  padding: 0;
  margin: 0;
  flex-wrap: wrap;
}

.nav-links li a {
  color: #cbd5e1;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease, border-bottom 0.3s ease;
}

.nav-links li a:hover,
.nav-links li a.router-link-exact-active {
  color: #ffffff;
  border-bottom: 2px solid #ffffff;
}
</style>