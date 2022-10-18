#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (e, data) {
  if (e) {
    console.error(e);
    return;
  }
  console.log(data);
});
