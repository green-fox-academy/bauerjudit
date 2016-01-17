"use strict";

var numbers = [4, 5, 6, 7, 8, 9, 10];
//# write your own sum function

function summa(numbers) {
  var output = 0;
  numbers.forEach(function(e) {
    output += e;
  })
  return output;
}

console.log(summa(numbers));


function summa2(numbers) {
  var output2 = 0;
  for (var i = 0; i < numbers.length; i++) {
    output2 += numbers[i];
  }
  return output2;
}

console.log(summa2(numbers));
