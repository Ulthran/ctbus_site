<script setup>
import { ref } from 'vue'
const sessionData = ref(JSON.parse(localStorage.getItem('session') || '{}'))
function clearKey(key){
  const data = JSON.parse(localStorage.getItem('session') || '{}')
  delete data[key]
  localStorage.setItem('session', JSON.stringify(data))
  sessionData.value = data
}
</script>

<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Session Data</h1>
    <div v-for="(value,key) in sessionData" :key="key" class="mb-2">
      <span class="font-mono">{{ key }}: {{ value }}</span>
      <button class="ml-2 text-blue-600 underline" @click="clearKey(key)">remove</button>
    </div>
  </div>
</template>
