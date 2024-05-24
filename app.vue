<template>
  <!-- <ul> -->
    <!-- Composant NuxtPage, peut-être utilisé pour rendre la page courante -->
    <NuxtPage/>
    
    <!-- Boucle à travers les pays pour générer une liste d'éléments li -->
    <!-- <li v-for="country in countries" :key="country.id"> -->
      <!-- Affichage du nom de chaque pays -->
      <!-- {{ country.name }}
    </li>
  </ul> -->
</template>



<!-- <script setup>
// Importation du client Supabase
import { createClient } from '@supabase/supabase-js'

// Création du client Supabase avec l'URL du projet et la clé anonyme
const supabase = createClient('https://<project>.supabase.co', '<your-anon-key>')

// Déclaration d'une variable réactive pour stocker la liste des pays
const countries = ref([])

// Définition d'une fonction asynchrone pour récupérer les pays depuis la table 'countries' dans Supabase
async function getCountries() {
  // Utilisation de Supabase pour sélectionner toutes les entrées de la table 'countries'
  const { data } = await supabase.from('countries').select()
  
  // Mise à jour de la variable réactive avec les données récupérées
  countries.value = data
}

// Appel de la fonction getCountries() lorsque le composant est monté
onMounted(() => {
  getCountries()
})
</script> -->
