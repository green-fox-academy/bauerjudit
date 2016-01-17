"use strict";

var ac = ['kuty', 'macsk', 'cic'];
//# add to all elements an 'a' on the end
var output = [];
ac.forEach(function(e) {
  output.push(e + "a");
})
console.log(output);

var output2 = [];
for (var i = 0; i < ac.length; i++) {
  output2.push(ac[i] + "a");
}

console.log(output2);
