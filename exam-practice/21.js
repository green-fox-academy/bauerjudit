"use strict";

var u = 13
/*# if u is between 10 and 20 print 'Sweet!'
# if less than 10 print 'More!',
# if more than 20 print 'Less!'*/

if (u >= 10 && u <= 20) {
  console.log("sweet");
} else if (u < 10) {
  console.log("More");
} else if (u > 20) {
  console.log("Less");
}
