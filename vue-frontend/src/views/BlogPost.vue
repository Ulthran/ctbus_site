<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const posts = import.meta.glob('../posts/*.vue', { eager: true })

const component = computed(() => {
  const name = route.params.post
  return posts[`../posts/${name}.vue`]
})
</script>

<template>
  <component :is="component" v-if="component" />
  <v-container v-else>Post not found.</v-container>
</template>
