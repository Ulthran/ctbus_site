<script setup>
import { ref, computed } from "vue";

const posts = window.posts;

const search = ref("");
const selectedTag = ref(null);
const allTags = [
  ...new Set(Object.values(posts).flatMap((p) => p.tags)),
].sort();

const filteredPosts = computed(() => {
  const query = search.value.toLowerCase();
  return Object.fromEntries(
    Object.entries(posts).filter(([_, post]) => {
      const matchesSearch =
        !query ||
        post.title.toLowerCase().includes(query) ||
        post.subtitle.toLowerCase().includes(query);
      const matchesTag =
        !selectedTag.value || post.tags.includes(selectedTag.value);
      return matchesSearch && matchesTag;
    })
  );
});
</script>

<template>
  <v-container>
    <h1 class="text-h5 font-weight-bold mb-4">Blog</h1>
    <v-row class="mb-4">
      <v-col cols="12" sm="6" md="4" lg="3">
        <v-text-field
          v-model="search"
          label="Search"
          prepend-inner-icon="fas fa-search"
          hide-details
          density="compact"
          class="blog-filter"
        />
      </v-col>
      <v-col cols="12" sm="6" md="4" lg="3">
        <v-autocomplete
          v-model="selectedTag"
          :items="allTags"
          label="Filter by tag"
          clearable
          hide-details
          density="compact"
          class="blog-filter"
        />
      </v-col>
    </v-row>
    <v-list>
      <v-list-item
        v-for="(post, name) in filteredPosts"
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
              :src="`/assets/images/blog/${name.replace(/-/g, '_')}.png`"
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
