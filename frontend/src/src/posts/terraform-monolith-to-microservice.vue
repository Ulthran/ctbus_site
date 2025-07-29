<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
import CodeBlock from "../components/CodeBlock.vue";
const posts = window.posts;
const slug = "terraform-monolith-to-microservice";
const info = posts[slug];
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`ASSETS_BASE_URL/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <SectionTitle>Intro</SectionTitle>
    <Paragraph>
      This post will outline the process of migrating Terraform resources from a
      single monolithic configuration to a microservice-oriented structure.
    </Paragraph>
  </v-container>
</template>
