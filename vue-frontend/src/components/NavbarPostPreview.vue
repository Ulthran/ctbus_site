<template>
  <router-link :to="link" class="nav-blog-preview">
    <v-img :src="img" width="40" height="60" cover class="rounded me-2" />
    <div class="text-left">
      <div class="text-body-2">{{ title }}</div>
      <div class="text-caption">{{ subtitle }}</div>
    </div>
  </router-link>
</template>

<script setup>
defineProps({
  link: String,
  img: String,
  title: String,
  subtitle: String,
});
</script>
