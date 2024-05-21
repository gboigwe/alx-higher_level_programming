#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length <= 3) {
  console.log('Usage: ./5-request_store.js URL FILE_PATH');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
    });
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    process.exit(1);
  }
});
