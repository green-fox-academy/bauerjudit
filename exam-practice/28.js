"use strict";

var ab = [3, 4, 5, 6, 7]
//# please double all the elements of the list

var output = [];
ab.forEach(function(e) {
  output.push(e*2);
})
console.log(output);

var output2 = [];
for (var i = 0; i < ab.length; i++) {
  output2.push(ab[i] * 2);
}
console.log(output2);
