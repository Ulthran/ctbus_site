<template>
  <v-container class="py-4 text-center">
    <h1 class="text-h5 font-weight-bold mb-2">{{ title }}</h1>
    <slot />
  </v-container>
</template>
<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
});
</script>
