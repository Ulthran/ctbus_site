<template>
  <div class="honeycomb">
    <div
      v-for="(layer, index) in layers"
      :key="index"
      class="hex-row"
      :class="{ offset: index % 2 === 1 }"
    >
      <div v-for="skill in layer" :key="skill.label" class="hex">
        <div class="hex-inner">
          <i :class="skill.icon" class="hex-icon"></i>
          <span class="hex-label">{{ skill.label }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  layers: {
    type: Array,
    required: true,
  },
});
</script>

<style scoped>
.honeycomb {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.hex-row {
  display: flex;
}
.hex-row.offset {
  margin-left: 55px;
}
.hex {
  width: 110px;
  height: 63px;
  margin: 31.5px 5px;
  position: relative;
}
.hex-inner {
  width: 100%;
  height: 100%;
  background-color: var(--v-theme-primary, #2e7d32);
  clip-path: polygon(50% 0%, 93% 25%, 93% 75%, 50% 100%, 7% 75%, 7% 25%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
}
.hex-icon {
  font-size: 24px;
  line-height: 1;
}
.hex-label {
  font-size: 0.75rem;
}
@media (max-width: 600px) {
  .hex-row.offset {
    margin-left: 27px;
  }
  .hex {
    width: 60px;
    height: 34px;
    margin: 17px 3px;
  }
  .hex-icon {
    font-size: 16px;
  }
  .hex-label {
    font-size: 0.55rem;
  }
}
</style>
