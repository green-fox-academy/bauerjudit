"use strict";

var numbers = [7, 8 , 4, -1, 13, 55];


var output = numbers[0];

for (var i = 1; i < numbers.length; i++) {
  if (output > numbers[i]) {
    output = numbers[i]
  }
}

console.log(output);
