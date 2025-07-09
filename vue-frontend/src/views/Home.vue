<script setup>
import Hero from "../components/Hero.vue";
import Frisbee from "../svgs/Frisbee.vue";

const certs = [
  {
    href: "https://www.credly.com/badges/bcecce87-e9f9-4f05-a068-40eeb7474731/public_url",
    src: `CDN_URL/certificates/aws_certified_cloud_practitioner.png`,
    alt: "AWS Certified Cloud Practitioner - Foundational",
    h: 120,
    w: 120,
    offset: 0,
  },
  {
    href: "https://www.credly.com/badges/a5cc21ee-a95c-4ba8-9a04-9f1f7e4928bf/public_url",
    src: `CDN_URL/certificates/aws_certified_ai_practitioner_early_adopter.png`,
    alt: "AWS Certified AI Practitioner",
    h: 205,
    w: 205,
    offset: -25,
  },
  {
    href: "https://www.credly.com/badges/c6ee2c89-f5d2-46df-826e-b2246435709f/public_url",
    src: `CDN_URL/certificates/aws_certified_developer_associate.png`,
    alt: "AWS Certified Developer - Associate",
    h: 120,
    w: 120,
    offset: 0,
  },
  {
    href: "https://www.credly.com/badges/3decec7b-025c-4f64-a461-01d7d0fd6c22/public_url",
    src: `CDN_URL/certificates/aws_certified_devops_pro.png`,
    alt: "AWS Certified DevOps Engineer - Professional",
    h: 120,
    w: 120,
    offset: 0,
  },
];

const buttons = [
  { to: "/pcmp", label: "Work", icon: "fas fa-briefcase" },
  { to: "/projects", label: "Projects", icon: "fas fa-project-diagram" },
  { to: "/blog", label: "Blog", icon: "fas fa-code" },
  { to: "/certifications", label: "Certs", icon: "fas fa-certificate" },
  { to: "/education", label: "Education", icon: "fas fa-graduation-cap" },
  { to: "/past-work", label: "Past Work", icon: "fas fa-history" },
  { to: "/sports", label: "Sports", icon: "fas fa-futbol" },
  { to: "/music", label: "Music", icon: "fas fa-music" },
];
</script>

<template>
  <Hero
    title="Charlie Bushman"
    subtitle="Full-Stack Software Engineer with Cloud, DevOps, and Python expertise. Impactful results pushing projects from ideation, to creation, to production. Always eager to learn new technologies, fields, and fun facts."
  >
    <v-row justify="center" class="mt-4">
      <router-link to="/resume">
        <v-btn
          color="green-darken-2"
          variant="elevated"
          aria-label="View Charlie Bushman's resume"
          >View Resume</v-btn
        >
      </router-link>
    </v-row>
    <v-row justify="space-evenly" class="my-4">
      <v-col cols="auto" v-for="cert in certs" :key="cert.href">
        <a :href="cert.href" target="_blank" rel="noopener noreferrer">
          <v-img
            :src="cert.src"
            :alt="cert.alt"
            loading="lazy"
            :height="cert.h"
            :width="cert.w"
            :style="{ marginTop: cert.offset + 'px' }"
            contain
          />
        </a>
      </v-col>
    </v-row>
  </Hero>

  <v-container class="text-center">
    <v-row justify="center">
      <v-col cols="auto" v-for="btn in buttons" :key="btn.to">
        <router-link :to="btn.to">
          <v-btn color="green-darken-2" class="ma-2" variant="elevated">
            {{ btn.label }}
            <span class="ms-2">
              <component
                v-if="btn.component"
                :is="btn.component"
                :size="16"
                :mode="light"
              />
              <i v-else :class="btn.icon"></i>
            </span>
          </v-btn>
        </router-link>
      </v-col>
    </v-row>
  </v-container>

  <v-container class="text-center">
    <h2 class="text-h6 font-weight-bold mb-4">Get In Touch</h2>
    <p class="mb-4">
      Feel free to reach out at
      <a href="mailto:ctbushman@gmail.com">ctbushman@gmail.com</a>
    </p>
  </v-container>
</template>
