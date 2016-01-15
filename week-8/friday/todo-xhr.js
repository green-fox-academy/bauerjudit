"use strict";

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';


function startRequest(text) {
  postItemToServer(text, appendP)
}

function appendP(response) {
  var output = document.querySelector(".todo");
  output.innerText = response.text;

}

function postItemToServer(text, callback) {
  var req = new XMLHttpRequest();
  req.open('POST', url);
  req.setRequestHeader('Content-Type', 'application/json');
  req.send(JSON.stringify({text: text}));
  console.log("start");
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      console.log("response ok");
      return callback(res);
    }
  };
}


function listItemsFromServer(callback) {
  var req = new XMLHttpRequest();
  req.open("GET", url);
  req.send();
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var todoItems = JSON.parse(req.response);
      return callback(todoItems);
    }
  }
}

function listTodoItems(todoItems) {
  var todoContainer = document.querySelector(".listTodos");
  todoItems.forEach(function(todoItem) {
    var newTodoItem = document.createElement("p");
    newTodoItem.setAttribute("id", todoItem.id);
    newTodoItem.innerText = todoItem.text;
    newTodoItem.addEventListener("click", function() {
      textArea.innerText = todoItem.id;
    })
    todoContainer.appendChild(newTodoItem);
  })
}

listItemsFromServer(listTodoItems);



function deleteItemFromServer(id, callback) {
  var req = new XMLHttpRequest();
  req.open("DELETE", url + "/" + id);
  req.send();
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var response = JSON.parse(req.response);
      return callback(response.id);
    }
  }
}

function deleteItemfromTodoList(id) {
  var deleteItem = document.getElementById(id);
  deleteItem.remove();
}


var textArea = document.querySelector(".inputTodo");
var addNewTodo = JSON.stringify({text: textArea.value});


var addButton = document.querySelector(".addButton");
addButton.addEventListener("click", function() {
  startRequest(textArea.value);
});

var removeButton = document.querySelector(".removeButton");
removeButton.addEventListener("click", function() {
  deleteItemFromServer(textArea.value, deleteItemfromTodoList)
});
