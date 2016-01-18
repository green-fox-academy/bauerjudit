"use strict";

var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];


function getTheLongestNamesAge(kids) {
	var longest = kids[0];
	kids.forEach(function(kid) {
		if(longest["name"].length < kid["name"].length) {
			longest = kid
		}
	});
	return longest.age
}


console.log(getTheLongestNamesAge(kids)); //8