#!/usr/bin/node
const fArg = process.argv[2];
function factorial (a) {
  a = Math.floor(Number(a));

  if (a === 0 || a === 1 || isNaN(a)) {
    return 1;
  } else {
    const res = a * factorial(a - 1);
    return res;
  }
}

console.log(factorial(fArg));
