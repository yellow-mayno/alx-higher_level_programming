#!/usr/bin/node
const args = [];
const { argv } = require('node:process');
argv.forEach((ind, val) => {
  args.push(ind);
});
args.push('undefined');
args.push('undefined');
console.log(args[2] + ' is ' + args[3]);
