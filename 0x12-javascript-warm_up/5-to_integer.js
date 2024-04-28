#!/usr/bin/node
const { argv } = require('node:process');
const args = [];
argv.forEach((value, index) => {
  args.push(value);
});
args.push('NaN');
const converted = Number(args[2]);
/* converted == or === NaN not working, Nan is number, but NaN * 0 is NaN while all numbers don't */
if (converted * 0 === 0) {
  console.log('My number: ' + converted);
} else {
  console.log('Not a number');
}
