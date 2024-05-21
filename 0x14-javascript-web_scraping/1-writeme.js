#!/usr/bin/node

const fs = require('fs');

if (process.argv.length <= 3) {
  console.log('Usage: ./1-write_file.js path_to_file string_to_write');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
