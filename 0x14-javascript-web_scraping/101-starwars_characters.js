#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const results = JSON.parse(body).characters;
  results.forEach(element => {
    request(element, function (err, response, body) {
      if (err) {
        console.error(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
