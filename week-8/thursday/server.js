"use strict";

var express = require("express");
var bodyParser = require("body-parser");

var app = express();

var itemList =
  [{item: "buy milk"},
   {item: "buy milk"},
   {item: "buy milk"},
]

// GET todo item
app.get("/", function(req, res) {
  res.json(itemList);
});


// POST todo item
app.post("/", function (req, res) {
  req.body
  res.status(201).json();
})

function addNewItem(newItem) {
  itemList.push(newItem)
}

app.listen(3000);
