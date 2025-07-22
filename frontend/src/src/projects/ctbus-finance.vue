<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["ctbus-finance"];
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`ASSETS_BASE_URL/images/${info.image}`"
  />
  <v-container>
    <v-card class="mb-4">
      <v-card-title>Overview</v-card-title>
      <v-card-text>
        Just a minimal example of using Python and SQL for some personal data
        management. Sometimes you just don't need to go any fancier.
      </v-card-text>
    </v-card>

    <v-card class="mb-4">
      <v-card-title>Dev</v-card-title>
      <v-card-text>
        The data model is built using SQLAlchemy. Pandas for ingesting data from
        CSVs and Yahoo finance for hydrating market values. SQLite for the
        database.
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>Links</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="auto">
            <router-link to="/blog/ctbus-finance">
              <v-btn variant="text" icon>
                <i class="fas fa-globe"></i>
              </v-btn>
            </router-link>
          </v-col>
          <v-col cols="auto">
            <a
              href="https://github.com/Ulthran/ctbus_finance"
              target="_blank"
              title="GitHub Repo"
            >
              <v-btn variant="text" icon>
                <i class="fab fa-github"></i>
              </v-btn>
            </a>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>
