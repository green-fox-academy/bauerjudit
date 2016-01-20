"use strict";

function createCar(color, type, km) {
	function ride(distance) {
		km += distance;
	}
	function getKm() {
		return km;
	}
	return {
		ride: ride,
		getKm: getKm
	};

}



var opel = createCar("white", "opel", "2000");
console.log(opel.ride(200));