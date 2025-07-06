<script setup>
import { useRoute } from "vue-router";
import { ref, watch } from "vue";

const loading = ref(true);
const notFound = ref(false);

const route = useRoute();
const component = ref(null);

async function loadComponent() {
  loading.value = true;
  notFound.value = false;
  component.value = null;
  const name = route.params.slug;
  try {
    component.value = await window["vue3-sfc-loader"].loadModule(
      `${window.postsPath}/${name}.vue`,
      window.loaderOptions
    );
    if (!component.value) {
      notFound.value = true;
    }
  } catch (e) {
    console.error("Error loading component:", e);
    component.value = null;
    notFound.value = true;
  } finally {
    loading.value = false;
  }
}

watch(
  () => route.params.slug,
  () => {
    loadComponent();
  },
  { immediate: true }
);
</script>

<template>
  <v-container class="py-8 d-flex justify-center" v-if="loading">
    <v-progress-circular indeterminate aria-label="Loading post..." />
  </v-container>
  <component :is="component" v-else-if="component" />
  <v-container v-else-if="notFound">Post not found.</v-container>
</template>
