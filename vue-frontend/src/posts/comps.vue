<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
import { onMounted, ref, watchEffect, reactive } from "vue";
const posts = window.posts;
const slug = "comps";
const info = posts[slug];

const MGtdelay = ref(2);
const MGn = ref(9.65);
const MGg = ref(1);
const MGB = ref(10);

const lorenzRunning = ref(true);

const MGPlaying = reactive({ B: false, n: false, g: false, tdelay: false });
const MGIntervals = {};

function toggleLorenz() {
  lorenzRunning.value = !lorenzRunning.value;
}

function toggleMG(key) {
  MGPlaying[key] = !MGPlaying[key];
  if (MGPlaying[key]) {
    const step = { B: 0.1, n: 0.05, g: 0.05, tdelay: 0.1 }[key];
    const min = { B: 5, n: 5, g: 0.1, tdelay: 1 }[key];
    const max = { B: 20, n: 12, g: 2, tdelay: 4 }[key];
    MGIntervals[key] = setInterval(() => {
      if (key === "B") {
        MGB.value += step;
        if (MGB.value > max) MGB.value = min;
      } else if (key === "n") {
        MGn.value += step;
        if (MGn.value > max) MGn.value = min;
      } else if (key === "g") {
        MGg.value += step;
        if (MGg.value > max) MGg.value = min;
      } else if (key === "tdelay") {
        MGtdelay.value += step;
        if (MGtdelay.value > max) MGtdelay.value = min;
      }
    }, 200);
  } else {
    clearInterval(MGIntervals[key]);
  }
}

onMounted(() => {
  const n = 100;
  const dt = 0.015;

  const system1 = { x: [], y: [], z: [] };
  const system2 = { x: [], y: [], z: [] };
  const system3 = { x: [], y: [], z: [] };

  for (let i = 0; i < n; i++) {
    system1.x[i] = Math.random() * 2 - 15;
    system1.y[i] = Math.random() * 2 - 15;
    system1.z[i] = 30 + Math.random() * 10;

    system2.x[i] = Math.random() * 2 + 13;
    system2.y[i] = Math.random() * 2 + 13;
    system2.z[i] = 30 + Math.random() * 10;

    system3.x[i] = system2.x[i];
    system3.y[i] = system2.y[i];
    system3.z[i] = system2.z[i];
  }

  function plot(id, dataX, dataZ, title) {
    return Plotly.newPlot(
      id,
      [
        {
          x: [dataX[0]],
          y: [dataZ[0]],
          mode: "markers",
          marker: { color: "#FF0000", size: 10 },
        },
        {
          x: dataX.slice(1),
          y: dataZ.slice(1),
          mode: "markers",
          marker: { color: "#0000FF", size: 3 },
        },
      ],
      {
        title: { text: title, font: { size: 14 } },
        margin: { l: 20, r: 10, t: 25, b: 20 },
        xaxis: { range: [-60, 60], showticklabels: false, zeroline: false },
        yaxis: { range: [0, 60], showticklabels: false, zeroline: false },
        plot_bgcolor: "#F3F4F6",
        paper_bgcolor: "#F3F4F6",
        showlegend: false,
      },
      { responsive: true },
    );
  }

  plot(
    "Lorenz_unlinked_2",
    system3.x,
    system3.z,
    "Unlinked Lorenz Attractor #2",
  );
  plot("Lorenz", system1.x, system1.z, "Lorenz Attractor #1");
  plot("Lorenz2", system2.x, system2.z, "Linked Lorenz Attractor #2");

  function step(sys, coupling = 0, sourceY = null) {
    const s = 10;
    const b = 8 / 3;
    const r = 28;
    for (let i = 0; i < n; i++) {
      let dx = s * (sys.y[i] - sys.x[i]);
      let dy = sys.x[i] * (r - sys.z[i]) - sys.y[i];
      let dz = sys.x[i] * sys.y[i] - b * sys.z[i];

      const xh = sys.x[i] + dx * dt * 0.5;
      const yh = sys.y[i] + dy * dt * 0.5;
      const zh = sys.z[i] + dz * dt * 0.5;

      dx = s * (yh - xh);
      dy = xh * (r - zh) - yh;
      dz = xh * yh - b * zh;

      sys.x[i] += dx * dt;
      if (sourceY) {
        sys.y[i] =
          (1 - coupling) * (sys.y[i] + dy * dt) + coupling * sourceY[i];
      } else {
        sys.y[i] += dy * dt;
      }
      sys.z[i] += dz * dt;
    }
  }

  function update() {
    if (lorenzRunning.value) {
      step(system1);
      step(system2, 0.03, system1.y);
      step(system3);

      Plotly.animate(
        "Lorenz_unlinked_2",
        {
          data: [
            { x: [system3.x[0]], y: [system3.z[0]] },
            { x: system3.x.slice(1), y: system3.z.slice(1) },
          ],
        },
        { transition: { duration: 0 }, frame: { duration: 0, redraw: false } },
      );

      Plotly.animate(
        "Lorenz",
        {
          data: [
            { x: [system1.x[0]], y: [system1.z[0]] },
            { x: system1.x.slice(1), y: system1.z.slice(1) },
          ],
        },
        { transition: { duration: 0 }, frame: { duration: 0, redraw: false } },
      );

      Plotly.animate(
        "Lorenz2",
        {
          data: [
            { x: [system2.x[0]], y: [system2.z[0]] },
            { x: system2.x.slice(1), y: system2.z.slice(1) },
          ],
        },
        { transition: { duration: 0 }, frame: { duration: 0, redraw: false } },
      );
    }

    requestAnimationFrame(update);
  }

  requestAnimationFrame(update);

  const MGnt = 1000;
  const MGdt = 0.1;

  function computeMG() {
    const x = [];
    const xd = [];
    const xd2 = [];
    x[0] = 0.5;
    for (let i = 1; i < MGtdelay.value / MGdt + 1; i++) {
      x[i] = 0.5;
    }
    for (let i = MGtdelay.value / MGdt; i < MGnt; i++) {
      const idelay = i - MGtdelay.value / MGdt;
      const frac =
        (MGB.value * x[idelay]) / (1 + Math.pow(x[idelay], MGn.value));
      const dx = frac - MGg.value * x[i - 1];
      x[i] = x[i - 1] + dx * MGdt;
    }
    for (let i = 1; i < MGnt - MGtdelay.value / MGdt; i++) {
      xd[i] = x[i + MGtdelay.value / MGdt];
    }
    for (let i = 1; i < MGnt - 2 * (MGtdelay.value / MGdt); i++) {
      xd2[i] = x[i + 2 * (MGtdelay.value / MGdt)];
    }
    return { x, xd, xd2 };
  }

  watchEffect(() => {
    const { x, xd, xd2 } = computeMG();
    Plotly.react(
      "MG",
      [
        {
          x,
          y: xd,
          z: xd2,
          mode: "markers",
          marker: { size: 2 },
          type: "scatter3d",
        },
      ],
      {
        xaxis: { range: [-5, 5], showticklabels: false, zeroline: false },
        yaxis: { range: [-5, 5], showticklabels: false, zeroline: false },
        zaxis: { range: [-5, 5], showticklabels: false, zeroline: false },
        plot_bgcolor: "#F3F4F6",
        paper_bgcolor: "#F3F4F6",
      },
    );
  });

  if (window.MathJax && window.MathJax.typeset) {
    window.MathJax.typeset();
  }
});
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`CDN_URL/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <Paragraph
      >My undergraduate thesis project on physical reservoir computing models.
      In the paper I introduce the reservoir computing framework, necessary
      grounding in ML, the characteristics of good physical reservoirs, and a
      few case studies: mechanical, electronic, and quantum. While this is still
      a relatively new field, the potential for chaotic systems prediction,
      smart mechanical sensors and more is potentially revolutionary across a
      wide range of sciences and industries. I also gave a talk that mimics the
      structure of the paper.</Paragraph
    >
    <Paragraph
      >The phenomenon of reservoir computing arises from an amazing property of
      chaotic systems: that when you link two similar chaotic systems, they
      start to align with each other. The technical definitions of most of the
      words used there can vary across contexts but at its core, that is
      reservoir computing. It's creating a chaotic system you know and using it
      to extract information from one you don't.</Paragraph
    >
    <SectionTitle>Linked Lorenz Systems</SectionTitle>
    <Paragraph
      >The Lorenz system is a classic example of a chaotic system. It's
      described by a set of three differential equations that dictate the
      evolution of the system in 3D space. The equations are:</Paragraph
    >
    <Paragraph
      >$$\frac{\delta x}{\delta t} = \sigma (y - x)$$ $$\frac{\delta y}{\delta
      t} = x (\rho - z) - y$$ $$\frac{\delta z}{\delta t} = x y - \beta
      z$$</Paragraph
    >
    <Paragraph
      >In the below plots, we can see chaotic system coupling in action. There
      are three Lorenz systems being simulated with the same parameters but the
      two on the right have different inputs from the one on the left.
      Additionally, the linked attractor #2 has one dimension of its evolution
      partially defined by attractor #1. This can be simulated according to the
      following equations:</Paragraph
    >
    <Paragraph
      >$$x_{1,t} = x_{1,t-1} + dx * dt$$ $$y_{1,t} = y_{1,t-1} + dy * dt$$
      $$z_{1,t} = z_{1,t-1} + dz * dt$$</Paragraph
    >
    <Paragraph
      >$$x_{2,t} = x_{2,t-1} + dx * dt$$ $$y_{2,t} = (1 - c)(y_{2,t-1} + dy *
      dt) + c * y_{1,t-1}$$ $$z_{2,t} = z_{2,t-1} + dz * dt$$ $$c =
      0.03$$</Paragraph
    >
    <Paragraph
      >$$x_{3,t} = x_{3,t-1} + dx * dt$$ $$y_{3,t} = y_{3,t-1} + dy * dt$$
      $$z_{3,t} = z_{3,t-1} + dz * dt$$</Paragraph
    >
    <div class="d-flex justify-center my-2">
      <v-btn size="small" icon variant="text" @click="toggleLorenz">
        <v-icon :icon="lorenzRunning ? 'fas fa-pause' : 'fas fa-play'" />
      </v-btn>
    </div>
    <div id="LorenzPlots" class="lorenz-container">
      <div id="Lorenz" class="lorenz-main">
        <!-- Plotly chart will be drawn inside this DIV -->
      </div>
      <div class="lorenz-side">
        <div id="Lorenz_unlinked_2">
          <!-- Plotly chart will be drawn inside this DIV -->
        </div>
        <div id="Lorenz2">
          <!-- Plotly chart will be drawn inside this DIV -->
        </div>
      </div>
    </div>
    <Paragraph
      >Each dot represents its own version of the system (unique starting
      points) and you can see from the highlighted red one that the dots across
      the two linked systems are drawn to each other and, even if they aren't
      always on the same side of the attractor, quickly fall into the same
      (quasi-)period. Meanwhile the unlinked system is doing its own thing, on
      its own time. And this is with a coupling constant of only
      0.03!</Paragraph
    >
    <SectionTitle>More Systems</SectionTitle>
    <Paragraph
      >The Mackey-Glass system is a single variable : $$\frac{dx}{dt} =
      \frac{\beta x(t-\tau)}{1+x(t-\tau)^n} - \gamma x(t)$$</Paragraph
    >
    <div id="MG"><!-- Plotly chart will be drawn inside this DIV --></div>
    <div class="d-flex align-center">
      <v-slider
        v-model="MGB"
        :min="5"
        :max="20"
        step="0.5"
        label="β"
        class="my-2 flex-grow-1"
        hide-details
      ></v-slider>
      <v-btn icon variant="text" size="small" @click="toggleMG('B')">
        <v-icon :icon="MGPlaying.B ? 'fas fa-pause' : 'fas fa-play'" />
      </v-btn>
    </div>
    <div class="d-flex align-center">
      <v-slider
        v-model="MGn"
        :min="5"
        :max="12"
        step="0.1"
        label="n"
        class="my-2 flex-grow-1"
        hide-details
      ></v-slider>
      <v-btn icon variant="text" size="small" @click="toggleMG('n')">
        <v-icon :icon="MGPlaying.n ? 'fas fa-pause' : 'fas fa-play'" />
      </v-btn>
    </div>
    <div class="d-flex align-center">
      <v-slider
        v-model="MGg"
        :min="0.1"
        :max="2"
        step="0.1"
        label="γ"
        class="my-2 flex-grow-1"
        hide-details
      ></v-slider>
      <v-btn icon variant="text" size="small" @click="toggleMG('g')">
        <v-icon :icon="MGPlaying.g ? 'fas fa-pause' : 'fas fa-play'" />
      </v-btn>
    </div>

    <Paragraph
      >It is a time delayed system, which means it relies on previous values of
      itself to determine its present dynamics. It is inspired by biological
      systems and is also the model used by
      <a href="https://www.nature.com/articles/ncomms1476" target="_blank"
        >L. Appeltant in his thesis work developing the first example of a
        physical system being used for reservoir computing</a
      >. He (and later in a class taught by
      <a
        href="https://umdphysics.umd.edu/people/faculty/current/item/445-rroy.html"
        target="_blank"
        >Rajarshi Roy</a
      >, I) mimicked this sytem's dynamics with a nonlinear, optoelectronic
      circuit to act as a physical reservoir computer.</Paragraph
    >
    <Paragraph
      >In the paper I also explore a mechanical system being used as a reservoir
      (a bunch of masses and springs) and a quantum computer being used as a
      reservoir. Maybe I'll write more about those here in the
      future.</Paragraph
    >
  </v-container>
</template>

<style scoped>
.lorenz-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}
.lorenz-main {
  flex: 1 1 45%;
  min-width: 300px;
  display: flex;
  align-items: center;
}
.lorenz-side {
  display: flex;
  flex-direction: column;
  flex: 1 1 45%;
  min-width: 300px;
}
.lorenz-side > div {
  flex: 1;
  min-height: 300px;
}
#Lorenz,
#Lorenz_unlinked_2,
#Lorenz2,
#MG {
  width: 100%;
  height: 300px;
  margin: 0;
}
</style>
