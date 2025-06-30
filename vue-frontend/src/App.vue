<template>
  <v-app>
    <v-app-bar color="secondary" dark app>
      <v-toolbar-title>
        <router-link to="/" style="color: inherit; text-decoration: none;">ctbus</router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/about" variant="text" router>About</v-btn>
      <v-btn to="/blog" variant="text" router>Blog</v-btn>
      <v-btn to="/projects" variant="text" router>Projects</v-btn>
    </v-app-bar>
    <v-main class="pa-15">
      <router-view></router-view>
    </v-main>
    <v-footer color="grey lighten-3" class="text-center py-2">
      <v-container class="py-0">
        <p>Always Learning. Always Building.</p>
        <p>&copy; 2025 Charlie Bushman. All rights reserved.</p>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
const { computed } = Vue;
const { useRouter } = VueRouter;
export default {
  name: 'App',
  setup() {
    const router = useRouter();
    return {};
  },
};
</script>
