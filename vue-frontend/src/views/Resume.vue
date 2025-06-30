<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  window.open('CDN_URL/documents/resume.pdf', '_blank')
})
</script>

<template>
  <v-container class="text-center">
    <p>Opening resume...</p>
  </v-container>
</template>
