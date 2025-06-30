<script setup>
import ProjectHero from '../components/ProjectHero.vue'
import projects from '../data/projects.json'

const info = projects['ctbus-finance']
const CDN_URL = 'CDN_URL'
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`${CDN_URL}/images/${info.image}`"
  />
  <v-container>
    <h2 class="text-h6 font-weight-bold mb-2">Overview</h2>
    <p>
      Just a minimal example of using Python and SQL for some personal data management.
      Sometimes you just don't need to go any fancier.
    </p>

    <h2 class="text-h6 font-weight-bold mt-4 mb-2">Dev</h2>
    <p>
      The data model is built using SQLAlchemy. Pandas for ingesting data from CSVs
      and Yahoo finance for hydrating market values. SQLite for the database.
    </p>

    <h2 class="text-h6 font-weight-bold mt-4 mb-2">Links</h2>
    <v-row>
      <v-col cols="auto">
        <router-link to="/blog/ctbus-finance">
          <v-btn variant="text" icon>
            <i class="fas fa-globe"></i>
          </v-btn>
        </router-link>
      </v-col>
      <v-col cols="auto">
        <a href="https://github.com/Ulthran/ctbus_finance" target="_blank" title="GitHub Repo">
          <v-btn variant="text" icon>
            <i class="fab fa-github"></i>
          </v-btn>
        </a>
      </v-col>
    </v-row>
  </v-container>
</template>
