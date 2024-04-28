#!/usr/bin/node
const { argv } = require('node:process');
console.log(argv);
console.log(argv[1]);
const args = [];
argv.forEach((value, index) => {
  args.push(value);
});
args.push('');
const type = typeof args[2];
if (type === 'number') {
  console.log(`My number: ${args[2]}`);
} else {
  console.log('Not a number');
}
