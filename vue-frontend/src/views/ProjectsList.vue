<script setup>
import projects from '../data/projects.json'
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Projects</h1>
    <v-list lines="two">
      <v-list-item
        v-for="(proj, name) in projects"
        :key="name"
        :to="`/projects/${name}`"
        link
      >
        <v-list-item-title>{{ proj.title }}</v-list-item-title>
        <v-list-item-subtitle>{{ proj.subtitle }}</v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-container>
</template>
