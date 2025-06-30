<script setup>
import posts from '../data/posts.json'
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Blog</h1>
    <div v-for="(post, name) in posts" :key="name" class="mb-4">
      <router-link :to="`/blog/${name}`" class="text-blue-600 underline">
        {{ post.title }}
      </router-link>
      <p class="text-caption">{{ post.subtitle }}</p>
    </div>
  </v-container>
</template>
