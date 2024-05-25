<template>
    <Header/>
        <div class="container">
            <div>
                <label>Email address</label>
                <br>
                <input type="email" v-model="email" />
                <br>
                <label>Password</label>
                <br>
                <input type="password" v-model="password" />
                <br>
                <label>User name</label>
                <br>
                <input type="text" v-model="username" />
                <br>
                <label>Address</label>
                <br>
                <input type="text" v-model="address" />
                <br><br>
                <button @click="">Register</button>

                <div v-if="successMsg">
                    <h1>{{ successMsg }}</h1>
                </div>
                <div v-if="errorMsg">
                    <h1>{{ errorMsg }}</h1>
                </div>
            </div>
        </div>
    <Footer/>
</template>

<script setup>
import { useSupabaseClient, useSupabaseUser } from '@supabase/supabase-js'
import { useState } from '#app'



    const supabase = useSupabaseClient()
    const user = useSupabaseUser()
    const email = useState(() => null)
    const password = useState(() => null)
    const username = useState(() => null)
    const address = useState(() => null)
    const successMsg = useState(() => false)
    const errorMsg = useState(() => false)

    if (user.value) await navigateTo('/') 
        
    const signUp = async () => {
        const {data, error} = await supabase.auth.signUp  ({
            email: email.value,
            password: password.value,
            options: {
                data: {
                    full_name: username.value,
                    address: address.value
                },
                emailRedirectTo: 'http://localhost:3000'
            }
            
        })
        if (error) {
            successMsg.value = null
            errorMsg.value = error.message
            return
        }

        errorMsg.value = null
        successMsg.value = 'Redirecting...'
        setTimeout(async() => {
            successMsg.value = null
            await navigateTo('/confirm')
        }, 2000)
    }
</script>
