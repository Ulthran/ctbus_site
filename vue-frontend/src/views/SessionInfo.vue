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
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Session Data</h1>
    <div v-for="(value,key) in sessionData" :key="key" class="mb-2">
      <code>{{ key }}: {{ value }}</code>
      <v-btn variant="text" size="x-small" class="ml-2" @click="clearKey(key)">remove</v-btn>
    </div>
  </v-container>
</template>
