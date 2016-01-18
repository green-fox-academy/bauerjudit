"use strict";

function Student() {
	this.grades = [];
	this.average = 0;
	this.addGrade = function(grade) {
		this.grades.push(grade)
	};
	this.getAverage = function() {
		var output = 0;
		this.grades.forEach(function(e) {
			output += e;
		})
		return output / this.grades.length;
	}
};


var jozsi = new Student();
jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);
console.log(jozsi.getAverage()); // 4.25