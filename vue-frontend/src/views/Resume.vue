<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  window.location.href = '/documents/resume.pdf'
})
</script>

<template>
  <v-container class="text-center">
    <p>Redirecting to resume...</p>
  </v-container>
</template>
