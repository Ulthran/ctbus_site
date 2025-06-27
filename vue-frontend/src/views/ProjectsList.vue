<script setup>
import projects from '../data/projects.json'
</script>

<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Projects</h1>
    <div v-for="(proj, name) in projects" :key="name" class="mb-4">
      <router-link :to="`/projects/${name}`" class="text-blue-600 underline">
        {{ proj.title }}
      </router-link>
      <p class="text-sm">{{ proj.subtitle }}</p>
    </div>
  </div>
</template>
