<template>
  <v-timeline align="start">
    <v-timeline-item
      v-for="(event, index) in events"
      :key="index"
      dot-color="primary"
    >
      <template #opposite>
        {{ event.time }}
      </template>
      <div>
        <h3 class="text-h6 font-weight-bold">{{ event.title }}</h3>
        <p v-html="event.content" class="mb-2" />
        <div v-if="event.link">
          <router-link :to="event.link">
            <v-btn color="primary" variant="outlined" size="small">
              Learn more
              <i class="fas fa-arrow-right ms-2"></i>
            </v-btn>
          </router-link>
        </div>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>
<script setup>
defineProps({
  events: {
    type: Array,
    required: true,
  },
});
</script>
