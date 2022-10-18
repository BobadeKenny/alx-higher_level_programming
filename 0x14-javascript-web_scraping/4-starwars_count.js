#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const results = JSON.parse(body).results;
  let num = 0;
  for (let index = 0; index < results.length; index++) {
    if (results[index].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      num++;
    }
  }
  console.log(num);
});
