<template>
    <div>
        <button class="btn bg-red-700 text-white">
            <p class="cursor-pointer" @click="logout">Logout</p>
        </button>
        
    </div>
    <div v-if="successMsg"></div>
    <div v-if="errorMsg">
        <h1>{{ errorMsg }}</h1>
    </div>
</template>

<script setup>
const supabase = useSupabaseClient()
const user = useSupabaseUser()
const successMsg = ref(false)
const errorMsg = ref(false)

const logout = async () => {
    const { error } = await supabase.auth.singUp()
    if (error) {
        errorMsg.value = error.message
        return
    }

    successMsg.value = 'Hope to see you again soon, Redirecting...'
    setTimeout(async () => {
        successMsg.value = null
        await navigateTo('/')
    }, 2000)
}

definePageMeta({
    middleware: ["auth"],
})

</script>

<style lang="scss" scoped></style>