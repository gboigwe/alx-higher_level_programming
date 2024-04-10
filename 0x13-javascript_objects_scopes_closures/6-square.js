#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
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
  }
};
