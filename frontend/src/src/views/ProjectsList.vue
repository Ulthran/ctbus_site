<script setup>
const projects = window.projects;
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Projects</h1>
    <v-list>
      <v-list-item
        v-for="(proj, name) in projects"
        :key="name"
        :to="`/projects/${name}`"
        link
      >
        <template v-slot:prepend>
          <v-avatar
            class="rounded-circle"
            :style="{ width: '60px', height: '60px' }"
          >
            <v-img
              :src="`ASSETS_BASE_URL/images/${proj.image}`"
              :alt="proj.title"
              cover
              loading="lazy"
            />
          </v-avatar>
        </template>
        <v-list-item-title>{{ proj.title }}</v-list-item-title>
        <v-list-item-subtitle>{{ proj.subtitle }}</v-list-item-subtitle>
        <v-list-item-subtitle>
          <div class="d-flex flex-wrap">
            <v-chip
              v-for="tag in proj.tags"
              :key="tag"
              class="ma-1"
              size="x-small"
              variant="outlined"
            >
              {{ tag }}
            </v-chip>
          </div>
        </v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-container>
</template>
