#!/usr/bin/node
const intVal = parseInt(process.argv[2]);
if (isNaN(intVal)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + intVal);
}
