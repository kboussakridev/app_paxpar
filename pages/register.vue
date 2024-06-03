<template>
  <Header/>
  <div class="page-container">
      <div class="container mx-auto p-6 max-w-md">
          <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
              <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">S'enregistrer</h1>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                      Email
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                      id="email" 
                      type="email" 
                      v-model="email" 
                      placeholder="Email"
                  />
              </div>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                      Mot de passe
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" 
                      id="password" 
                      type="password" 
                      v-model="password" 
                      placeholder="******************"
                  />
              </div>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
                      Nom
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                      id="username" 
                      type="text" 
                      v-model="username" 
                      placeholder="Votre nom"
                  />
              </div>
              <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="address">
                      Address
                  </label>
                  <input 
                      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                      id="address" 
                      type="text" 
                      v-model="address" 
                      placeholder="Address"
                  />
              </div>
              <div class="flex items-center justify-between">
                <nuxt-link to="/page-vide">
                  <button 
                      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" 
                      @click=""
                      type="button"
                  >
                      Valider
                  </button>
                </nuxt-link>
              </div>
              <div v-if="successMsg" class="mt-4">
                  <h1 class="text-green-500 font-bold">{{ successMsg }}</h1>
              </div>
              <div v-if="errorMsg" class="mt-4">
                  <h1 class="text-red-500 font-bold">{{ errorMsg }}</h1>
              </div>
          </div>
      </div>
  </div>
  <Footer/>
</template>


<style scoped>
    .page-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-image: url('~/assets/img/paxpar2_4k.png');
        background-size: 100% 100%;
        background-position: center;
    }
</style>





<!-- <script setup>
import { useSupabaseClient, useSupabaseUser } from '@supabase/supabase-js' // Importation des hooks pour utiliser Supabase
import { useState } from '#app' // Importation du hook useState pour gérer les états locaux

// Initialisation des variables et des états
const supabase = useSupabaseClient() // Initialisation du client Supabase
const user = useSupabaseUser() // Récupération de l'utilisateur actuellement connecté via Supabase
const email = useState(() => null) // État pour stocker l'email
const password = useState(() => null) // État pour stocker le mot de passe
const username = useState(() => null) // État pour stocker le nom d'utilisateur
const address = useState(() => null) // État pour stocker l'adresse
const successMsg = useState(() => false) // État pour afficher un message de succès
const errorMsg = useState(() => false) // État pour afficher un message d'erreur

// Redirection vers la page d'accueil si l'utilisateur est déjà connecté
// if (user.value) await navigateTo('/')

// Fonction pour se connecter avec OAuth via Supabase
const signInWithOAuth = async () => {
    // Tentative de connexion avec les informations fournies
    const {data, error} = await supabase.auth.signInWithOAuth  ({
        email: email.value, // Email de l'utilisateur
        password: password.value, // Mot de passe de l'utilisateur
        options: {
            data: {
                full_name: username.value, // Nom d'utilisateur
                address: address.value // Adresse de l'utilisateur
            },
            emailRedirectTo: 'http://localhost:3000' // URL de redirection après connexion
        }
    })

    // Gestion des erreurs de connexion
    if (error) {
        successMsg.value = null // Réinitialisation du message de succès
        errorMsg.value = error.message // Affichage du message d'erreur
        return
    }

    // Si la connexion est réussie
    errorMsg.value = null // Réinitialisation du message d'erreur
    successMsg.value = 'Redirecting...' // Affichage du message de succès

    // Redirection après un délai de 2 secondes
    setTimeout(async() => {
        successMsg.value = null // Réinitialisation du message de succès
        await navigateTo('/confirm') // Navigation vers la page de confirmation
    }, 2000)
}
</script> -->
