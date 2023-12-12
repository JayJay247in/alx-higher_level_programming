#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print() {
    if (this.width !== undefined && this.height !== undefined) {
      for (let y = 0; y < this.height; y++) {
        let row = '';
        for (let x = 0; x < this.width; x++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }

}

module.exports = Rectangle;