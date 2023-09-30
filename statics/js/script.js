const slider = document.querySelector(".slider");
const prevButton = document.getElementById("prev");
const nextButton = document.getElementById("next");
let slideIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll(".slide");
    if (slideIndex >= slides.length) {
        slideIndex = 0;
    }
    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }
    slider.style.transform = `translateX(-${slideIndex * 100}%)`;
}

prevButton.addEventListener("click", () => {
    slideIndex--;
    showSlides();
});

nextButton.addEventListener("click", () => {
    slideIndex++;
    showSlides();
});

showSlides();

function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}



