"use strict";

var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];

function countBySex2(kids) {
  var output = {female: 0, male: 0};
  kids.forEach(function(kid) {
      output[kid.sex]++;
    })
  return output;
}

console.log(countBySex2(kids));

function countBySex(kids) {
	var output = {female: 0, male: 0};
	kids.forEach(function(kid) {
		if("female" === kid.sex) {
			output.female++
		} else {
			output.male++
		}
	});
	return output;
}



console.log(countBySex(kids)); //{female: 2, male: 3}

