'use strict';

var pirates = [
  {name: 'Jack', id: 1},
  {name: 'Bob', id: 2},
  {name: 'Omar', id: 3},
  {name: 'Olaf', id: 4},
  {name: 'Boris', id: 5}
];

var stashes = [
  {pirateId: 3, gold:4},
  {pirateId: 4, gold:1},
  {pirateId: 2, gold:5},
  {pirateId: 5, gold:3},
  {pirateId: 1, gold:8},
];


function getGoldByPirateName(name) {
  var id = 0;
  var gold = 0;
  pirates.forEach(function(e) {
    if (e["name"] === name) {
      id = e["id"];
    }
  })
  stashes.forEach(function(e) {
    if (e["pirateId"] === id) {
      gold = e["gold"];
    }
  })
  return gold;
}


console.log(getGoldByPirateName('Jack'));





function getGoldByPirateName2(name) {
  var id = 0;
  var gold = 0;
  for (var i = 0; i < pirates.length; i++) {
    if (pirates[i]["name"] === name) {
      id = pirates[i]["id"];
    }
  }
  for (var j = 0; j < stashes.length; j++) {
    if (stashes[j]["pirateId"] === id) {
      gold = stashes[j]["gold"];
    }
  }
  return gold;
}



console.log(getGoldByPirateName2("Jack"));
