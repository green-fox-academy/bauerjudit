"use strict";

var numbers = [3, 4, 5, 6, 7];
//# write a function that reverses a list

function reverseList(list) {
  var reversedList = [];
  for (var i = list.length - 1 ; i > -1; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
}

console.log(reverseList(numbers));
