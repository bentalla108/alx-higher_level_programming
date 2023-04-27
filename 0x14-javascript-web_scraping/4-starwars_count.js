#!/usr/bin/node

const r = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id18 = 'https://swapi-api.alx-tools.com/api/people/18/';

r(url, (err, reponse, body) => {
  if (err) {
    console.error(err);
  }
  const resultquery = reponse.statusCode === 200 ? JSON.parse(body).results : null;
  const count = resultquery ? resultquery.filter(element => element.characters.includes(id18)).length : 0;
  console.log(resultquery ? count : 'error code: ' + reponse.statusCode);
});
