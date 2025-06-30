<script setup>
import BlogHero from '../components/BlogHero.vue'
const posts = window.posts
const slug = 'fully-serverless-data-pipeline'
const info = posts[slug]
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :tags="info.tags"
    :img="`CDN_URL/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <p >In 2025, I started tracking everything I ingest other than water in a Google doc. I'd already been tracking my weight in a Google spreadsheet and I've worn various different HR trackers for years as well. And now I've earned the Professional AWS DevOps Engineer certification and have a lot of technologies floating around in my head that I want to practice. So I am working on creating an entirely serverless data pipeline for extracting, transforming, ingesting, and viewing all of my health data at once.</p>
    <p >I'm breaking this project down into four logical subdivisions:</p><br />
    <p >1. Extraction: The first step is creating Lambda functions that will access their assigned data sources and provide a recent chunk of the data to an SQS queue</p>
    <p >2. Transform: The second step is creating functions that will read from the queue and transform it into a format that can be ingested by the database</p>
    <p >3. Ingest: This might meld into 2. in practice, if the transform functions can push data directly to Aurora without needing another queue, we'll go with that</p>
    <p >4. Viewing: The final step is creating a serverless dashboard that will display the data in a way that is useful to me, there will be many options for this</p>
    <p >I see this pattern as being applicable to a number of projects down the line, so I want to make sure each component is sufficiently decoupled and abstracted. Given that, I'm using the Cloud Development Kit (CDK) to create the pipeline as a reusable microservice stack (plain CloudFormation templates aren't abstracted enough for the amount of configuration I want).</p>
    <p >1. How much data to extract: We either have to inform the extraction functions with the latest database entry or retrieve more than enough to fill in what's new.</p>
    <p >2. Dead letter queue: To make sure we're not losing data that fails at transform we will want to implement a dead letter queue.</p>
    <p >3. Data visualization: We have a lot of options for this. One is to use Redshift's ZeroETL integration with Aurora but that is almost definitely overpowered for the amount of data we're working with. A likely alternative is custom built serverless dashboards.</p>
  </v-container>
</template>
