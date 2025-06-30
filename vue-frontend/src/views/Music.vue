<script setup>
import SimplePage from '../components/SimplePage.vue'
</script>

<template>
  <SimplePage title="Music">
    <p>Music sounds good. I listen to it a lot and sometimes try to make it. Top 0.05% of Jacob Collier listeners on Spotify for 4 years running. I play piano. I've also made playlists of my new music finds every month since January 2022, follow my Spotify to listen.</p>
    <div class="d-flex justify-center my-4">
      <v-btn icon href="https://open.spotify.com/user/charlie_bushman?si=0dd732a8d6da46b6" target="_blank">
        <v-icon>mdi-spotify</v-icon>
      </v-btn>
      <v-btn icon href="https://0qn7o9e6pd.execute-api.us-east-1.amazonaws.com/Prod/" target="_blank">
        <v-icon>mdi-web</v-icon>
      </v-btn>
    </div>
  </SimplePage>
</template>
