<template>
  <v-container class="mt-8 text-center">
    <v-row justify="center">
      <v-col cols="12" md="6">
        <h1 class="text-h4 font-weight-bold mb-2">{{ title }}</h1>
        <p v-html="subtitle" class="text-subtitle-1"></p>
        <slot />
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup>
defineProps({
  title: String,
  subtitle: String,
});
</script>
