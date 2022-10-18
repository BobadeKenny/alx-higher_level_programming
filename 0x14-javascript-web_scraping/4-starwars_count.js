#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const results = JSON.parse(body).results;
  let num = 0;
  for (let index = 0; index < results.length; index++) {
    results[index].characters.forEach(element => {
      if (element.includes("18"))
      {
        num++
      }
    });
  }
  console.log(num);
});
