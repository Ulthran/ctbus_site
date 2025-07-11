<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
const posts = window.posts;
const slug = "vibe-coding-in-bioinformatics";
const info = posts[slug];
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`/assets/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <SectionTitle>AI as a Developer Tool</SectionTitle>
    
  </v-container>
</template>
