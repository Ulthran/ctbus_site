<script setup>
import Hero from "../components/Hero.vue";
</script>

<template>
  <Hero
    title="Software Engineer, HAX Team"
    subtitle="WHOOP"
  />

  <v-container class="text-center">
    <v-row>
      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">About WHOOP</h2>
        <p>
          WHOOP is a performance optimization company that makes wearable
          fitness trackers focused on recovery, strain, and sleep. The platform
          helps athletes and everyday users understand their bodies and optimize
          performance through continuous biometric monitoring.
        </p>
      </v-col>

      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">About the HAX Team</h2>
        <p>
          The Hardware Accelerate (HAX) team works at the intersection of
          software and hardware, building the systems and tooling that power
          WHOOP&#39;s devices. The team focuses on accelerating hardware
          development and ensuring the software stack performs reliably on
          embedded platforms.
        </p>
      </v-col>

      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">My Role</h2>
        <p>
          As a Software Engineer on the HAX team, I work on the software systems
          that support WHOOP&#39;s hardware products. This role builds on my
          background in building reliable, production-grade software while
          expanding into the embedded and hardware domains.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>
