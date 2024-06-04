<template>
    
    <div
      class="dropzone"
      @dragover.prevent="onDragOver" 
      @dragleave.prevent="onDragLeave" 
      @drop.prevent="onDrop"
    >
      <p v-if="!isDragging">Déposez vos fichiers ici</p> <!-- Message affiché lorsqu'aucun fichier n'est en cours de glissement -->
      <p v-else>Déposez les fichiers maintenant!</p> <!-- Message affiché lorsque des fichiers sont en cours de glissement -->
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue' 
  
  // Variable réactive pour suivre l'état du glissement
  const isDragging = ref(false)
  
  // Fonction appelée lorsque des fichiers sont glissés sur la zone de drop
  function onDragOver(event) {
    isDragging.value = true
  }
  
  // Fonction appelée lorsque des fichiers quittent la zone de drop
  function onDragLeave(event) {
    isDragging.value = false
  }
  
  // Fonction appelée lorsque des fichiers sont déposés dans la zone de drop
  function onDrop(event) {
    isDragging.value = false
    const files = event.dataTransfer.files // Récupération des fichiers déposés
    emit('files-dropped', files) // Émission d'un événement personnalisé avec les fichiers déposés
  }
  </script>
  
  <style scoped>
  .dropzone {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    font-size: 24px;
    z-index: 1000;
    transition: background-color 0.3s;
  }
  
  .dropzone p {
    margin: 0;
  }
  
  .dropzone.dragging {
    background-color: rgba(0, 0, 0, 0.7);
  }
  </style>
  