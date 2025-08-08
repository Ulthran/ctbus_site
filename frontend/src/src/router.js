import { createRouter, createWebHistory } from "vue-router";

import Home from "./views/Home.vue";
import About from "./views/About.vue";
import PastWork from "./views/PastWork.vue";
import PCMP from "./views/PCMP.vue";
import PcmpDashboard from "./views/PcmpDashboard.vue";
import Music from "./views/Music.vue";
import BlogList from "./views/BlogList.vue";
import BlogPost from "./views/BlogPost.vue";
import ProjectsList from "./views/ProjectsList.vue";
import ProjectDetail from "./views/ProjectDetail.vue";
import Sports from "./views/Sports.vue";
import Education from "./views/Education.vue";
import Certifications from "./views/Certifications.vue";
import FavoriteNumber from "./views/FavoriteNumber.vue";
import SessionInfo from "./views/SessionInfo.vue";
import Resume from "./views/Resume.vue";
import NotFound from "./views/NotFound.vue";
import Snakemake from "./views/Snakemake.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/past_work", component: PastWork },
  { path: "/pcmp", component: PCMP },
  { path: "/pcmp/dashboard", component: PcmpDashboard },
  { path: "/music", component: Music },
  { path: "/blog", component: BlogList },
  { path: "/blog/:post", component: BlogPost },
  { path: "/projects", component: ProjectsList },
  { path: "/projects/:project", component: ProjectDetail },
  { path: "/sports", component: Sports },
  { path: "/education", component: Education },
  { path: "/certifications", component: Certifications },
  { path: "/favorite-number", component: FavoriteNumber },
  { path: "/session", component: SessionInfo },
  { path: "/resume", component: Resume },
  { path: "/snakemake", component: Snakemake },
  { path: "/:pathMatch(.*)*", component: NotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
