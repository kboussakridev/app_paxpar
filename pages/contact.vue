<template>
    <Header/>
    <div class="min-h-screen bg-gray-100 flex justify-center items-center">
    <div class="bg-white p-8 rounded shadow-md max-w-md w-full">
      <h1 class="text-2xl font-semibold mb-4">Contactez-nous</h1>
      <form>
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700">Nom</label>
          <input type="text" id="name" name="name" class="mt-1 p-2 border border-gray-300 rounded-md w-full" />
        </div>
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input type="email" id="email" name="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" />
        </div>
        <div class="mb-4">
          <label for="message" class="block text-sm font-medium text-gray-700">Message</label>
          <textarea id="message" name="message" rows="4" class="mt-1 p-2 border border-gray-300 rounded-md w-full"></textarea>
        </div>
        <div class="text-right">
          <button type="submit" class="py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600">Envoyer</button>
        </div>
      </form>
    </div>
  </div>
    <Footer/>
</template>
<script setup>
definePageMeta({
  middleware: ["auth"]
})
</script>