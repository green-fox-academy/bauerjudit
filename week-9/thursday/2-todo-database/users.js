var mysql      = require('mysql');

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

function getItems(attributes) {
  connection.query('SELECT * FROM `todo`', function(err, results) {
    if (err) throw err;
    console.log(results);
  });
}

/*function deleteItems(attributes) {
  connection.query('DELETE FROM `todo`', function(err, results) {
    if (err) throw err;
    console.log(results);
  });
}*/

module.exports = {
  add: addItem,
  get: getItems/*,
  delete_: deleteItems*/
};
