<script lang="ts" setup>
import { string } from 'yup'
const client = useSupabaseClient();
const router = useRouter();

const email = ref("");
const password = ref(null);
const errorMsg = ref(null);

async function signUp() {
    try {
        const { error } = await client.auth.signInWithPassword({
            email: email.value,
            password: password.value,
        });
        if (error) throw error;
        router.push("/profile")
    } catch (error) {
        errorMsg.value = error.message;
    }
}
</script>

<template>
    
    <Header />
    <main class="relative">
        <div class="h-screen flex border-green-700">
            <div class="flex-1 flex items-center justify-center bg-[#f1f1f1]">
            <form 
            @submit.prevent="signin"
            class="flex flex-col px-16 py-8 rounded-md shadow-lg max-w-screen-sm w-full">
            <h1 class="text-3xl mb-4 text-emerald-600">Login</h1>
            <div class="mt-10">
                <FormField 
                label='Email'
                type='email'
                name='email'
                :validator="string().required('Email is required').email('Email is invalid.')"
                />
                <!-- :validate-on-change="true" -->
                <FormField 
                label='Password'
                type='password'
                name='password'
                initial-value="***********"
                :validator="string().required('Password is required').min(10, 'Password is too short.')"
                />
                <!-- :validate-on-change="true" -->
                <!-- <FormField 
                label='First Name'
                type='text'
                name='firstName'
                initial-value="John"
                :validator="string().required('First name is required').min(5, 'Minimum of 5 characters.')"
                />
                 :validate-on-change="true"
                <FormField 
                label='Last Name'
                type='text'
                name='lastName'
                initial-value="Wick"
                :validator="string().required('Last name is required').min(5, 'Minimum of 5 characters.')"
                /> -->
                <!-- :validate-on-change="true" -->
                
            </div>
            <button @click="signUp" type="button" class="bg-green-600 btn mt-6">Logout</button>
        </form>
    </div>
        </div>
    </main>
    <Footer/>
</template>
                
            