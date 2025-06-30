<script setup>
import { useRoute } from 'vue-router'
import { ref, watch } from 'vue'

const route = useRoute()
const component = ref(null)

async function loadComponent() {
  const name = route.params.name
  try {
    component.value = await window['vue3-sfc-loader'].loadModule(
      `${window.componentsPath}/${name}.vue`,
      window.loaderOptions,
    )
  } catch (e) {
    console.error('Failed to load component:', e)
    component.value = null
  }
}

watch(
  () => route.params.name,
  () => {
    loadComponent()
  },
  { immediate: true },
)
</script>

<template>
  <component :is="component" v-if="component" />
  <v-container v-else>Component not found.</v-container>
</template>
