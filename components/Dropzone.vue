<template>
  <!-- Lorsque le survol du drag-and-drop se produit -->
  <!-- Lorsque le pointeur de la souris quitte la zone de drop -->
  <!-- Lorsqu'un élément est lâché dans la zone de drop -->
  <div
    class="dropzone"
    :class="{ dragging: isDragging }"
    @dragover.prevent="dragOver" 
    @dragleave.prevent="dragLeave" 
    @drop.prevent="drop($event)" 
  >
  
    <p v-if="!isDragging">Déposez vos fichiers ici</p> <!-- Si aucun fichier n'est en cours de glissement -->
    <p v-else>Déposez les fichiers maintenant!</p> <!-- Si des fichiers sont en cours de glissement -->
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'


const isDragging = ref(false) // Variable pour suivre l'état de glissement des fichiers
const emit = defineEmits(['files-dropped']) // Définition de l'événement à émettre lorsqu'un fichier est déposé

function onDragOver(event) {
  isDragging.value = true // Met à jour l'état pour indiquer qu'un fichier est en cours de glissement
}

function onDragLeave(event) {
  isDragging.value = false // Met à jour l'état pour indiquer qu'aucun fichier n'est en cours de glissement
}

function onDrop(event) {
  isDragging.value = false // Met à jour l'état pour indiquer qu'aucun fichier n'est en cours de glissement
  const files = event.dataTransfer.files //Obtient les fichiers déposés 

 // Filtrer les fichiers pour ne prendre en compte que les fichiers PDF, .odt et .xlsx
//  const validFiles = Array.from(files).filter(file => {
//     const extension = file.name.split('.').pop().toLowerCase();
//     return ['pdf', 'odt', 'xlsx'].includes(extension);
//   });

  emit('files-dropped', files) //Émet l'événement avec les fichiers déposés 
}
</script>

<style scoped>
.dropzone {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  border: blue dashed;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url('~/assets/img/paxpar2_4k.png');
  background-color: rgba(0, 0, 0, 0.5); /* Couleur de fond semi-transparente */
  background-blend-mode: multiply; /* Mélange avec l'image de fond */
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
  color: white;
  font-size: 24px;
  z-index: 1000;
  transition: background-color 0.3s;
  pointer-events: none; /* Désactiver les événements de pointeur pour permettre les clics à travers */
}
.dropzone.dragging {
  background-color: rgba(255, 255, 255, 0.7);
  pointer-events: all; /* Activer les événements de pointeur uniquement lors du glissement */
}

</style>
