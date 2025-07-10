<script setup>
import { ref, onMounted } from "vue";
import Hero from "../components/Hero.vue";

const PLAYLISTS_URL = "SPOTIFY_PLAYLISTS_URL";

const monthlies = ref([]);

async function fetchMonthlyPlaylists() {
  try {
    const res = await fetch(PLAYLISTS_URL);
    if (!res.ok) throw new Error("Failed to fetch playlists");
    monthlies.value = await res.json();
  } catch (e) {
    console.error("Failed to fetch playlists", e);
  }
}

onMounted(fetchMonthlyPlaylists);
</script>

<template>
  <Hero
    title="Music"
    subtitle="Music sounds good. I listen to it a lot and sometimes try to make it. Top 0.05% of Jacob Collier listeners on Spotify for 4 years running. I play piano. I've also made playlists of my new music finds every month since January 2022, follow my Spotify to listen."
  >
    <div class="d-flex justify-center my-4 mx-6">
      <v-btn
        class="p-6"
        icon
        href="https://open.spotify.com/user/charlie_bushman?si=0dd732a8d6da46b6"
        target="_blank"
      >
        <v-icon icon="fa-brands fa-spotify" />
      </v-btn>
      <v-btn
        class="p-6"
        icon
        href="https://0qn7o9e6pd.execute-api.us-east-1.amazonaws.com/Prod/"
        target="_blank"
      >
        <v-icon icon="fa-solid fa-globe" />
      </v-btn>
    </div>
    <div class="d-flex flex-wrap justify-center">
      <div v-for="p in monthlies" :key="p.name" class="text-center ma-2">
        <a :href="p.url" target="_blank" class="text-decoration-none">
          <h2 class="text-subtitle-1 font-weight-bold">{{ p.name }}</h2>
          <img
            :src="p.image"
            alt="Missing Playlist Graphic"
            width="80"
            height="80"
            class="rounded"
          />
        </a>
      </div>
    </div>
  </Hero>
</template>
