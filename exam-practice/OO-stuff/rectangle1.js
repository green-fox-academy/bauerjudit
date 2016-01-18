"use strict";

/*# Create a Rectangle class
# It should take a, b as the length of the sides as arguments on the constructor
# It should have a get_perimeter method that returns the perimeter of the Rectangle
# It should have a get_aera method that returns the aera of thi Rectangle*/


function Rectangle() {
	this.a = 0;
	this.b = 0;
	this.getPerimeter = function(a, b) {
		return ((a + b) * 2)
	}
	this.getArea = function(a, b) {
		return a * b
	}
};

var myRectangle = new Rectangle();
console.log(myRectangle.getPerimeter(2, 3));
console.log(myRectangle.getArea(2, 3));