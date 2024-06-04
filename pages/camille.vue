<script setup lang="ts">

async function getMyInvoice() {
    // appel API
    console.debug("appel API ...")
    //const data = await $fetch('http://localhost:8000/camille')
    const data = await useFetch('http://localhost:8000/camille')
    console.debug({data})
}
</script>

<template>
    <div />
    <h1>PAGE CAMILLE</h1>
    <button>Facture PDF</button>

    <button @click="getMyInvoice" class="btn btn-active">
        <span class="loading loading-spinner"></span>
        loading
    </button>
    <div />

</template>