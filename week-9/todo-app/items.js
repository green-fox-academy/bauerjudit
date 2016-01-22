"use-strict"

var mysql = require('mysql');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test',
  password : 'test',
  database : 'todo'
});

connection.connect();


function addItem(attribute, callback) {
  connection.query('INSERT INTO todo SET ?', attribute, function(err, result) {
    if (err) throw err;
    getItem(result.insertId, callback);
  });
}

function getItem(id, callback) {
  connection.query('SELECT * FROM todo WHERE id = ?', id, function(err, result) {
    if (err) throw err;
    callback(result[0]);
  });
}

function getItems(callback) {
  connection.query('SELECT * FROM `todo`', function(err, results) {
    if (err) throw err;
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
  addItem: addItem,
  getItem: getItem,
  getItems: getItems,
  remove: deleteItem
};

