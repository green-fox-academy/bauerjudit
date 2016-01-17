"use strict";

var numbers = [7, 5, 8, -1, 2]
/*# Write a function that returns the minimal element
# in a list (your own min function)*/

function findMinimum(list) {
  var output = list[0];
  list.forEach(function(e) {
    if (e < output) {
      output = e;
    }
  })
  return output;
}

console.log(findMinimum(numbers));


function findMinimum2(list) {
  var output3 = list[0];
  for (var i = 0; i < list.length; i++) {
    if (i < output3) {
      output3 = list[i];
    }
  }
  return output3;
}

console.log(findMinimum2(numbers));



function findMaximum(list) {
  var output2 = list[0];
  list.forEach(function(e) {
    if (e > output2) {
      output2 = e;
    }
  })
  return output2;
}

console.log(findMaximum(numbers));
