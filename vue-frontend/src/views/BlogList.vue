<script setup>
import posts from '../data/posts.json'
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Blog</h1>
    <v-list lines="two">
      <v-list-item
        v-for="(post, name) in posts"
        :key="name"
        :to="`/blog/${name}`"
        link
      >
        <v-list-item-title>{{ post.title }}</v-list-item-title>
        <v-list-item-subtitle>{{ post.subtitle }}</v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-container>
</template>
