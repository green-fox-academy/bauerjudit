"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");

var app = express();



app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());


app.get("/todos", function (req, res) {
  items.getItems(function (allItems) {
    res.status(200).json(allItems);
 });
});


app.post("/todos", function (req, res) {
  var attribute = req.body;
  console.log(attribute);
  items.addItem(attribute, function (item) {
    res.status(201).json(item);
  });
});

app.get("/todos/:id", function (req, res) {
  var id = parseInt(req.params.id);
  console.log(id)
  items.getItem(id, function (item) {
    res.status(200).json(item);
  });
});


app.put("/todos/:id", function (req, res) {
  items.addItem(id, function (item) {
    res.status(200).json(item)
  });
});


app.delete("/todos/:id", function (req, res) {
    items.remove(req.params.id);
    item.destroyed = true;
    res.status(200).send('OK');
});

app.listen(3000, function () {
  console.log("Listening on port 3000...")
});

function findItem(req, res, found) {
  var id = req.params.id;
  var item = items.get(id);
  if (item) {
    found(item);
  } else {
    res.status(404).json({error: "Item not found"})
  }
}

function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(" "));
  next();
}
