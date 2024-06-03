# Création d'une aplication Paxpar.light

## Installation de nuxtjs
```bash
npx nuxi@latest init app_paxpar

```
## Démarage du projet
```bash
npm run dev -- --port 3000 
```
## installation de Tailwindcss, DaisyUi, Flowbite, NuxtUi, supabase et image-edge

```bash
npx nuxi@latest module add tailwindcss
npm i -D daisyui@latest
npm install flowbite
npx nuxi@latest module add ui
npm i @nuxt/image-edge
npm install @supabase/supabase-js

```
### nuxt.config.ts

```bash
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  modules: ["@nuxt/ui", 
            "@nuxtjs/supabase",
            "@nuxt/image-edge",
            "@nuxtjs/tailwindcss",
          ],
  supabase: {
    url: process.env.SUPABASE_URL,
    key: process.env.SUPABASE_KEY,
    redirect: false,
    redirectOptions: {
      login: '/login',
      callback: '/confirm',
      include: undefined,
      exclude: [],s
      cookieRedirect: false,
    }
  }
})

```
### tailwind.config.js

```bash
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')({
      charts: true,
    }),
    require('daisyui')
  ],
  
}

```
