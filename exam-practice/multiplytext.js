"use strict";


var text = "apple";

function multiplyText(text, number) {
  var output = "";
  for (var i = 0; i <= number; i++) {
    output += text;
  }
  return output;
}

console.log(multiplyText(text, 3));
