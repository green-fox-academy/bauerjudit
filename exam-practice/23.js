"use strict";

var w = 123;
var credits = 100;
var is_bonus = false;
/*# if credits are at least 50,
# and is_bonus is False decrement w by 2
# if credits are smaller than 50,
# and is_bonus is False decrement w by 1
# if is_bonus is True w should remain the same*/

if (credits >= 50 && is_bonus === false) {
  w -= 2;
} else if (credits < 50  && is_bonus === false) {
  w -= 1;
}

console.log(w);
