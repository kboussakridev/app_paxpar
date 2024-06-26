<template>
    <Header />
    <div class="page-container">
        <div class="container mx-auto p-6 max-w-md">
            <form @submit.prevent="signIn">
                <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                    <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">Login</h1>
                    <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                            Email
                        </label>
                        <input
                            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            id="email" type="email" v-model="email" placeholder="Email" />
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                            Mot de passe
                        </label>
                        <input
                            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                            id="password" type="password" v-model="password" placeholder="******************" />
                    </div>
                    <div class="flex items-center justify-between">
                        <nuxt-link to="/profile">
                            <button
                                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                                @click="signIn" type="button">
                                Valider
                            </button>
                        </nuxt-link>
                    </div>
                    <div>
                        <p class="text-center mt-3 flex justify-center">Don't have an account? <nuxt-link
                                class="font-bold" to="/register">Register</nuxt-link></p>
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
    <Footer />
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

const client = useSupabaseClient();
const router = useRouter();
const email = ref("");
const password = ref(null);
const errorMsg = ref(null);
const successMsg = ref(null);

async function signIn() {

    const { data, error } = await client.auth.signInWithPassword({
        email: email.value,
        password: password.value
    })
    if (error) {
        successMsg.value = null
        errorMsg.value = error.message
        return
    }
    errorMsg.value = null
    successMsg.value = 'Welcome Back, Redirecting...'
    setTimeout(async () => {
        successMsg.value = null
        await navigateTo('/')
    }, 2000)

}
</script>