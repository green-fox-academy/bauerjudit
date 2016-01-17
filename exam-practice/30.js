"use strict";

var ad = [3, 4, 5, 6, 7];
//# print the sum of all numbers in ad

var output = 0;
ad.forEach(function(e) {
  output += e;
})

console.log(output);

var output2 = 0;
for (var i = 0; i < ad.length; i++) {
  output2 += ad[i];
}

console.log(output2);
