"use strict";

/*nction Car (color, type, km) {
	this.color = color;
	this.type = type;
	this.km = km;

	this.ride = function(km) {
		this.km += km;
	}
}


var uaz = new Car("grey", "uaz", "300000");
*/

function Car2(color, type, km) {
	this.color = color;
	this.type = type;
	this.km = km;
}

Car2.prototype.ride = function(km) {
	this.km += km;
}

var trabant = new Car2("gold", "Trabant", "400");
trabant.ride(0.02);
console.log(trabant.km)


