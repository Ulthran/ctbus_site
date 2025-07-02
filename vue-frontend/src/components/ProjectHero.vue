<template>
  <v-container class="my-4">
    <v-row align="center">
      <v-col cols="auto">
        <v-img :src="img" :alt="title" width="120" height="120" class="rounded-circle" loading="lazy" />
      </v-col>
      <v-col>
        <h1 class="text-h5 font-weight-bold mb-2">{{ title }}</h1>
        <p class="text-subtitle-1">{{ subtitle }}</p>
        <div class="mt-2">
          <v-chip
            v-for="tag in tags"
            :key="tag"
            class="ma-1"
            size="small"
            variant="outlined"
          >
            {{ tag }}
          </v-chip>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup>
defineProps({
  title: String,
  subtitle: String,
  img: String,
  tags: Array,
})
</script>
