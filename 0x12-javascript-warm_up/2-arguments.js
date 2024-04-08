#!/usr/bin/node
const myVar = process.argv.length;
console.log(myVar === 2 ? 'No argument' : myVar === 3 ? 'Argument found' : 'Arguments found');
// if (myVar === 2) {
// 	console.log('No argument');
// } else if (myVar === 3) {
// 	console.log('Argument found');
// } else {
// 	console.log('Argument found');
// }
