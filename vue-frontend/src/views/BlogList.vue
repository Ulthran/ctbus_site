<script setup>
const posts = window.posts
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
        <template v-slot:prepend>
          <v-avatar 
            class="rounded" 
            :style="{ width: '60px', height: '90px', 'border-radius': '4px' }"
          >
            <v-img :src="`CDN_URL/images/blog/${name.replace(/-/g, '_')}.png`" cover></v-img>
          </v-avatar>
        </template>
        <v-list-item-title>{{ post.title }}</v-list-item-title>
        <v-list-item-subtitle>{{ post.subtitle }}</v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-container>
</template>
