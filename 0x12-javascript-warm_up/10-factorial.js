#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 0;
  } else if (n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const { argv } = require('node:process');
console.log(factorial(argv[2]));
