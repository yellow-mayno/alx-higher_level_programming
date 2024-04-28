#!/usr/bin/node
let i = 0;
const { argv } = require('node:process');
argv.forEach((value, index) => {
  i++;
  if (i === 3) {
    console.log(`${value}`);
  }
});
if (i < 3) {
  console.log('No argument');
}
