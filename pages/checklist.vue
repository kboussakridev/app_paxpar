<script setup> 
import { ref } from 'vue'

const files = ref([]) // Variable réactive pour stocker les fichiers déposés

// Fonction appelée lorsque des fichiers sont déposés
function handleFilesDropped(droppedFiles) {
  console.log('Fichiers déposés :', droppedFiles)
  files.value = Array.from(droppedFiles) // Stockage des fichiers déposés dans la variable réactive
}
</script>

<style>
/* Ajoutez d'autres styles ici si nécessaire */
</style>


<template>
    <div >
        <Dropzone @files-dropped="handleFilesDropped" /> <!-- Utilisation du composant Dropzone et écoute de l'événement personnalisé -->
    </div>
</template>
                
            