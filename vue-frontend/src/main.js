const options = {
    moduleCache: {
      vue: Vue,
      'vue-router': VueRouter,
    },
    async getFile(url) {
      const res = await fetch(url);
      if (!res.ok) throw Object.assign(new Error(res.statusText + ' ' + url), { res });
      return {
        getContentData: asBinary => asBinary ? res.arrayBuffer() : res.text(),
      };
    },
    addStyle(textContent) {
      const style = Object.assign(document.createElement('style'), { textContent });
      const ref = document.head.getElementsByTagName('style')[0] || null;
      document.head.insertBefore(style, ref);
    },
  };
  window.loaderOptions = options;
  window.componentsPath = './src/components';
  window.viewsPath = './src/views';
  window.postsPath = './src/posts';
  window.projectsPath = './src/projects';
  window.dataPath = './src/data';
  
  (async () => {
    const [App] = await Promise.all([
      window['vue3-sfc-loader'].loadModule('./src/App.vue', options),
    ]);
  
    const router = VueRouter.createRouter({
      history: VueRouter.createWebHistory(),
      routes: [
        { path: '/', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/Home.vue`, options) },
        { path: '/about', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/About.vue`, options) },
        { path: '/blog', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/BlogList.vue`, options) },
        { path: '/blog/:slug', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/BlogPost.vue`, options) },
        { path: '/certifications', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/Certifications.vue`, options) },
        { path: '/education', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/Education.vue`, options) },
        { path: '/favorite-numbers', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/FavoriteNumber.vue`, options) },
        { path: '/music', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/Music.vue`, options) },
        { path: '/past-work', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/PastWork.vue`, options) },
        { path: '/pcmp', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/PCMP.vue`, options) },
        { path: '/projects', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/ProjectList.vue`, options) },
        { path: '/projects/:slug', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/ProjectDetail.vue`, options) },
        { path: '/resume', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/Resume.vue`, options) },
        { path: '/sports', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/Sports.vue`, options) },
        { path: '/:pathMatch(.*)*', component: () => window['vue3-sfc-loader'].loadModule(`${window.viewsPath}/NotFound.vue`, options) },
      ],
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
  
    Vue.createApp(App).use(router).use(vuetify).mount('#app');
  })();
  