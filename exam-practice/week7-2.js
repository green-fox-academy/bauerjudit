"use strict";

function range(number) {
  var output = [];
  for(var i = 0; i < number; i++) {
    output.push(i)
  }
  return output;
}

var array = range(5);
console.log(array); // [0,1,2,3,4]



function range2(begin, end) {
  var output = [];
  for (var i = begin; i < end; i++) {
    output.push(i);
  }
  return output;
}

var array2 = range2(3, 7);
console.log(array2); // [3, 4, 5, 6]


function range3(begin, end, step) {
  var output = [];
  for(var i = begin; i < end; i += step) {
    output.push(i);
  }
  return output;
}

var array3 = range3(4, 8, 2);
console.log(array3); // [4, 6]


function range4(from, to, step) {
  var output = [];
  if (step > 0) {
    for (var i = from; i < to; i += step) {
      output.push(i);
    }
  } else {
    for (var i = from; i > to; i -= step) {
      output.push(i);
    }
  }
  return output;
}


var array4 = range4(8, 4, -1);
console.log(array4); // [4, 6]
