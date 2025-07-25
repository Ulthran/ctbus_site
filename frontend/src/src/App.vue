<template>
  <v-app>
    <v-app-bar class="px-6" color="secondary" dark app>
      <v-toolbar-title class="ml-0 pl-0">
        <router-link to="/" style="color: inherit; text-decoration: none">
          <v-btn icon variant="text" router>
            <v-icon aria-label="Home" icon="fas fa-home"></v-icon>
          </v-btn>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        href="ASSETS_BASE_URL/documents/resume.pdf"
        icon
        variant="text"
        target="_blank"
      >
        <v-icon aria-label="Resume" icon="fas fa-file-alt"></v-icon>
      </v-btn>
      <v-btn
        href="https://github.com/Ulthran"
        icon
        variant="text"
        target="_blank"
      >
        <v-icon aria-label="GitHub" icon="fab fa-github"></v-icon>
      </v-btn>
      <v-btn
        href="https://www.linkedin.com/in/charlie-bushman-8b0b59128/"
        icon
        variant="text"
        target="_blank"
      >
        <v-icon aria-label="LinkedIn" icon="fab fa-linkedin"></v-icon>
      </v-btn>
    </v-app-bar>
    <v-main class="pa-15">
      <v-alert
        v-if="env !== 'main'"
        type="warning"
        variant="tonal"
        class="text-center m-0"
      >
        This is a dev deployment ({{ env }})
      </v-alert>
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
export default {
  name: "App",
  data() {
    return { env: "ENV_NAME" };
  },
};
</script>
