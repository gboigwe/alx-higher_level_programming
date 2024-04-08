#!/usr/bin/node
const myVar = process.argv[2];
if (!isNaN(myVar)) {
  const conve = Math.floor(myVar);
  console.log(`My number: ${conve}`);
} else {
  console.log('Not a number');
}
