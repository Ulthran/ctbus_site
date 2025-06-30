<script setup>
import projects from '../data/projects.json'
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Projects</h1>
    <div v-for="(proj, name) in projects" :key="name" class="mb-4">
      <router-link :to="`/projects/${name}`" class="text-blue-600 underline">
        {{ proj.title }}
      </router-link>
      <p class="text-caption">{{ proj.subtitle }}</p>
    </div>
  </v-container>
</template>
