"use strict";

var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];


function filterNameBySex(kids, string) {
  var output = [];
  kids.forEach(function(kid) {
    if(kid.sex === string)
      output.push(kid.name);
  })
  return output;
}


console.log(filterNameBySex(kids, "female")); //"Julika", "Gerda"