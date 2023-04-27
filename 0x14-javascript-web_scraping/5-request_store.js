#!/usr/bin/node

const r = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
let content;
r(url, (err, reponse, body) => {
  if (err) {
    console.error(err);
  }
  const resultquery = reponse.statusCode === 200 ? body : null;
  if (!resultquery) {
    console.log(resultquery);
  }
  content = resultquery;

  fs.writeFile(file, content, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    }
  });
});
