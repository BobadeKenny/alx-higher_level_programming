#!/usr/bin/node
let intVal = parseInt(process.argv[2]);
if (isNaN(intVal)) {
  console.log('Missing number of occurrences');
} else {
  while (intVal > 0) {
    console.log('C is fun');
    intVal--;
  }
}
