<script setup>
const projects = window.projects;
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Projects</h1>
    <v-row>
      <v-col v-for="(proj, name) in projects" :key="name" cols="12" md="6">
        <v-card
          class="ma-2 scrollable-card uniform-card"
          :to="`/projects/${name}`"
          link
        >
          <v-row no-gutters align="center">
            <v-col cols="auto">
              <v-img
                :src="`/assets/images/${proj.image}`"
                :alt="proj.title"
                width="60"
                height="60"
                class="rounded-circle"
                cover
                loading="lazy"
              />
            </v-col>
            <v-col>
              <v-card-title class="text-wrap">{{ proj.title }}</v-card-title>
              <v-card-subtitle class="text-wrap">{{
                proj.subtitle
              }}</v-card-subtitle>
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
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
