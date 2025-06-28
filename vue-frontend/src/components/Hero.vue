<template>
  <div class="container mx-auto flex-1 mt-8 p-2 md:p-4 text-center md:w-1/2">
    <h1 class="text-4xl font-bold mb-2">{{ title }}</h1>
    <p class="text-lg" v-html="subtitle"></p>
    <slot />
  </div>
</template>
<script setup>
defineProps({
  title: String,
  subtitle: String
})
</script>
