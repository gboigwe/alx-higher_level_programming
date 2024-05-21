#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./4-starwars_count.js API_URL');
  process.exit(1);
}

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.reduce((count, film) => {
      const characters = film.characters.map(url => url.split('/').slice(-2, -1)[0]);
      if (characters.includes(wedgeAntillesId.toString())) {
        return count + 1;
      }
      return count;
    }, 0);

    console.log(moviesWithWedgeAntilles);
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    process.exit(1);
  }
});
