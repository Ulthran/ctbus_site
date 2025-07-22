<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["ctbus-health"];
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`ASSETS_BASE_URL/images/${info.image}`"
  />
  <v-container>
    <v-card>
      <v-card-title>Overview</v-card-title>
      <v-card-text>
        WORK IN PROGRESS. I've been keeping more and more personal biometric
        data as I figure out what I care about and what maybe I should care
        about. I've had a heart rate tracking watch of some sort for years now.
        I've been tracking my weight daily for almost a year. And as of 2025 I'm
        keeping track of everything I eat as well. All that data deserves a good
        pipeline so I'm taking the chance to apply all my newfound knowledge of
        AWS SAM and Glue and create a serverless ETL pipeline.
      </v-card-text>
    </v-card>
  </v-container>
</template>
