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
  

  components: [
    {
      path: '~/components/ui',
      extensions: ['.vue'],
      prefix: '',
    },
    {
      path: '~/components',
      extensions: ['.vue'],
      prefix: '',
    },
  ],

  modules: [
    "@nuxt/ui",
    "@nuxtjs/supabase",
    '@vueuse/nuxt',
    "@nuxtjs/tailwindcss",
    "@vee-validate/nuxt",
    "@nuxt/image"
  ],
  veeValidate: {
    autoImports : true
  },
  vite: {
    optimizeDeps: {
      include: ['@supabase/gotrue-js']
    }
  },
  supabase: {
    url: process.env.SUPABASE_URL,
    key: process.env.SUPABASE_KEY,
    redirect: false,
    redirectOptions: {
      login: '/login',
      callback: '/confirm',
      include: undefined,
      exclude: [],
      cookieRedirect: false,
    }
  }

  
})