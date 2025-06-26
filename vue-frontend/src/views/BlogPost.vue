<script setup>
import { useRoute } from 'vue-router'
import posts from '../data/posts.json'
import { ref, onMounted } from 'vue'

const route = useRoute()
const html = ref('')

onMounted(async () => {
  const name = route.params.post
  const res = await fetch(`/blog/${name}.html`)
  html.value = await res.text()
})
</script>

<template>
  <div class="container mx-auto p-4" v-html="html"></div>
</template>
