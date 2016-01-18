"use strict";

function szorzotabla(number) {
	var output = "";
	for(var i = 1; i <= number; i++) {
		output += i + " * " + number + " = " + number * i + "\n";
	}
	return output;
}


console.log(szorzotabla(7));



function fullSzorzotabla() {
	var output = "";
	for(var i = 1; i <= 10; i++) {
		for(var j = 1; j <= 10; j++) {
			output += i + " * " + j + " = " + i * j + "\n";
		}
	}
	return output;
}
 
console.log(fullSzorzotabla());


