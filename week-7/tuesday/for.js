"use strict";



for (var i = 0; i < 5; i++) {
  console.log(i);
}


var array = ["ez", "meg", "az"];

for (var i = 0; i < array.length; i++) {
  console.log(array[i]);
}


var student = {
  kor: 12,
  name: "Csaba",
  labmeret: 46
};

for (var key in student) {
  console.log(key);
}
