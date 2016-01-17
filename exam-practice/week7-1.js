'use strict';

// write a function that counts how many
// fives are in an array
var grades = [4, 3, 5, 2, 5, 4, 1, 3, 5];

function countFives(grades) {
  var count = 0;
  grades.forEach(function(e) {
    if (e === 5) {
      count++
    }
  })
  return count;
}

console.log(countFives(grades)); // 3


function countFives2(grades) {
  var count2 = 0;
  for(var i = 0; i < grades.length; i++) {
    if(grades[i] === 5) {
      count2++;
    }
  }
  return count2;
}

console.log(countFives2(grades));
