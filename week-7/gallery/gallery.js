"use strict";

var title = document.querySelector(".title");
title.classList.add("title");

var currentPicture = 0;

var images = [
  "http://desktopography.net/media/exhibition/2010/rush_cocktail/large.jpg",
  "http://desktopography.net/media/exhibition/2010/creating_vs_creating/large.jpg",
  "http://desktopography.net/media/exhibition/2010/island_paradise/large.jpg",
  "http://desktopography.net/media/exhibition/2010/spartan/large.jpg"
];

var leftClick = document.querySelector(".left");
var rightClick = document.querySelector(".right");


var picture = document.querySelector("img");
var buttonRight = document.querySelector(".changeright");
var buttonLeft = document.querySelector(".changeleft");




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

function changePicture(src) {
  picture.setAttribute("src", src);
}


/*buttonRight.addEventListener("click", function () {
  nextPicture();
})

buttonLeft.addEventListener("click", function () {
  previousPicture();
})*/

rightClick.addEventListener("click", function () {
  nextPicture();
})

leftClick.addEventListener("click", function () {
  previousPicture();
})
