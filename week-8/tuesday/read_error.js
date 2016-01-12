"use strict";

var fs = require("fs");

try (
  var content = fs.readFileSync("korte.txt");
)
catch (e) (
  content = "para volt"
)
console.log(String(content))



var fs = require("fs");


fs.readFile("korte.txt", function (err, content) {
  if (err) {
  console.log("para volt");
  } else {
    console.log(content);
  }
})
