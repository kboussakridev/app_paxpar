<template>
    
    <Header />
      <main class="flex-grow">
        <div class="text-center">
          <div class="py-24 sm:py-32 md:py-40 relative">
            <div class="text-5xl font-bold tracking-tight text-gray-900 dark:text-white sm:text-7xl">
              Your PDF documents in compliance
            </div>
          </div>
        </div>
          <div class="carousel w-auto h-max">
            <div id="item1" class="carousel-item w-full">
              <img src="~/assets/img/incoming_files.png" class="w-full" />
            </div> 
            <div id="item2" class="carousel-item w-full">
              <img src="~/assets/img/fichier.png" class="w-full" />
            </div> 
            <div id="item3" class="carousel-item w-full">
              <img src="~/assets/img/craft.png" class="w-full" />
            </div> 
            <div id="item4" class="carousel-item w-full">
              <img src="~/assets/img/conformité.png" class="w-full" />
            </div>
            <div id="item4" class="carousel-item w-full">
              <img src="~/assets/img/children.png" class="w-full" />
            </div>
            <div id="item4" class="carousel-item w-full">
              <img src="~/assets/img/check_ok.png" class="w-full" />
            </div>
          </div> 
      <div class="flex justify-center w-full py-2 gap-2">
        <a href="#item1" class="btn btn-xs">1</a> 
        <a href="#item2" class="btn btn-xs">2</a> 
        <a href="#item3" class="btn btn-xs">3</a> 
        <a href="#item4" class="btn btn-xs">4</a>
      </div>
      </main>
    <Footer/>  
  </template>



<script setup>

</script>


  