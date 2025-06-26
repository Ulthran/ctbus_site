<script setup>
import posts from '../data/posts.json'
</script>

<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Blog</h1>
    <div v-for="(post, name) in posts" :key="name" class="mb-4">
      <router-link :to="`/blog/${name}`" class="text-blue-600 underline">
        {{ post.title }}
      </router-link>
      <p class="text-sm">{{ post.subtitle }}</p>
    </div>
  </div>
</template>
