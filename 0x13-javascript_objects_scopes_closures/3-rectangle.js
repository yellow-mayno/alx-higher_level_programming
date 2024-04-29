#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h)) {
      return;
    } else if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
