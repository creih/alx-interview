#!/usr/bin/node

const req = require('request'); // importing request module
const movId = process.argv[2]; // get 2nd arg as movie id from the command line
const url = `https://swapi-api.alx-tools.com/api/films/${movId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach(char => {
        request(char, (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }
            const character = JSON.parse(body);
            console.log(character.name);
        });
    });
});