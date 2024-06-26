<script setup>
definePageMeta({
    middleware: ["auth"],
})

const user = useSupabaseUser();
const client = useSupabaseClient();
const router = useRouter();

console.log(user.value);
async function logout() {
    try {
        const { error } = await client.auth.signOut();
    if(error) throw error;
    router.push("/login");
    } catch (error) {
        console.log(error.message);
    }
    
}

</script>

<template>
    <main class="h-screen container py-36 sm:pt-44 sm:pb-60">
        <div class="flex flex-col border-2 border-blue-400 p-10 rounded-lg bg-opacity-0">
            <h1 class="text-xl mb-2">Email: {{ user.email }}</h1>
            <button @click="logout" type="button" class="self-start btn mt-6">Logout</button>
        </div>
    </main>
</template>



<style lang="scss" scoped>

</style>