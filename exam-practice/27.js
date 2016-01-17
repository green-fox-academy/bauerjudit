"use strict";

var aa = [4, 5, 6, 7];
//# print all the elements of aa

aa.forEach(function(e , index, arr) {
  console.log(e, index, arr);
});

for (var j = 0; j < aa.length; j ++) {
  console.log(aa[j]);
}

var i = 0;
while (i < aa.length) {
  console.log(aa[i]);
  i++;
}
