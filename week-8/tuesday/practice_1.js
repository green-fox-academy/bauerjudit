"use strict";

var students = [
  "Zsolt",
  "Évi",
  "Judit",
  "Matyi",
  "Flóri"
];

function getRandomArray(list) {
  var index = Math.random() * list.length;
  return list[index]
}


console.log(getRandomArray(students));
