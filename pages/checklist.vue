
<template>
  <div>
    <!-- Composant Dropzone qui accepte les fichiers déposés -->
    <Dropzone @files-dropped="handleFilesDropped" />
  </div>
</template>

<script setup>
import { ref } from 'vue'


// Crée une référence réactive pour stocker les fichiers déposés
const files = ref([])

// Fonction asynchrone pour gérer les fichiers déposés
async function handleFilesDropped(droppedFiles) {
  // Affiche les fichiers déposés dans la console
  console.log('Fichiers déposés :', droppedFiles)

  // Convertit les fichiers déposés en un tableau et les stocke dans la référence réactive
  files.value = Array.from(droppedFiles)

  // Crée un objet FormData pour envoyer les fichiers via une requête POST
  const formData = new FormData()
  for (let i = 0; i < files.value.length; i++) {
    formData.append('files', files.value[i])
  }

  try {
    // Envoie une requête POST contenant les fichiers à l'URL spécifiée
    const response = await fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: formData
    })

    // Récupère les données de la réponse
    const data = await response.json()

    // Affiche la réponse du serveur dans la console
    console.log('Réponse du serveur:', data)
  } catch (error) {
    // Affiche une erreur si la requête échoue
    console.error('Erreur lors du téléchargement des fichiers:', error)
  }
}
</script>

