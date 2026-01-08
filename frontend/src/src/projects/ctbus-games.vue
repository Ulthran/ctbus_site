<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["ctbus-games"];
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`ASSETS_BASE_URL/images/${info.image}`"
  />
  <v-container>
    <v-card class="mb-4">
      <v-card-title>Overview</v-card-title>
      <v-card-text>
        A collection of game development experiments. Nothing too fancy.
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>Links</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="auto">
            <a
              href="https://games.charliebushman.com"
              target="_blank"
              title="CTBus Games Site"
            >
              <v-btn variant="text" icon>
                <i class="fas fa-globe"></i>
              </v-btn>
            </a>
          </v-col>
          <v-col cols="auto">
            <a
              href="https://github.com/Ulthran/ctbus_site/tree/master/games"
              target="_blank"
              title="GitHub Repo"
            >
              <v-btn variant="text" icon>
                <i class="fab fa-github"></i>
              </v-btn>
            </a>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>
