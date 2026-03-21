<script setup>
import Hero from "../components/Hero.vue";
</script>

<template>
  <Hero title="Software Engineer, HAX Team" subtitle="WHOOP" />

  <v-container class="text-center">
    <v-row>
      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">About WHOOP</h2>
        <p>
          WHOOP makes a leading wearable fitness & health tracker focused on
          recovery, strain, and sleep. The platform helps athletes and everyday
          users understand their bodies and optimize performance and health
          through continuous biometric monitoring.
        </p>
      </v-col>

      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">About the HAX Team</h2>
        <p>
          The Hardware Accelerate (HAX) team works at the intersection of
          software, hardware, and signal processing. We build the systems and
          tooling that power WHOOP&#39;s devices. The team focuses on
          accelerating the flow of data from studies to development work.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>
