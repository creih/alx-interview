#!/usr/bin/node

// this dile is meant to display names of characters in specified movie id
const req = require('request'); // importing request module
const movId = process.argv[2]; // get 2nd arg as movie id from the command line
const url = `https://swapi-api.alx-tools.com/api/films/${movId}/`;

req(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  // Function to fetch and print character name
  const fetchCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      req(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
          resolve();
        }
      });
    });
  };

  // Process all characters sequentially
  characters.reduce((promise, characterUrl) => {
    return promise.then(() => fetchCharacterName(characterUrl));
  }, Promise.resolve());
});
