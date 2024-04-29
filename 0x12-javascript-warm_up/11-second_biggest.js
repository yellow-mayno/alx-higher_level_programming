#!/usr/bin/nore
const { argv } = require('node:process');
const list = [];
argv.forEach((value, index) => {
  list.push(Number(value));
});
list.sort().reverse();
if (list[3] === undefined) {
  console.log(0);
  process.exit();
}
console.log(list[3]);

