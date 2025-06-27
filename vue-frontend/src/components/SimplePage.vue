<template>
  <div class="container mx-auto p-4 text-center">
    <h1 class="text-2xl font-bold mb-2">{{ title }}</h1>
    <slot />
  </div>
</template>
<script setup>
defineProps({
  title: {
    type: String,
    required: true
  }
})
</script>
