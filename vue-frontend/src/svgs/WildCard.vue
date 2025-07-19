<template>
  <v-container>
    <svg
      :width="size"
      :height="size"
      viewBox="0 0 21 21"
      xmlns="http://www.w3.org/2000/svg"
      :fill="color"
      transform="rotate(45)"
      :stroke="color"
      stroke-width="2.1"
    >
      <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
      <g
        id="SVGRepo_tracerCarrier"
        stroke-linecap="round"
        stroke-linejoin="round"
      ></g>
      <g id="SVGRepo_iconCarrier">
        <g
          fill="none"
          fill-rule="evenodd"
          :stroke="color"
          stroke-linecap="round"
          stroke-linejoin="round"
          transform="translate(2 4)"
        >
          <path d="m8.5 8.5 4 4.107 4-4.107"></path>
          <path d="m8.5 4.5-4-4-4 3.997"></path>
          <path d="m4.5.5v12"></path>
          <path d="m12.5.5v12"></path>
        </g>
      </g>
    </svg>
  </v-container>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  size: { type: [Number, String], default: 48 },
  mode: { type: String, default: "dark" },
});
const color = computed(() => (props.mode === "light" ? "#fff" : "#000"));
</script>
