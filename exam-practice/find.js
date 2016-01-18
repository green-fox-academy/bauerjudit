"use strict";


var students = [
    {'name': 'Tibi', 'age': 8},
    {'name': 'Adorjan', 'age': 9},
    {'name': 'Agoston', 'age': 6},
    {'name': 'Aurel', 'age': 7},
    {'name': 'Dezso', 'age': 12}
]


function findStudentUnderAge8(students) {
	var output = "";
	students.forEach(function(e) {
		if (e.age < 8) {
			output += e.name + "\n";
		}
	})
	return output;
}

console.log(findStudentUnderAge8(students));


function findStudentUnderAge8Ver2(students) {
	var output = "";
	for (var i = 0; i < students.length; i++) {
		if (students[i]["age"] < 8) {
			output += students[i]["name"] + "\n";
		}
	}
	return output;
}

console.log(findStudentUnderAge8Ver2(students));



function findStudentNameStartingA(students) {
	var output = "";
	students.forEach(function(e) {
		if (e["name"][0] === "A") {
			output += e["name"] + "\n";
		}
	})
	return output;
}


console.log(findStudentNameStartingA(students));


function makeFactorial(number) {
	var output = 1;
	for (var i = 1; i <= number; i++) {
		output *= number
	}
	return output;
}

console.log(makeFactorial(8));