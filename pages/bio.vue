<template>
  <Header />
  <div class="container">
    <div class="row justify-content-center">
      <h1>PAGE BIOGRAPHIE 3</h1>
      <h1>{{ message }}</h1>
      <button @click="chargeData" class="btn btn-active btn-primary">Primary</button>

      <button @click="conversationChat" class="btn btn-active btn-primary">chat</button>


      <!-- -->

      <!-- penpot/figma/canva -->
      <div class="chat chat-start">
        <div class="chat-bubble">It's over Anakin, <br />I have the high ground.</div>
      </div>
      <div class="chat chat-end">
        <div class="chat-bubble">You underestimate my power!</div>
      </div>
      <div class="chat chat-start">
        <div class="chat-bubble">It's over Anakin, <br />I have the high ground.</div>
      </div>
      <div class="chat chat-end">
        <div class="chat-bubble">You underestimate my power!</div>
      </div>
      <div class="chat chat-start">
        <div class="chat-bubble">It's over Anakin, <br />I have the high ground.</div>
      </div>
      <div class="chat chat-end">
        <div class="chat-bubble">You underestimate my power!</div>
      </div>


    </div>
  </div>
  <Footer />
</template>

<script setup lang="ts">

const message = ref('')
const conversation = ref([])



async function conversationChat() {
  try {
    const response = await $fetch('http://localhost:8000/api/chat')
    console.debug(response)
    conversation.value = response.conversation
  } catch (error) {
    console.error(error)
    message.value = "ERROR"
  }
}


async function chargeData() {
  try {
    const response = await $fetch('http://localhost:8000/api/data')
    //console.debug(response)
    message.value = response.message
  } catch (error) {
    console.error(error)
    message.value = "ERROR"
  }
}

</script>




