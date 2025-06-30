<template>
  <v-app>
    <v-app-bar color="secondary" dark app>
      <v-toolbar-title class="ml-0 pl-0">
        <router-link to="/" style="color: inherit; text-decoration: none;">
          <v-btn icon variant="text" router>
            <v-icon icon="fas fa-home"></v-icon>
          </v-btn>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/resume" icon variant="text" router>
        <v-icon icon="fas fa-file-alt"></v-icon>
      </v-btn>
      <v-btn href="https://github.com/Ulthran" icon variant="text" target="_blank">
        <v-icon icon="fab fa-github"></v-icon>
      </v-btn>
      <v-btn href="https://www.linkedin.com/in/charlie-bushman-8b0b59128/" icon variant="text" target="_blank">
        <v-icon icon="fab fa-linkedin"></v-icon>
      </v-btn>
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
