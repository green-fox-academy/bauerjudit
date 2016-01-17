"use strict";

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
/*# create a function that returns the shortest string
# from a list*/

function returnShortestString(list) {
  var output = list[0];
  list.forEach(function(e) {
    if (e.length < output.length) {
      output = e;
    }
  })
  return output;
}

console.log(returnShortestString(names));


function returnShortestString2(list) {
  var output2 = list[0];
  for (var i = 0; i < list.length; i ++) {
    if (list[i].length < output2.length) {
      output2 = list[i];
    }
  }
  return output2;
}

console.log(returnShortestString2(names));
