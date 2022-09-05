#!/usr/bin/node
let intVal = parseInt(process.argv[2]);
let res = 1;
if (isNaN(intVal)) {
  console.log(1);
} else {
  while (intVal > 0) {
    res *= intVal;
    intVal--;
  }
  console.log(res);
}
