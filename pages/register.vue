<template>
  <Header/>
  <div class="page-container">
      <div class="container mx-auto p-6 max-w-md">
        <form @submit.prevent="signUp">
          <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
              <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">Register</h1>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                      Email
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                      id="email" 
                      type="email" 
                      v-model="email" 
                      placeholder="Email"
                  />
              </div>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                      Mot de passe
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" 
                      id="password" 
                      type="password" 
                      v-model="password" 
                      placeholder="******************"
                  />
              </div>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                      User Name
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                      id="userName" 
                      type="text" 
                      v-model="userName" 
                      placeholder="userName"
                  />
              </div>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                      Address
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                      id="address" 
                      type="text" 
                      v-model="address" 
                      placeholder="address"
                  />
              </div>
              <div class="flex items-center justify-between">
                <nuxt-link to="/">
                  <button 
                      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" 
                      @click="signUp"
                      type="button"
                  >
                      Valider
                  </button>
                </nuxt-link>
              </div>
              <div v-if="successMsg" class="mt-4">
                  <h1 class="text-green-500 font-bold">{{ successMsg }}</h1>
              </div>
              <div v-if="errorMsg" class="mt-4">
                  <h1 class="text-red-500 font-bold">{{ errorMsg }}</h1>
              </div>
          </div>
        </form>
      </div>
  </div>
  <Footer/>
</template>


<style scoped>
    .page-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-image: url('~/assets/img/paxpar2_4k.png');
        background-size: 100% 100%;
        background-position: center;
    }
</style>

<script setup>



const client = useSupabaseClient()
const user = useSupabaseUser()
const email = ref(null)
const password = ref(null)
const userName = ref(null)
const address = ref(null)
const successMsg = ref(false)
const errorMsg = ref(false)
const router = useRouter()



const signUp = async () => {
  const { data, error } = await client.auth.signUp({
    email: email.value,
    password: password.value,
    options: {
      data: {
        full_name: userName.value,
        address: address.value
      },
      emailRedirectTo: 'http://localhost:3000' // Assurez-vous que cette URL est correcte
    }
  })

  if (error) {
    successMsg.value = null
    errorMsg.value = error.message
    return
  }
  errorMsg.value = null
  successMsg.value = 'Redirecting...'
  setTimeout(async () => {
    successMsg.value = null
    await router.push('/confirm')
  }, 2000)
}
 
</script>
