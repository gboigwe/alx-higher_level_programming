#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {

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
