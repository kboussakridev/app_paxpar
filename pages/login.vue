<script lang="ts" setup>
import { string } from 'yup'
</script>

<template>
    
    <Header />
    <main class="relative">
        <div class="concainer">
            <div class="mt-10">
                <FormField 
                label='Email'
                type='email'
                name='email'
                :validator="string().required('Email is required').email('Email is invalid.')"
                />
                <!-- :validate-on-change="true" -->
                <FormField 
                label='First Name'
                type='text'
                name='firstName'
                initial-value="John"
                :validator="string().required('First name is required').min(5, 'Minimum of 5 characters.')"
                />
                <!-- :validate-on-change="true" -->
                <FormField 
                label='Last Name'
                type='text'
                name='lastName'
                initial-value="Wick"
                :validator="string().required('Last name is required').min(5, 'Minimum of 5 characters.')"
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
            </div>
        </div>
    </main>
    <Footer/>
</template>
                
            