<script setup>
import { onMounted } from "vue";

onMounted(() => {
  // Redirect directly to the resume so navigating to /resume
  // loads the PDF in the current tab instead of opening a new one
  window.location.replace("ASSETS_BASE_URL/documents/resume.pdf");
});
</script>

<template>
  <v-container class="text-center">
    <p>Opening resume...</p>
  </v-container>
</template>
