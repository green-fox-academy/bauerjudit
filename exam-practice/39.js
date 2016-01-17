"use strict";

var numbers = [3, 4, 5, 6, 7]
/*# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens*/

function filterOddNumbers(list) {
  var output = [];
  list.forEach(function(e) {
    if (e % 2 === 0) {
      output.push(e);
    }
  })
  return output;
}

console.log(filterOddNumbers(numbers));


function filtersOddNumbers2(list) {
  var output2 = [];
  for ( var i = 0; i < list.length; i++) {
    if (list[i] % 2 === 0) {
      output2.push(list[i]);
    }
  }
  return output2;
}

console.log(filtersOddNumbers2(numbers));
