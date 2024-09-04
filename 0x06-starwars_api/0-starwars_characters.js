#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the film ID from the command line arguments
const filmId = process.argv[2];

// Make a request to the Star Wars API to get the details of the film
request('https://swapi-api.hbtn.io/api/films/' + filmId, function (error, response, body) {
  if (error) throw error;

  // Parse the response body to get the list of character URLs
  const characterUrls = JSON.parse(body).characters;

  // Function to request and print character names in order
  fetchAndPrintCharactersInOrder(characterUrls, 0);
});

/**
 * Fetches and prints the names of characters in the order they appear in the characterUrls array.
 *
 * @param {Array} characterUrls - An array of URLs pointing to character data.
 * @param {number} index - The current index of the characterUrls array being processed.
 */
const fetchAndPrintCharactersInOrder = (characterUrls, index) => {
  if (index === characterUrls.length) return; // Base case: Stop recursion when all characters are processed

  // Request the character data from the URL at the current index
  request(characterUrls[index], function (error, response, body) {
    if (error) throw error;

    // Print the character's name
    console.log(JSON.parse(body).name);

    // Recursively call the function to process the next character
    fetchAndPrintCharactersInOrder(characterUrls, index + 1);
  });
};
