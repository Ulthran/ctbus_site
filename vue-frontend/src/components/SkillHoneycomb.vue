<template>
  <div class="honeycomb">
    <div
      v-for="(layer, index) in layers"
      :key="index"
      class="hex-row"
      :class="{ offset: index % 2 === 1 }"
    >
      <div v-for="skill in layer" :key="skill.label" class="hex">
        <div class="hex-border">
          <div class="hex-inner">
            <i :class="skill.icon" class="hex-icon"></i>
            <span class="hex-label">{{ skill.label }}</span>
          </div>
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
.hex-row + .hex-row {
  margin-top: -15.75px;
}
.hex {
  --hex-path: polygon(50% 0%, 93% 25%, 93% 75%, 50% 100%, 7% 75%, 7% 25%);
  width: 110px;
  height: 63px;
  margin: 0;
  position: relative;
}
.hex-border {
  width: 100%;
  height: 100%;
  padding: 5px;
  background: linear-gradient(135deg, #f5f5f5, #9e9e9e);
  clip-path: var(--hex-path);
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}
.hex-inner {
  width: 100%;
  height: 100%;
  background-color: rgb(var(--v-theme-primary, 46, 125, 50));
  clip-path: var(--hex-path);
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
  .hex-row + .hex-row {
    margin-top: -8.5px;
  }
  .hex {
    width: 60px;
    height: 34px;
    margin: 0;
  }
  .hex-border {
    padding: 2px;
  }
  .hex-icon {
    font-size: 16px;
  }
  .hex-label {
    font-size: 0.55rem;
  }
}
</style>
