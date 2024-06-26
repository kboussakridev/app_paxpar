<template>
    <Header/>
    <div>
        
        <h1>Check your email to confirm Registration</h1>
    </div>
    <Footer/>
    
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"]
})
const user = useSupabaseUser()

watch(user, () => {
  if (user.value) {
      // Redirect to protected page
      return navigateTo('/')
  }
}, { immediate: true })
</script>