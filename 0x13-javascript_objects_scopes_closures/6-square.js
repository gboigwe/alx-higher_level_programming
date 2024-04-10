#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  print (c = 'X') {
    let i = 0;
    while (i < this.height) {
      let row = '';
      let j = 0;
      while (j < this.width) {
        row += c;
        j++;
      }
      console.log(row);
      i++;
    }
  }

  charPrint (c) {
    if (c) {
      this.print(c);
    } else {
      this.print();
    }
  }
};
