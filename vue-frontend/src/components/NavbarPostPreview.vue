<template>
  <v-container class="my-4 py-2" max-width="50%"></v-container>
    <v-row align="center">
      <v-col cols="auto">
        <v-img :src="img" :alt="title" width="120" height="120" class="rounded" loading="lazy" />
      </v-col>
      <v-col>
        <h1 class="text-h5 font-weight-bold mb-2">{{ title }}</h1>
        <p class="text-subtitle-1 mb-1">{{ subtitle }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup>
defineProps({
  title: String,
  subtitle: String,
  img: String,
});
</script>
