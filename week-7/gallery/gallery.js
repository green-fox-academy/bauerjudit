"use strict";

var currentPicture = 0;

var images = [
  "http://desktopography.net/media/exhibition/2011/flight/large.jpg",
  "http://desktopography.net/media/exhibition/2010/creating_vs_creating/large.jpg",
  "http://desktopography.net/media/exhibition/2010/island_paradise/large.jpg",
  "http://desktopography.net/media/exhibition/2010/spartan/large.jpg"
];

var picture = document.querySelector("img");
var leftClick = document.querySelector(".left");
var rightClick = document.querySelector(".right");


function nextPicture() {
  if (currentPicture === images.length - 1) {
    currentPicture = 0;
  } else {
    currentPicture++;
  }
  changePicture(images[currentPicture]);
}

function previousPicture() {
  if (currentPicture === 0) {
    currentPicture = images.length -1;
  } else {
    currentPicture--;
  }
  changePicture(images[currentPicture]);
}

function changePicture(src) {
  picture.setAttribute("src", src);
}


rightClick.addEventListener("click", function () {
  nextPicture();
})

leftClick.addEventListener("click", function () {
  previousPicture();
})
