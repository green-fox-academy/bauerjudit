"use strict"

function reverseString(string) {
	var output = "";
	for (var i = string.length -1; i > -1; i--) {
		output += string[i];
	}
	return output;
}


console.log(reverseString('kacsa'));