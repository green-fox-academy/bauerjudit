'use strict';


var kids = [
  {name: 'Tibbor', candies: 2},
  {name: 'Steve', candies: 3},
  {name: 'Agoston', candies: 0},
  {name: 'Julika', candies: 7},
  {name: 'Krisztian', candies: 4}
];


function richestKid(kids) {
	var richestkid = kids[0];
	for (var i = 0; i < kids.length; i++) {
		var currentkid = kids[i];
		if (richestkid.candies < currentkid.candies) {
			richestkid = currentkid
		}
	}
	return richestkid.name
}

console.log(richestKid(kids));



function getRichestKidsName2(kids) {
  var richestKid = kids[0];
  kids.forEach(function(currentKid) {
    if (currentKid.candies > richestKid.candies) {
      richestKid = currentKid;
    }
  });
  return richestKid.name;
}




console.log(getRichestKidsName2(kids)); // Julika