#!/usr/bin/node
exports.esrever = function (list) {
  let theLeft = 0;
  let theRight = list.length - 1;
  while (theLeft < theRight) {
    // Swap elements from left to right
    const temp = list[theLeft];
    list[theLeft] = list[theRight];
    list[theRight] = temp;
    // Print front and back to middle
    theLeft++;
    theRight--;
  }
  return list;
};
