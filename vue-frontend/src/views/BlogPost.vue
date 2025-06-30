<script setup>
import { useRoute } from 'vue-router'
import { ref, watch } from 'vue'

const route = useRoute()
const component = ref(null)

async function loadComponent() {
  const name = route.params.slug
  try {
    component.value = await window['vue3-sfc-loader'].loadModule(
      `${window.postsPath}/${name}.vue`,
      window.loaderOptions,
    )
  } catch (e) {
    console.error('Error loading component:', e)
    component.value = null
  }
}

watch(
  () => route.params.slug,
  () => {
    loadComponent()
  },
  { immediate: true },
)
</script>

<template>
  <component :is="component" v-if="component" />
  <v-container v-else>Post not found.</v-container>
</template>
