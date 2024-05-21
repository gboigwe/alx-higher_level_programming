#!/usr/bin/node

const fs = require('fs');

if (process.argv.length <= 2) {
  console.log('Usage: ./0-read_file.js path_to_file');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  console.log(data);
});
