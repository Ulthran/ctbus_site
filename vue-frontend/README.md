# Vue 3 + Vite

This front-end is built with [Vue 3](https://vuejs.org/) and [Vite](https://vitejs.dev/).

## Getting started

From this directory run:

```bash
npm install
npm run dev
```

This starts Vite's development server so you can visit the site locally. Opening
`index.html` directly without running the dev server results in errors like
`Failed to resolve module specifier "vue"` because the modules are unbundled.

To create a production build run:

```bash
npm run build
npm run preview
```

`npm run preview` serves the built files from `dist/` so you can verify the
output before deploying.

The production build expects Vue and Vue Router to be provided from a CDN. The
default `index.html` includes links to `https://unpkg.com/vue@3/dist/vue.global.prod.js`
and `https://unpkg.com/vue-router@4/dist/vue-router.global.prod.js`. These
scripts must be available at runtime when hosting the generated files from S3.
