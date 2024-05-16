<script setup>
const name = ref("karim")
</script>

<template>
    <Header />
        <div class="container mt-3">
             <h1>Ma variable {{ name }}</h1>
        </div>
    <Footer/>
</template>

