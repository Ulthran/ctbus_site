<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["disctracker"];
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`/assets/images/${info.image}`"
  />
  <v-container>
    <v-card>
      <v-card-title>Overview</v-card-title>
      <v-card-text>
        WORK IN PROGRESS. My goal was originally to create a real-time stat
        tracking app so that coaches could easily and actively track touches,
        turnovers, scores, play time, etc during a game and receive suggestions
        on how to stick to whatever plan they create for player management. That
        still sounds cool but my attention has drifted towards the data
        processing and analytics end of the process. Focus is lacking but dreams
        are big.
      </v-card-text>
    </v-card>
  </v-container>
</template>
