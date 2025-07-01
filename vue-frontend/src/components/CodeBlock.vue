<template>
  <v-card class="my-4" variant="outlined">
    <div class="code-header" v-if="props.filename">
      <span class="filename">{{ props.filename }}</span>
      <v-btn
        class="copy-btn"
        size="small"
        variant="text"
        @click="copyCode"
      >
        <v-icon icon="fas fa-copy" />
      </v-btn>
    </div>
    <pre ref="pre" class="line-numbers"><code :class="languageClass"></code></pre>
  </v-card>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
const props = defineProps({
  code: { type: String, required: true },
  language: { type: String, default: 'markup' },
  filename: { type: String, default: '' }
});
const pre = ref(null);
const languageClass = computed(() => `language-${props.language}`);

function loadPrism() {
  if (window.Prism) {
    return Promise.resolve();
  }
  return new Promise(resolve => {
    const theme = document.createElement('link');
    theme.rel = 'stylesheet';
    theme.href = 'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism.min.css';
    document.head.appendChild(theme);

    const lineCss = document.createElement('link');
    lineCss.rel = 'stylesheet';
    lineCss.href = 'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/line-numbers/prism-line-numbers.css';
    document.head.appendChild(lineCss);

    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js';
    script.onload = () => {
      const auto = document.createElement('script');
      auto.src = 'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js';
      auto.onload = () => {
        const line = document.createElement('script');
        line.src = 'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/line-numbers/prism-line-numbers.min.js';
        line.onload = resolve;
        document.head.appendChild(line);
      };
      document.head.appendChild(auto);
    };
    document.head.appendChild(script);
  });
}

function copyCode() {
  navigator.clipboard.writeText(props.code);
}

onMounted(async () => {
  const el = pre.value.querySelector('code');
  if (el) {
    el.textContent = props.code;
    await loadPrism();
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
  text-shadow: none;
}

.code-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2d2d2d;
  color: #f8f8f2;
  padding: 0.25rem 0.5rem;
  font-size: 0.8rem;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  border-bottom: 1px solid #444;
}

.copy-btn {
  color: #f8f8f2;
  z-index: 100;
}
</style>
