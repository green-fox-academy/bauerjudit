"use strict";

//# create a function that returns it's input factorial

function factorial(number) {
  var output = 1;
  for (var i = 1; i <= number; i++) {
    output *= i;
  }
  return output;
}

console.log(factorial(3));
