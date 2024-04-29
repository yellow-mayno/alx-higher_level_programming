#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h)) {
      w = undefined;
      h = undefined;
    } else if (w <= 0 || h <= 0) {
      w = undefined;
      h = undefined;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
