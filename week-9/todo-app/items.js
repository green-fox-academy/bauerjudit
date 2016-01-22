"use-strict"

var mysql = require('mysql');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test',
  password : 'test',
  database : 'todo'
});

connection.connect();


function addItem(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function getItem(id) {
  connection.query('SELECT id, todo_text, todo_status FROM todo WHERE id = ?', id, function(err, result) {
    if (err) throw err;
  });
}

function getItems(callback) {
  connection.query('SELECT * FROM `todo`', function(err, results) {
    if (err) throw err;
    console.log(results);
    callback(results);
  });
}

function deleteItem(id) {
  connection.query('DELETE FROM todo WHERE id = ?', id, function(err, results) {
    if (err) throw err;
  });
}


var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

module.exports = {
  add: addItem,
  getItems: getItems,
  remove: deleteItem
};

/*function getItem(id) {
  return items[id];
}

function addItem(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}


function removeItem(id) {
  delete items[id];
}

function allItems() {
  var values = [];
  for (id in items) {
    values.push(items[id]);
  }
  return values;
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems
};*/
