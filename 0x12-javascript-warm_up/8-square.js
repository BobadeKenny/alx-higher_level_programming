#!/usr/bin/node
const intVal = parseInt(process.argv[2]);
let i = 0;
if (isNaN(intVal)) {
  console.log('Missing size');
} else {
  while (i < intVal) {
    console.log('X'.repeat(intVal));
    i++;
  }
}
