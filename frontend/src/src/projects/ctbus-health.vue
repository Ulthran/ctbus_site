<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["ctbus-health"];
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
        A personal nutrition and health tracking system built on AWS. A Vue 3
        mobile-first dashboard lets me log everything I eat — either by typing a
        natural language description or scanning a barcode with my phone camera.
        Entries flow through an API Gateway and SQS queue to a Lambda that uses
        Claude AI, the USDA FoodData Central API, and Open Food Facts to parse
        them into structured nutrition data. The dashboard then shows daily,
        weekly, and monthly breakdowns with percent daily value (%DV) for
        calories, protein, fat, carbohydrates, fiber, sodium, and more.
      </v-card-text>
      <v-card-text> Access by allowlist only :/ </v-card-text>
    </v-card>

    <v-card class="mb-4">
      <v-card-title>Stack</v-card-title>
      <v-card-text>
        <ul>
          <li>
            <strong>Frontend:</strong> Vue 3 + Vuetify 3 (no build step),
            Cognito auth, served from S3 + CloudFront
          </li>
          <li>
            <strong>Backend:</strong> AWS API Gateway → SQS → Lambda (Python)
          </li>
          <li>
            <strong>AI:</strong> Claude via AWS Bedrock for natural-language
            food parsing
          </li>
          <li>
            <strong>Data sources:</strong> USDA FoodData Central API, Open Food
            Facts barcode database
          </li>
          <li><strong>Storage:</strong> S3 (JSON files per day + index)</li>
          <li><strong>Infrastructure:</strong> Terraform</li>
        </ul>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>Links</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="auto">
            <a
              href="https://github.com/Ulthran/ctbus_health"
              target="_blank"
              title="GitHub Repo"
            >
              <v-btn variant="text" icon>
                <i class="fab fa-github"></i>
              </v-btn>
            </a>
          </v-col>
          <v-col cols="auto">
            <a
              href="https://food.charliebushman.com"
              target="_blank"
              title="Website"
            >
              <v-btn variant="text" icon>
                <i class="fas fa-globe"></i>
              </v-btn>
            </a>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>
