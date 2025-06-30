<script setup>
import Hero from '../components/Hero.vue'

const workCards = [
  {
    title: 'Lead Developer for Nightly',
    body: 'In college a friend pitched a party planning app for a startup competition. I built a prototype with React Native and AWS Amplify and later helped refine the web and mobile apps alongside a small team before joining the PCMP.',
    img: `CDN_URL/images/latenite_logo.png`,
  },
  {
    title: 'HPE Software Internship',
    body: 'I worked with the GreenLake team on a large scale data migration pipeline, learning Scrum and tackling challenges around flexible data ingestion and processing.',
    img: `CDN_URL/images/hpe_greenlake.png`,
    link: 'https://hpe.com/us/en/greenlake.html',
  },
  {
    title: 'Owl Labs Software Internship',
    body: 'At Owl Labs I created a unit testing framework for their Meeting Owl firmware and later built internal inventory tools.',
    img: `CDN_URL/images/owllabs.png`,
    link: 'https://owllabs.com',
  },
  {
    title: 'HepatoChem Software Internship',
    body: 'During high school I built an Access database to manage inventory for HepatoChem\'s biomimetic screening kits.',
    img: `CDN_URL/images/hepatochem.png`,
    link: 'https://hepatochem.com',
  },
]
</script>

<template>
  <Hero title="My Previous Employment" />
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8" v-for="(card, i) in workCards" :key="card.title">
        <v-card class="ma-4" :href="card.link" target="_blank">
          <v-row no-gutters>
            <v-col cols="12" md="4">
              <v-img :src="card.img" :alt="card.title" height="160" contain />
            </v-col>
            <v-col cols="12" md="8">
              <v-card-title>{{ card.title }}</v-card-title>
              <v-card-text v-html="card.body"></v-card-text>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
