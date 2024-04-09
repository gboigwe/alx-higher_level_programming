#!/usr/bin/node
const fArg = process.argv[2];
const sArg = process.argv[3];

function add (a, b) {
  a = Math.floor(Number(fArg));
  b = Math.floor(Number(sArg));
  const result = a + b;
  console.log(result);
}

add();
