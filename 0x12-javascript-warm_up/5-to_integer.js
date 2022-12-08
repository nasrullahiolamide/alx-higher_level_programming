#!/usr/bin/node
const process = require('process');

const parsed = parseInt(process.argv[2], 10);

if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsed}`);
}
