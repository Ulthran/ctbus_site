<script setup>
import SimplePage from "../components/SimplePage.vue";

const schools = [
  {
    name: "Carleton College",
    link: "https://www.carleton.edu/",
    img: `CDN_URL/images/carleton_logo.png`,
  },
  {
    name: "Marblehead High School",
    link: "https://www.marbleheadschools.org/marblehead-high-school",
    img: `CDN_URL/images/mhs_logo.png`,
  },
];
</script>

<template>
  <SimplePage title="Education">
    <v-row justify="center">
      <v-col cols="12" md="4" v-for="school in schools" :key="school.name">
        <v-card class="ma-4" :href="school.link" target="_blank">
          <v-img
            :src="school.img"
            :alt="school.name"
            height="160"
            contain
            loading="lazy"
          />
          <v-card-title>{{ school.name }}</v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </SimplePage>
</template>
