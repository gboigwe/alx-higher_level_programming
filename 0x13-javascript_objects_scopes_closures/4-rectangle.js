#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let row = '';
      let j = 0;
      while (j < this.width) {
        row += 'X';
        j++;
      }
      console.log(row);
      i++;
    }
  }

  rotate () {
    const holdWidth = this.width;
    this.width = this.height;
    this.height = holdWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
