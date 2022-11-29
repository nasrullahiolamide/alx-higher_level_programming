#!/usr/bin/node
const process = require('process');

const times = parseInt(process.argv[2], 10);

if (Number.isInteger(times) && times > 0) {
  for (let i = 1; i <= times; i++) {
    console.log('C is fun');
  }
} else if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
