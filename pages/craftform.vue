<template>
  <Header/>
  <div class="container">
    <div class="steps ">
      <span class="circle active">1</span>
      <span class="circle">2</span>
      <span class="circle">3</span>
      <span class="circle">4</span>
      <div class="progress-bar">
        <span class="indicator"></span>
      </div>
    </div>
    <div class="buttons">
      <button id="prev" disabled>Prev</button>
      <button id="next">Next</button>
    </div>
  </div>
  <Footer/>
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const circles = document.querySelectorAll(".circle");
  const progressBar = document.querySelector(".indicator");
  const prevButton = document.getElementById("prev");
  const nextButton = document.getElementById("next");

  let currentStep = 1;

  const updateSteps = (e) => {
    if (e.target.id === "next" && currentStep < circles.length) {
      currentStep++;
    } else if (e.target.id === "prev" && currentStep > 1) {
      currentStep--;
    }

    circles.forEach((circle, index) => {
      circle.classList.toggle("active", index < currentStep);
    });

    progressBar.style.width = `${((currentStep - 1) / (circles.length - 1)) * 100}%`;

    prevButton.disabled = currentStep === 1;
    nextButton.disabled = currentStep === circles.length;
  };

  prevButton.addEventListener("click", updateSteps);
  nextButton.addEventListener("click", updateSteps);
});
</script>

<style scoped>
/* Import Google font - Poppins */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");

body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  height: 0;
  font-family: 'Poppins', sans-serif;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 40px;
  max-width: 400px;
  width: 100%;
  height: 100%;
}

.container .steps {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-between;
  position: relative;
}

.steps .circle {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  width: 50px;
  color: #999;
  font-size: 22px;
  font-weight: 500;
  border-radius: 50%;
  background: #fff;
  border: 4px solid #e0e0e0;
  transition: all 200ms ease;
  transition-delay: 0s;
}

.steps .circle.active {
  transition-delay: 100ms;
  border-color: #57cbcc;
  color: #57cbcc;
}

.steps .progress-bar {
  position: absolute;
  height: 4px;
  width: 100%;
  background: #e0e0e0;
  z-index: -1;
}

.progress-bar .indicator {
  position: absolute;
  height: 100%;
  width: 0%;
  background: #57cbcc;
  transition: all 300ms ease;
}

.container .buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  width: 100%;
}

.buttons button {
  padding: 8px 25px;
  background: #57cbcc;
  border: none;
  border-radius: 8px;
  color: #fff;
  font-size: 16px;
  font-weight: 400;
  cursor: pointer;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.05);
  transition: all 200ms linear;
}

.buttons button:active {
  transform: scale(0.97);
}

.buttons button:disabled {
  background: #57cbcc;
  cursor: not-allowed;
}
</style>
