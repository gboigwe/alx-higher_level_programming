#!/usr/bin/node
exports.add = function (a, b) {
  a = Math.floor(Number(a));
  b = Math.floor(Number(b));
  const result = a + b;
  return result;
};
