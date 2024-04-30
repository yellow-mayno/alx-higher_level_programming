#!/usr/bin/node
const Rectangle = require('./3-rectangle');
const Square = require('./5-square');
const r1 = new Rectangle();
const r2 = new Rectangle(2, 3);
const r3 = new Rectangle(2,-3);
const r4 = new Rectangle(3);
const r5 = new Rectangle('f', 'a');
console.log(r1);
r2.print();
const s1 = new Square(10);
console.log(s1);
