'use strict';

// write a function that counts how many
// fives are in an array
var grades = [4, 3, 5, 2, 5, 4, 1, 3, 5];


function count5(grades) {
	var count = 0;
	grades.forEach(function(e) {
		if (e === 5) {
			count++
		}
	})
	return count;
}

console.log(count5(grades));


function countFiveVar2(grades) {
	var count = 0;
	for (var i = 0; i < grades.length; i++) {
		if (grades[i] === 5) {
			count++;
		}
	}
	return count;
}

console.log(countFiveVar2(grades));


function textMultiply(string, number) {
	var output = "";
	for(var i = 0; i <= number; i++) {
		output += string + " ";
	}
	return output;
}

console.log(textMultiply('alma', 3)); // almaalmaalma




function sumNumbers(numbers) {
	var output = 0;
	numbers.forEach(function(num) {
		output += num
	})
	return output;
}

function sumNumbers2(numbers) {
	var output = 0;
	for (var i = 0; i < numbers.length; i++) {
		output += numbers[i];
	}
	return output;
}


console.log(sumNumbers([4, 5, 6]));
console.log(sumNumbers2([4, 5, 6]));


