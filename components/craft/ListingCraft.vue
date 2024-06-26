<script setup>
const props = defineProps({
  listing: Object,
});
</script>

<template>
  <div class="shadow rounded overflow-hidden flex justify-between mb-4">
    <div class="flex">
      <img :src="listing.url" alt="" class="w-80 mr-3 h-44" />
      <div class="p-3">
        <h1 class="text-2xl"></h1>
        <p class="text-blue-400"></p>
      </div>
    </div>
    <div class="p-3 flex">
      <NuxtLink
        class="text-blue-400 mr-4"
        :to="`/profile/listings/view/`"
        >View</NuxtLink
      >
      <p class="text-red-400 cursor-pointer">Delete</p>
    </div>
  </div>
</template>