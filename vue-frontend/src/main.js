const options = {
  moduleCache: {
    vue: Vue,
    "vue-router": VueRouter,
  },
  async getFile(url) {
    const res = await fetch(url);
    if (!res.ok)
      throw Object.assign(new Error(res.statusText + " " + url), { res });
    return {
      getContentData: (asBinary) => (asBinary ? res.arrayBuffer() : res.text()),
    };
  },
  addStyle(textContent) {
    const style = Object.assign(document.createElement("style"), {
      textContent,
    });
    const ref = document.head.getElementsByTagName("style")[0] || null;
    document.head.insertBefore(style, ref);
  },
};
window.loaderOptions = options;
// use absolute paths so navigation from nested routes works correctly
const basePath = "/src";
window.basePath = basePath;
window.componentsPath = `${basePath}/components`;
window.viewsPath = `${basePath}/views`;
window.postsPath = `${basePath}/posts`;
window.projectsPath = `${basePath}/projects`;
window.dataPath = `${basePath}/data`;

(async () => {
  const [App] = await Promise.all([
    window["vue3-sfc-loader"].loadModule(`${basePath}/App.vue`, options),
  ]);

  const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes: [
      {
        path: "/",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/Home.vue`,
            options,
          ),
        meta: {
          title: "Charlie Bushman - Portfolio",
          description:
            "Portfolio for Charlie Bushman showcasing resume, projects and technical blog posts.",
        },
      },
      {
        path: "/about",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/About.vue`,
            options,
          ),
        meta: { title: "About - Charlie Bushman" },
      },
      {
        path: "/blog",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/BlogList.vue`,
            options,
          ),
        meta: {
          title: "Blog - Charlie Bushman",
          description:
            "Technical articles on software engineering, DevOps and more.",
        },
      },
      {
        path: "/blog/:slug",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/BlogPost.vue`,
            options,
          ),
        meta: { title: "Blog Post - Charlie Bushman" },
      },
      {
        path: "/certifications",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/Certifications.vue`,
            options,
          ),
        meta: { title: "Certifications - Charlie Bushman" },
      },
      {
        path: "/education",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/Education.vue`,
            options,
          ),
        meta: { title: "Education - Charlie Bushman" },
      },
      {
        path: "/favorite-number",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/FavoriteNumber.vue`,
            options,
          ),
        meta: { title: "Favorite Number - Charlie Bushman" },
      },
      {
        path: "/music",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/Music.vue`,
            options,
          ),
        meta: { title: "Music - Charlie Bushman" },
      },
      {
        path: "/past-work",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/PastWork.vue`,
            options,
          ),
        meta: { title: "Past Work - Charlie Bushman" },
      },
      {
        path: "/pcmp",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/PCMP.vue`,
            options,
          ),
        meta: { title: "Work - Charlie Bushman" },
      },
      {
        path: "/projects",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/ProjectsList.vue`,
            options,
          ),
        meta: {
          title: "Projects - Charlie Bushman",
          description:
            "Explore projects designed and built by Charlie Bushman.",
        },
      },
      {
        path: "/projects/:slug",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/ProjectDetail.vue`,
            options,
          ),
        meta: { title: "Project Details - Charlie Bushman" },
      },
      {
        path: "/resume",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/Resume.vue`,
            options,
          ),
        meta: {
          title: "Resume - Charlie Bushman",
          description: "Download the resume of Charlie Bushman.",
        },
      },
      {
        path: "/sports",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/Sports.vue`,
            options,
          ),
        meta: { title: "Sports - Charlie Bushman" },
      },
      {
        path: "/:pathMatch(.*)*",
        component: () =>
          window["vue3-sfc-loader"].loadModule(
            `${window.viewsPath}/NotFound.vue`,
            options,
          ),
        meta: { title: "Not Found - Charlie Bushman" },
      },
    ],
  });

  router.afterEach((to) => {
    const defaultTitle = "Charlie Bushman - Portfolio";
    const defaultDescription =
      "Portfolio for Charlie Bushman showcasing resume, projects and technical blog posts.";
    document.title = to.meta.title || defaultTitle;
    const desc = to.meta.description || defaultDescription;
    let meta = document.querySelector("meta[name='description']");
    if (meta) {
      meta.setAttribute("content", desc);
    } else {
      meta = document.createElement("meta");
      meta.name = "description";
      meta.content = desc;
      document.head.appendChild(meta);
    }
  });

  const vuetify = Vuetify.createVuetify({
    /*theme: {
        defaultTheme: 'dark',
        themes: {
            dark: {
              colors: {
                background: '#000000',
                surface: '#1a1a2e',
                primary: '#89cff0',
                secondary: '#ffb6c1',
              },
            },
        },
      },*/
  });

  Vue.createApp(App).use(router).use(vuetify).mount("#app");
})();
