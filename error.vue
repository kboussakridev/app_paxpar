<script setup>
import { defineProps } from 'vue';

const props = defineProps(['error']);

const handleClearError = () => {
  // Assurez-vous que clearError est défini quelque part dans votre code
  clearError({ redirect: '/' });
};
</script>

<template>
  <div class="error-page">
    <div class="error-container">
      <p class="error-code">404 {{ error.statuscode }}</p>
      <p class="oops-text">Ooops.</p>
      <p class="error-message">{{ error.message }}</p>
      <button class="clear-error-btn" @click="handleClearError">Clear Error</button>
    </div>
  </div>
</template>

<style scoped>
.error-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-image: url('~/assets/img/paxpar2_4k.png');
  background-size: 100% 100%;
  background-position: center;
}

.error-container {
  background-color: rgba(53, 59, 67, 0.9); /* Couleur de fond avec opacité pour voir l'image derrière */
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  color: #ffffff;
  border: 2px solid #57cbcc;
}

.error-code {
  font-size: 5rem;
  font-weight: bold;
  color: #57cbcc;
}

.oops-text {
  font-size: 3rem;
  color: #737f8a;
}

.error-message {
  font-size: 1.5rem;
}

.clear-error-btn {
  margin-top: 1.75rem;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  color: #353b43;
  background-color: #57cbcc;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.clear-error-btn:hover {
  background-color: #737f8a;
}
</style>
