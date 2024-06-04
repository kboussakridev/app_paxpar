<template>
    <Header/>
        <div class="container">
            <div class="row justify-content-center">
                <h1>PAGE BIOGRAPHIE</h1>
                <h1>{{ message }}</h1>
            </div>
        </div>
    <Footer/>
</template>

<script>
export default {
  data() {
    return {
      message: ''
    }
  },
  async fetch() {
    try {
      const response = await this.$axios.$get('http://localhost:8000/api/data')
      this.message = response.message
    } catch (error) {
      console.error(error)
    }
  }
}
</script>




