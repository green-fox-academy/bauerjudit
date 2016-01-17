"use strict";

/*# Write a function that greets the name passed as argument

# Write a function that returns true if the input is dividable by 5

# Write a function that takes a number and returns a list with the numbers till the input*/



function greet(name) {
  console.log("Hello " + name)
}

greet("Tojás");


function isDividableBy5(number) {
  console.log(number % 5 === 0);
}

isDividableBy5(10);


function makeAlist(number) {
  var output = [];
  for(var i = 0; i <= number; i ++) {
    output.push(i);
  }
  return output;
}

console.log(makeAlist(5));
