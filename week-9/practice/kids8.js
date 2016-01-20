"use strict";
var array = ["apple", "pear", "pineapple", "carrot", "salad"];

function deleteCarrot(array) {
  var newArray = [];
  for (var i = 0; i < array.length; i++) {
    if (array[i] !== "carrot") {
      newArray.push(array[i]);
    }
  }
  array = newArray;
  return array;
}
console.log(array)


function delete2(array) {
  array.splice(array.indexOf("carrot", 1));
  return array;
}
console.log(delete2(array))