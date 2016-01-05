"use strict";



function addition(numbers) {
  var output = 0;
  for (var i = 0; i < numbers.length; i++) {
    output += numbers[i];
  }
  return output;
}

console.log(addition([2, 3]));
