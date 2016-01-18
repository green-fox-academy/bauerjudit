/*# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise*/




function Pirates() {
	this.drunkness = 0;
	this.drinkRum = function() {
		this.drunkness += 1;
	}
	this.howsGoinMate = function(number) {
		if (this.drunkness >= 5) {
			console.log("Arrggh")
		} else {
			console.log("Neee")
		}
	}
};


var pirate = new Pirates();
pirate.drinkRum();
pirate.howsGoinMate();