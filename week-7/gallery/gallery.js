"use strict";

var title = document.querySelector(".title");


title.classList.add("title");


var images = [
  "http://desktopography.net/media/exhibition/2010/rush_cocktail/large.jpg",
  "http://desktopography.net/media/exhibition/2010/creating_vs_creating/large.jpg",
  "http://desktopography.net/media/exhibition/2010/island_paradise/large.jpg",
  "http://desktopography.net/media/exhibition/2010/spartan/large.jpg"
];

function changePicture(src) {
  var nextpicture = document.querySelector("img");
  nextpicture.setAttribute("src", src);
}

var currentPicture = 0;

function nextPicture() {
  if (currentPicture === images.length - 1) {
    currentPicture = 0;
    changePicture(images[currentPicture]);
  } else {
    currentPicture++;
    changePicture(images[currentPicture]);
  }
}

function previousPicture() {
  if (currentPicture === 0) {
    currentPicture = images.length;
    changePicture(images[currentPicture]);
  }
  currentPicture--;
  changePicture(images[currentPicture]);
}


var buttonRight = document.querySelector(".changeright");
buttonRight.addEventListener("click", function () {
  nextPicture();
})

var buttonLeft = document.querySelector(".changeleft");
buttonLeft.addEventListener("click", function () {
  previousPicture();
})
