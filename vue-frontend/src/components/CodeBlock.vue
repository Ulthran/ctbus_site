<template>
  <v-card class="my-4" variant="outlined">
    <pre ref="pre" class="line-numbers"><code :class="languageClass"></code></pre>
  </v-card>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
const props = defineProps({
  code: { type: String, required: true },
  language: { type: String, default: 'markup' }
});
const pre = ref(null);
const languageClass = computed(() => `language-${props.language}`);

onMounted(() => {
  const el = pre.value.querySelector('code');
  if (el) {
    el.textContent = props.code;
    if (window.Prism) {
      Prism.highlightElement(el);
    }
  }
});
</script>

<style scoped>
pre {
  margin: 0;
  background-color: #2d2d2d;
  color: #f8f8f2;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
  font-family: 'Fira Code', monospace;
}
</style>
