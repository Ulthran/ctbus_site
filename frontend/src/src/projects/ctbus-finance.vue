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
        An example of using Beancount for personal finance tracking. Through the
        magic of double-entry accounting, I can see all of the money that moves
        through me and my accounts.
      </v-card-text>
    </v-card>

    <v-card class="mb-4">
      <v-card-title>Dev</v-card-title>
      <v-card-text>
        The core of the project is Beancount, a double-entry accounting system
        that uses a text-based input file to track accounts and transactions. I
        use Python scripts and custom importers to pull in data from bank
        accounts, credit cards, investment accounts, etc. All of this can then
        be seen in a local dashboard run with Fava.
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
