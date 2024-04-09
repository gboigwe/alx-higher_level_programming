#!/usr/bin/node
const sArg = process.argv.length;
if (sArg <= 3) {
  console.log(0);
} else {
  const theSlice = process.argv.slice(2, sArg)
    .map(Number).sort((a, b) => a - b);
  console.log(theSlice[theSlice.length - 2]);
}
