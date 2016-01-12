"use strict";

var candyCount = 0;
var lollypopCount = 0;
var buyCandyButton = document.querySelector(".BuyCandie");
var buyLollypopButton = document.querySelector(".BuyLollypop");
var candieCounter = document.querySelector(".CandieCounter");
var lollypopCounter = document.querySelector(".LollypopCounter");


buyCandyButton.addEventListener("click", function() {
  candyCount++;
  candieCounter.innerHTML = "You have" + " " + candyCount + " " + "candies!";
});

buyLollypopButton.addEventListener("click", function() {
  if (candyCount >= 10) {
    lollypopCount++;
    candyCount -= 10;
    lollypopCounter.innerHTML = "You have" + " " + lollypopCount + " " + "lollypops!";
    candieCounter.innerHTML = "You have" + " " + candyCount + " " + "candies!";
  } else {
    lollypopCounter.innerHTML = "You have" + " " + lollypopCount + " " + "lollypops!";
  }
});
