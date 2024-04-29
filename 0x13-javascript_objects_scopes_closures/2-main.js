#!/usr/bin/node
const Rectangle = require('./2-rectangle');
const r1 = new Rectangle();
const r2 = new Rectangle(2, 3);
const r3 = new Rectangle(2,-3);
const r4 = new Rectangle(3);
const r5 = new Rectangle('f', 'a');
console.log(r1);
console.log(r1.constructor);
console.log(r2);
console.log(r3);
console.log(r4);
console.log(r5);
