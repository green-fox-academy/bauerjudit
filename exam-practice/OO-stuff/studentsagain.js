"use strict";

/*# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades*/



function Students() {
	this.grades = [];
	this.average = 0;
	this.addGrade = function(grade) {
		this.grades.push(grade)
	}
	this.getAverage = function() {
		var sum = 0;
		this.grades.forEach(function(grade) {
			sum += grade;
		})
		return sum / this.grades.length;
	}
};


var Béla = new Students();
Béla.addGrade(4);
Béla.addGrade(5);
Béla.addGrade(1);
console.log(Béla.getAverage());