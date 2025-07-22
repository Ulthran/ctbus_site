<script setup>
import Hero from "../components/Hero.vue";
import Timeline from "../components/Timeline.vue";

const timelineEvents = [
  {
    time: "Jan 2022",
    title: "Developer in Statistical Metagenomics",
    content:
      "My position with the Penn-CHOP Microbiome Program has honed my <b>software development skills</b> and expanded my knowledge about <b>bioinformatics and statistics</b>. It has also shown me how to have an outsized impact on research and development on the basis of my unique skillset, namely driving software standards, encouraging well structured data/metadata, and building the infrastructure to support it.",
    link: "/pcmp",
  },
  {
    time: "Jun 2021",
    title: "Lead Developer for Nightly",
    content:
      "This was where I experienced for the first time seeing something missing from the world and then creating a product to fill that gap. Before this, all my projects had been academic, the ends were just themselves and I knew they had been done before. After, I started to see every bad UX, every missing feature or platform, as opportunities and as gaps that I could conceivably fill. This was also the first time I had to take on the role of a <b>product owner</b> and spend more of my time thinking about the user experience than working out bugs.",
    link: "/past-work#Lead%20Developer%20for%20Nightly",
  },
  {
    time: "Jun 2021",
    title: "Graduated Carleton College",
    content:
      "Physics Major.<br />GPA: 3.66.<br />Two years as captain of DIII frisbee team (best finish 3rd at nationals) and two years as head of the standup group.<br />Prototyped Nightly for startup competition and was among finalists.",
  },
  {
    time: "Jun 2020",
    title: "Internship at HPE",
    content:
      "At HPE I got to experience working with a <b>Scrum team</b> for the first time. Unlike with many other interns, my manager, after some training and certification, put me right to work as a member of the team which was awesome for so many reasons. I got to learn first hand how Scrum teams work (and sometimes don't work), both the theory and the practice of large scale <b>data pipelines</b>, and how to approach each unit of development work with the dual focuses of how to make it work in a vacuum and have it effectively integrate into the larger system.",
    link: "/past-work#HPE%20Software%20Internship",
  },
  {
    time: "Jun 2018",
    title: "Internship at Owl Labs",
    content:
      "This internship was my first experience with a professional software environment. And it taught me a lot of skills that I now take for granted such as how to work at the command line, how to use git, and how to apply a <b>testing framework</b> to a large codebase.",
    link: "/past-work#Owl%20Labs%20Software%20Internship",
  },
  {
    time: "Jul 2017",
    title: "Graduated Marblehead High School",
    content: "",
  },
  {
    time: "Jul 2016",
    title: "Internship at HepatoChem",
    content:
      "I was fortunate to spend two summers and a winter of high school working with the awesome biochemists of HepatoChem. It was here that I first gained experience with lab work (just a little bit), practical database implementation, and the importance of good information infrastructure for <b>inventory management</b>. They were using Excel for all of their order and inventory management when I arrived and I was able to create a simple Access database that could handle the same tasks and compile safety data sheets for each kit. That system is still in use today.",
    link: "/past-work#HepatoChem%20Software%20Internship",
  },
  { time: "Oct 1998", title: "I was born", content: "Self explanatory." },
];
</script>

<template>
  <Hero
    title="About Me"
    subtitle="Building the infrastructure behind <b>reliable</b>, <b>reproducible</b>, and <b>high performance</b> research and development."
  />
  <v-container class="pt-0 pb-10">
    <Timeline :events="timelineEvents" />
  </v-container>
</template>
