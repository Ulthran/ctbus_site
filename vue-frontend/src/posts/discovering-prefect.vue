<script setup>
import BlogHero from '../components/BlogHero.vue'
const posts = window.posts
const slug = 'discovering-prefect'
const info = posts[slug]
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`CDN_URL/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <p >Automation in academia is difficult. Once a protocol is locked down enough to be reasonably automatable, it drifts into being mundane, no longer the cutting edge, and definitely not very publishable. Despite this, primary barriers to faster progress in many data intensive academic research fields are poor data lifecycle management and lack of automated processes. Preprocessing metagenomic sequencing data to make it ready for exploratory analysis can be a complicated task and it's one that takes away hours per project from bioinformaticians who's main value should be added downstream. I was tasked with converting a large array of written preprocessing Standard Operating Procedures into an automation framework to solve this problem for the CHOP Microbiome Center Analytics Core.</p>
    <p >I settled on Airflow as the platform to build on and set about prototyping a solution. But I quickly found that Airflow was significantly overpowered for our needs and I was being forced to provision resources we would have no use for. Additionally the GUI it exposes felt old fashioned and too complex for users just trying to monitor their project's progress. I was about ready to abandon using an automation platform at all and bootstrap a cron-based script monster when I found Prefect and decided to give it a shot.</p>
    <p >Immediately, the experience was different. Getting a prototype up and running on dummy datasets took under a day and deploying a production version that handles only the first protocol followed soon after. The GUI is sleek and immediately provides the information bioinformaticians want when they check it. Implementing a simple interface with SLURM enables Prefect to leverage an internal HPC and achieve throughputs up to tens of terabytes a day (a reasonable upper bound for the sequencing core's output).</p>
    <p >Now that the fun part of standing up the core automation framework is done, we're in the process of finding out all the ways that SOPs need to change in order to be automatable. This ranges from field naming conventions to adjusting access policies to standing up whole new services for achieving metadata standardization. But as more and more of the pipeline comes into production more and more time is repurposed towards downstream analytics and publications. I'd recommend Prefect as the go to platform for any small-to-medium scale automation needs you may have.</p>
  </v-container>
</template>
