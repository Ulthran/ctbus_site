<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["chaos"];
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
        This one started out as a demo for a guest lecture on snakemake but I couldn't get the JS-based kernel to work with all of the shell commands snakemake is built around, so I turned to recreating all my favorite chaotic systems and fractals instead (and ended up showing the snakemake demo on my machine, no interactive component :(). I'm always coming back to this and adding more systems or updating existing ones with new features and documentation. There are always crazy new ways to visualize chaos!
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>Links</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="auto">
            <a
              href="https://jupyter.charliebushman.com"
              target="_blank"
              title="Jupyter Site"
            >
              <v-btn variant="text" icon>
                <i class="fas fa-globe"></i>
              </v-btn>
            </a>
          </v-col>
          <v-col cols="auto">
            <a
              href="https://github.com/Ulthran/ctbus_site/tree/master/jupyter"
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