"use strict";

var grades = [
  {num: 3, subject: 'math'},
  {num: 5, subject: 'math'},
  {num: 5, subject: 'arts'},
  {num: 2, subject: 'sport'},
  {num: 5, subject: 'physics'},
  {num: 4, subject: 'physics'},
  {num: 5, subject: 'math'}
];


function countMathFives(grades) {
  var count = 0;
  grades.forEach(function(e) {
    if (e["num"] === 5 && e["subject"] === "math") {
      count++
    }
  })
  return count;
}

console.log(countMathFives(grades)); // 2


function countMathFives2(grades) {
  var count = 0;
  for(var i = 0; i < grades.length; i++) {
    if(grades[i]["num"] === 5 && grades[i]["subject"] === "math") {
      count++
    }
  }
  return count;
}

console.log(countMathFives2(grades));
