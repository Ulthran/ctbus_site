<script setup>
import ProjectHero from '../components/ProjectHero.vue'
const projects = window.projects

const info = projects['ctbus-site']

const badges = [
  {
    href: 'https://github.com/Ulthran/ctbus_site/actions/workflows/main.yml',
    src: 'https://github.com/Ulthran/ctbus_site/actions/workflows/main.yml/badge.svg',
    alt: 'CI/CD',
  },
  { href: 'https://www.mend.io/renovate/', src: 'https://img.shields.io/badge/renovate-enabled-brightgreen.svg', alt: 'Renovate' },
  { href: 'https://app.codacy.com/gh/Ulthran/ctbus_site/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade',
    src: 'https://app.codacy.com/project/badge/Grade/07edb64af1c544439190dff82571e7a5', alt: 'Codacy' },
  { href: 'https://snyk.io/test/github/Ulthran/ctbus_site', src: 'https://snyk.io/test/github/Ulthran/ctbus_site/badge.svg', alt: 'Snyk' },
]
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`CDN_URL/images/${info.image}`"
  />
  <v-container>
    <h2 class="text-h6 font-weight-bold mb-2">Overview</h2>
    <p>
      It's my website! I've spent a lot of time working on this, evolving it into the thing you see now.
      Not all of it is pretty, there are ideas and remnants of ideas floating around places. But I'm proud of it and I like working on it.
      Hopefully you like it and find what you came here looking for. :)
    </p>

    <h2 class="text-h6 font-weight-bold mt-4 mb-2">Dev</h2>
    <p>
      A Vue site deployed through AWS S3 and CloudFront using Terraform for infrastructure management.
      It began as a PHP-based site using Laravel and running on an EC2 instance.
      From there it progressed to being a collection of statically sourced HTML pages from an S3 bucket.
      The next step was making it dynamic and "serverless" with Flask, stylized with Tailwind CSS, and Zappa.
      And then to it's current, properly serverless incarnation.
      There are absolutely no fun easter-eggs so don't bother looking.
    </p>
    <v-row class="my-2" justify="center">
      <v-col cols="auto" v-for="badge in badges" :key="badge.href">
        <a :href="badge.href" target="_blank" rel="noopener noreferrer">
          <v-img :src="badge.src" :alt="badge.alt" height="24" contain />
        </a>
      </v-col>
    </v-row>

    <h2 class="text-h6 font-weight-bold mt-4 mb-2">Links</h2>
    <v-row>
      <v-col cols="auto">
        <a href="https://charliebushman.com" target="_blank" title="charliebushman.com">
          <v-btn variant="text" icon>
            <i class="fas fa-globe"></i>
          </v-btn>
        </a>
      </v-col>
      <v-col cols="auto">
        <a href="https://github.com/Ulthran/ctbus_site" target="_blank" title="GitHub Repo">
          <v-btn variant="text" icon>
            <i class="fab fa-github"></i>
          </v-btn>
        </a>
      </v-col>
    </v-row>
  </v-container>
</template>
