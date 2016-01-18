"use strict";

var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];

function getAgeByName(kids, name) {
	var output = 0;
	kids.forEach(function(e) {
		if(e.name === name) {
			output = e.age;
		}
	});
	return output;
}


console.log(getAgeByName(kids, "Gerda"));


function getAgeByName2(kids, name) {
	for(var i = 0; i < kids.length; i++) {
		if(kids[i]["name"] === name) {
			return kids[i]["age"];
		}
	}
}

console.log(getAgeByName2(kids, "Gerda"));