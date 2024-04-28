#!/usr/bin/node
const { argv } = require('node:process');
const arg = Number(argv[2]);
let i = NaN;
if (isNaN(arg)) {
  console.log('Missing size');
  process.exit();
}
for (i = 0; i < arg; i++) {
  console.log('X'.repeat(arg));
}
