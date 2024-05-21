#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./3-starwars_title.js episodeNumber');
  process.exit(1);
}

const episodeNumber = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    process.exit(1);
  }
});
