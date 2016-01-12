"use strict";

var candyCount = 100;
var lollypopCount = 0;
var buyCandyButton = document.querySelector(".BuyCandie");
var buyLollypopButton = document.querySelector(".BuyLollypop");
var candieCounter = document.querySelector(".CandieCounter");
var lollypopCounter = document.querySelector(".LollypopCounter");
var candySpeed = 0;

function buyCandies () {
  candyCount++;
  updateCandy();
}

function buyLollypop () {
  if (candyCount >= 10) {
    lollypopCount++;
    candyCount -= 10;
    updateLollypop();
    updateCandy();
    candySpeed = Math.floor(lollypopCount / 10);
  } else {
    updateLollypop;
  }
}

function updateCandy () {
  candieCounter.innerHTML = "You have " + candyCount + " candies!";
}

function updateLollypop () {
  lollypopCounter.innerHTML = "You have " + lollypopCount + " lollypops!";
}

buyCandyButton.addEventListener("click", buyCandies);
buyLollypopButton.addEventListener("click", buyLollypop);


var interval = setInterval(function () {
  if (lollypopCount >= 10 && lollypopCount !== 0) {
  candyCount += candySpeed;
  updateCandy();
  }
}, 1000);
