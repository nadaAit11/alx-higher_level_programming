#!/usr/bin/node
/* prints all characters of a Star Wars movie.
    - the first argument is the Movie ID.
    - displays one character name by line.
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    printCharacters(film.characters, 0);
  }
});

function printCharacters (characters, i) {
  if (i >= characters.length) {
    return;
  }

  request(characters[i], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, i + 1);
    }
  });
}
