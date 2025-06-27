<script setup>
import Hero from '../components/Hero.vue'
const CDN_URL = window.CDN_URL || ''
</script>

<template>
  <Hero
    title="Charlie Bushman"
    subtitle="Full-Stack Software Engineer with Cloud, DevOps, and Python expertise. Impactful results pushing projects from ideation, to creation, to production. Always eager to learn new technologies, fields, and fun facts."
  >
    <div class="flex flex-row justify-center items-center">
      <a href="https://www.credly.com/badges/bcecce87-e9f9-4f05-a068-40eeb7474731/public_url" target="_blank">
        <img :src="`${CDN_URL}/certificates/aws_certified_cloud_practitioner.png`" alt="AWS Certified Cloud Practitioner - Foundational" class="px-4" height="150" width="150" />
      </a>
      <a href="https://www.credly.com/badges/a5cc21ee-a95c-4ba8-9a04-9f1f7e4928bf/public_url" target="_blank">
        <img :src="`${CDN_URL}/certificates/aws_certified_ai_practitioner_early_adopter.png`" alt="AWS Certified AI Practitioner" class="px-4" height="180" width="180" />
      </a>
      <a href="https://www.credly.com/badges/c6ee2c89-f5d2-46df-826e-b2246435709f/public_url" target="_blank">
        <img :src="`${CDN_URL}/certificates/aws_certified_developer_associate.png`" alt="AWS Certified Developer - Associate" class="px-4" height="150" width="150" />
      </a>
      <a href="https://www.credly.com/badges/3decec7b-025c-4f64-a461-01d7d0fd6c22/public_url" target="_blank">
        <img :src="`${CDN_URL}/certificates/aws_certified_devops_pro.png`" alt="AWS Certified DevOps Engineer - Professional" class="px-4" height="150" width="150" />
      </a>
    </div>
  </Hero>

  <div class="container flex flex-wrap mx-auto md:w-1/2 p-4 justify-center items-center">
    <router-link to="/pcmp" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[40px] m-4">
      Work&nbsp;&nbsp;&nbsp;&nbsp;<span class="ml-2"><i class="fas fa-briefcase"></i></span>
    </router-link>
    <router-link to="/blog" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[40px] m-4">
      Blog&nbsp;&nbsp;&nbsp;&nbsp;<span class="ml-2"><i class="fas fa-code"></i></span>
    </router-link>
    <router-link to="/projects" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[50px] m-4">
      Projects<span class="ml-2"><i class="fas fa-project-diagram"></i></span>
    </router-link>
    <router-link to="/certifications" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[50px] m-4">
      Certs&nbsp;&nbsp;&nbsp;<span class="ml-2"><i class="fas fa-certificate"></i></span>
    </router-link>
    <router-link to="/education" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[50px] m-4">
      Education<span class="ml-2"><i class="fas fa-graduation-cap"></i></span>
    </router-link>
    <router-link to="/past-work" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[50px] m-4">
      Past Work<span class="ml-2"><i class="fas fa-history"></i></span>
    </router-link>
    <router-link to="/sports" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[50px] m-4">
      Sports&nbsp;&nbsp;<span class="ml-2"><i class="fas fa-football-ball"></i></span>
    </router-link>
    <router-link to="/music" class="interest-button flex items-center bg-green-700 hover:bg-green-800 text-white text-lg font-bold font-mono py-2 px-4 rounded h-[40px] m-4">
      Music&nbsp;&nbsp;&nbsp;<span class="ml-2"><i class="fas fa-music"></i></span>
    </router-link>
  </div>

  <div class="container mx-auto p-4 text-center">
    <h2 class="text-2xl font-bold mb-4">Get In Touch</h2>
    <p class="mb-4">Feel free to reach out at <a href="mailto:ctbushman@gmail.com" class="font-medium text-blue-600 underline dark:text-blue-500 hover:no-underline">ctbushman@gmail.com</a></p>
  </div>
</template>
