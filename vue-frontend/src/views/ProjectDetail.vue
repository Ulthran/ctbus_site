<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'
const route = useRoute()

const pages = import.meta.glob('../projects/*.vue', { eager: true })

const component = computed(() => {
  const name = route.params.project
  return pages[`../projects/${name}.vue`]
})
</script>

<template>
  <component :is="component" v-if="component" />
  <v-container v-else>Project not found.</v-container>
</template>
