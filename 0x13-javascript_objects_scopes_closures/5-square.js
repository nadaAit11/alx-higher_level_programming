#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Calling the constructor of the class Rectangle
    super(size, size);
  }
}

module.exports = Square;
