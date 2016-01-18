'use strict';

var benaSzavak = [
  'kuty',
  'macsk',
  'alm',
  'kacs'
];


function appendA(list) {
	var output = [];
	list.forEach(function(e) {
		output.push(e + "a");
	})
	return output;
}

function appendA2(list) {
	var output = [];
	for (var i = 0; i < list.length; i++) {
		output.push(list[i] + "a");
	}
	return output;
}


console.log(appendA(benaSzavak));
console.log(appendA2(benaSzavak));