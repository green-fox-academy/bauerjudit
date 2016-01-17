"use strict";

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
/*# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10*/

function candyCounter(students) {
  var candycounter = 0;
  students.forEach(function(e) {
    if (e["age"] < 10) {
    candycounter += e["candies"];
    }
  })
  return candycounter;
}

console.log(candyCounter(students));


function candyCounter2(students) {
  var candycounter2 = 0;
  for (var i = 0; i < students.length; i ++) {
    if (students[i]["age"] < 10) {
      candycounter2 += students[i]["candies"];
    }
  }
  return candycounter2;
}


console.log(candyCounter2(students));
