<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
const route = useRoute()
const html = ref('')

onMounted(async () => {
  const name = route.params.project
  const res = await fetch(`/projects/${name}.html`)
  html.value = await res.text()
})
</script>

<template>
  <div class="container mx-auto p-4" v-html="html"></div>
</template>
