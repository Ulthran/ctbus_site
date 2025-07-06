<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["spotify-vis"];
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`CDN_URL/images/${info.image}`"
  />
  <v-container>
    <v-card class="mb-4">
      <v-card-title>Overview</v-card-title>
      <v-card-text>
        I had originally created a few Spotify stats graphs on this website as a
        fun project but the code behind it was messy and the display was
        mediocre. So I created a new AWS SAM application with a Python runtime
        using Dash to serve the frontend. Unfortunately, Spotify just (late
        2024) removed a lot of public access for interesting things like song
        audio features, so pretty much all that's left to show is a popularity
        score per song per playlist. Try it out yourself and let me know what
        you think!
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>Links</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="auto">
            <a
              href="https://0qn7o9e6pd.execute-api.us-east-1.amazonaws.com/Prod/"
              target="_blank"
              title="Spotify Vis Site"
            >
              <v-btn variant="text" icon>
                <i class="fas fa-globe"></i>
              </v-btn>
            </a>
          </v-col>
          <v-col cols="auto">
            <a
              href="https://github.com/Ulthran/spotify_vis"
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
