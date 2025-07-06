<script setup>
const posts = window.posts;
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Blog</h1>
    <v-list>
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
            <v-img
              :src="`CDN_URL/images/blog/${name.replace(/-/g, '_')}.png`"
              :alt="post.title"
              cover
              loading="lazy"
            ></v-img>
          </v-avatar>
        </template>
        <v-list-item-title>{{ post.title }}</v-list-item-title>
        <v-list-item-subtitle>{{ post.subtitle }}</v-list-item-subtitle>
        <v-list-item-subtitle class="text-caption">
          {{ post.date }}
          <span v-if="post.mod_date !== post.date"
            >(Edited: {{ post.mod_date }})</span
          >
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          <div class="d-flex flex-wrap">
            <v-chip
              v-for="tag in post.tags"
              :key="tag"
              class="ma-1"
              size="x-small"
              variant="outlined"
            >
              {{ tag }}
            </v-chip>
          </div>
        </v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-container>
</template>
