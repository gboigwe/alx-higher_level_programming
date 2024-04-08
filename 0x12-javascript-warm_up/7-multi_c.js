#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
// let myWord = 'C is fun';
// let i = 0;
if (!isNaN(myVar) && Number.isInteger(myVar)) {
  const myWord = 'C is fun';
  let i = 0;
  while (i < myVar) {
    console.log(myWord);
    i++;
  }
} else {
  console.log('Missing number of occurences');
}
