#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const results = JSON.parse(body);
  const todos = {};
  for (let index = 0; index < results.length; index++) {
    if (results[index].completed) {
      if (todos[results[index].userId]) {
        todos[results[index].userId] += 1;
      } else {
        todos[results[index].userId] = 1;
      }
    }
  }
  console.log(todos);
});
