var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];


function countBySex(kids) {
  var array = {female: [], male: []};
  kids.forEach(function(e) {
    if (e.sex === "male" ) {
      array.male.push(e);
    } else {
      array.female.push(e);
    }
  })
  return array;
}
console.log(countBySex(kids));

