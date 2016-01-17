"use strict";

function runIn5econds(callback) {
  setTimeout(callback, 5000);
}


runIn5econds(function() {
  console.log("jeee");
});
