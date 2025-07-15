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
    <v-row>
      <v-col v-for="(post, name) in filteredPosts" :key="name" cols="12" md="6">
        <v-card
          class="ma-2 scrollable-card uniform-card"
          :to="`/blog/${name}`"
          link
        >
          <v-row no-gutters align="center">
            <v-col cols="auto">
              <v-img
                :src="`/assets/images/blog/${name.replace(/-/g, '_')}.png`"
                :alt="post.title"
                width="60"
                height="90"
                class="rounded"
                cover
                loading="lazy"
              />
            </v-col>
            <v-col>
              <v-card-title class="text-wrap">{{ post.title }}</v-card-title>
              <v-card-subtitle class="text-wrap">{{
                post.subtitle
              }}</v-card-subtitle>
              <div class="text-caption">
                {{ post.date }}
                <span v-if="post.mod_date !== post.date"
                  >(Edited: {{ post.mod_date }})</span
                >
              </div>
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
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
