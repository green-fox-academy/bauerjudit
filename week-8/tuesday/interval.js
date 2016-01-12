"use strict";

var count = 0;

var interval = setInterval(function () {
  count++;
  console.log("Je-Je-Je", count);
}, 500);



setTimeout(function () {
  console.log("Booooo");
  clearInterval(interval);
}, 5000);



setTimeout(function() {
  for (var i = 0; i < 64375437047; i++)
}, 100);
