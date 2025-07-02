<script setup>
import SimplePage from '../components/SimplePage.vue'

const primaryCerts = [
  {
    href: 'https://www.credly.com/badges/bcecce87-e9f9-4f05-a068-40eeb7474731/public_url',
    src: `CDN_URL/certificates/aws_certified_cloud_practitioner.png`,
    alt: 'AWS Certified Cloud Practitioner - Foundational',
    h: 130,
    w: 130,
    offset: 0,
  },
  {
    href: 'https://www.credly.com/badges/a5cc21ee-a95c-4ba8-9a04-9f1f7e4928bf/public_url',
    src: `CDN_URL/certificates/aws_certified_ai_practitioner_early_adopter.png`,
    alt: 'AWS Certified AI Practitioner',
    h: 215,
    w: 215,
    offset: -30,
  },
  {
    href: 'https://www.credly.com/badges/c6ee2c89-f5d2-46df-826e-b2246435709f/public_url',
    src: `CDN_URL/certificates/aws_certified_developer_associate.png`,
    alt: 'AWS Certified Developer - Associate',
    h: 130,
    w: 130,
    offset: 0,
  },
  {
    href: 'https://www.credly.com/badges/3decec7b-025c-4f64-a461-01d7d0fd6c22/public_url',
    src: `CDN_URL/certificates/aws_certified_devops_pro.png`,
    alt: 'AWS Certified DevOps Engineer - Professional',
    h: 130,
    w: 130,
    offset: 0,
  },
  {
    href: 'https://www.credly.com/badges/23e89c9d-02de-49e3-9634-a21816ea29b2/public_url',
    src: `CDN_URL/certificates/ibm_data_engineering_badge.png`,
    alt: 'IBM Data Engineering Specialization',
    h: 130,
    w: 130,
    offset: 0,
  },
]

const extraCerts = {
  'AWS SkillBuilder': [
    {
      href: 'CDN_URL/certificates/aws_security_compliance_governance_for_ai.pdf',
      title: "Security, Compliance, and Governance for AI Solutions ('25)",
    },
    {
      href: 'CDN_URL/certificates/aws_optimizing_foundation_models.pdf',
      title: "Optimizing Foundation Models ('25)",
    },
    {
      href: 'CDN_URL/certificates/aws_essentials_of_prompt_engineering.pdf',
      title: "Essentials of Prompt Engineering ('25)",
    },
    {
      href: 'CDN_URL/certificates/aws_developing_gen_ai_solutions.pdf',
      title: "Developing Generative Artificial Intelligence Solutions ('25)",
    },
    {
      href: 'CDN_URL/certificates/aws_developing_ml_solutions.pdf',
      title: "Developing Machine Learning Solutions ('25)",
    },
    {
      href: 'CDN_URL/certificates/aws_responsible_ai_practices.pdf',
      title: "Responsible Artificial Intelligence Practices ('25)",
    },
    {
      href: 'CDN_URL/certificates/aws_exploring_ai_use_cases_and_applications.pdf',
      title: "Exploring Artificial Intelligence Use Cases and Applications ('25)",
    },
    {
      href: 'CDN_URL/certificates/aws_fundamentals_of_ai_and_ml.pdf',
      title: "Fundamentals of Machine Learning and Artificial Intelligence ('25)",
    },
  ],
  'LinkedIn Learning': [
    { href: 'CDN_URL/certificates/aws_mls_c01_prep.pdf', title: "AWS Machine Learning ('23)" },
    { href: 'CDN_URL/certificates/devops_foundations_cicd.pdf', title: "DevOps Foundations: CI/CD ('23)" },
    { href: 'CDN_URL/certificates/learning_amazon_web_services_for_developers.pdf', title: "Learning AWS for Developers ('23)" },
    { href: 'CDN_URL/certificates/learning_docker.pdf', title: "Docker ('23)" },
    { href: 'CDN_URL/certificates/learning_docker_compose.pdf', title: "Docker Compose ('23)" },
    { href: 'CDN_URL/certificates/25_github_configuration_files_you_should_be_using.pdf', title: "25 GitHub Configuration Files You Should Be Using ('23)" },
    { href: 'CDN_URL/certificates/scrum_master.pdf', title: "Scrum Master ('23)" },
    { href: 'CDN_URL/certificates/supporting_allyship_and_antiracism_at_work.pdf', title: "Supporting Allyship and Antiracism at Work ('23)" },
    { href: 'CDN_URL/certificates/strategic_thinking.pdf', title: "Strategic Thinking ('23)" },
  ],
  'Techstrong Learning': [
    { href: 'CDN_URL/certificates/build_AI_native_foundation.pdf', title: "AI-Native Foundations for Enterprise Apps ('24)" },
    { href: 'CDN_URL/certificates/future_of_AI_assisted_dev_and_code_qual_cert.pdf', title: "Future of AI Assisted Development and Code Quality ('23)" },
  ],
  'Misc and Old': [
    { href: 'CDN_URL/certificates/IBM_quantum_challenge_fall_2020.pdf', title: "IBM - Quantum Challenge - Foundational ('20)" },
    { href: 'CDN_URL/certificates/scala_lang_prof.pdf', title: "Lightbend Scala Language - Professional ('20)" },
    { href: 'https://projecteuler.net/profile/Ulthran.png', title: 'Project Euler (Top 5%)' },
  ],
}
</script>

<template>
  <SimplePage title="Certifications">
    <v-row class="my-4" justify="center" align="center">
      <v-col cols="auto" v-for="cert in primaryCerts" :key="cert.href">
        <a :href="cert.href" target="_blank">
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

    <h2 class="text-h6 font-weight-bold mt-6">Extra Learning and Practice</h2>
    <div v-for="(list, name) in extraCerts" :key="name" class="my-4">
      <h3 class="text-subtitle-1 mb-2">{{ name }}</h3>
      <div class="d-flex flex-wrap justify-center">
        <v-chip
          v-for="cert in list"
          :key="cert.href"
          class="ma-1"
          size="small"
          variant="outlined"
        >
          <a :href="cert.href" target="_blank" class="text-decoration-none" rel="noopener noreferrer">{{ cert.title }}</a>
        </v-chip>
      </div>
    </div>
  </SimplePage>
</template>
