"use strict"

function text_multiply(text, number) {
  var output = "";
  for(var i = 0; i < number; i++) {
    output += text;
  }
  return output
}

console.log(text_multiply("alma", 3))
