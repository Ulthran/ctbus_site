<script setup>
import { onMounted } from "vue";

onMounted(() => {
  // Redirect directly to JupyterLab
  window.location.replace("https://jupyter.charliebushman.com");
});
</script>

<template>
  <v-container class="text-center">
    <p>Opening JupyterLab...</p>
  </v-container>
</template>
