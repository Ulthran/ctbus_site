<script setup>
import { ref, onMounted } from "vue";
import Hero from "../components/Hero.vue";

const CLIENT_ID = "SPOTIFY_CLIENT_ID";
const CLIENT_SECRET = "SPOTIFY_CLIENT_SECRET";

const monthlies = ref([]);

async function fetchMonthlyPlaylists() {
  try {
    const tokenRes = await fetch("https://accounts.spotify.com/api/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization: "Basic " + btoa(`${CLIENT_ID}:${CLIENT_SECRET}`),
      },
      body: "grant_type=client_credentials",
    });
    const tokenData = await tokenRes.json();
    const token = tokenData.access_token;

    let url =
      "https://api.spotify.com/v1/users/charlie_bushman/playlists?limit=50";
    const playlists = [];
    while (url) {
      const res = await fetch(url, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await res.json();
      playlists.push(...data.items.filter(Boolean));
      url = data.next;
    }

    const regex = /[A-Z][a-z]{2} ['‘]\d{2}/;
    const months = [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ];

    const filtered = playlists
      .filter((p) => regex.test(p.name))
      .map((p) => ({ ...p, name: p.name.replace("‘", "'") }));

    filtered.sort((a, b) => {
      const aYear = parseInt(a.name.slice(-2));
      const bYear = parseInt(b.name.slice(-2));
      if (aYear !== bYear) return bYear - aYear;
      const aMonth = months.indexOf(a.name.slice(0, 3));
      const bMonth = months.indexOf(b.name.slice(0, 3));
      return bMonth - aMonth;
    });

    monthlies.value = filtered.map((p) => ({
      name: p.name,
      url: p.external_urls?.spotify || "#",
      image: (p.images && p.images[2] && p.images[2].url) || "#",
    }));
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
