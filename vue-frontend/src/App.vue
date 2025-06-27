<template>
  <div class="min-h-screen flex flex-col bg-gray-100 text-gray-800">
    <nav class="bg-gray-700 text-white p-4">
      <div class="container mx-auto flex space-x-4">
        <router-link to="/" class="font-bold">Home</router-link>
        <router-link to="/about" class="font-bold">About</router-link>
        <router-link to="/blog" class="font-bold">Blog</router-link>
        <router-link to="/projects" class="font-bold">Projects</router-link>
      </div>
    </nav>
    <main class="flex-1">
      <router-view></router-view>
    </main>
    <footer class="bg-gray-300 text-center py-2">
      <p>Always Learning. Always Building.</p>
      <p>&copy; 2025 Charlie Bushman. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
</script>

<style>
body { margin: 0; }
</style>
