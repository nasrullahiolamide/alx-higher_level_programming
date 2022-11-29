#!/usr/bin/node
const process = require('process');

const times = parseInt(process.argv[2], 10);

if (Number.isInteger(times) && times > 0) {
  for (let i = 1; i <= times; i++) {
    console.log('X'.repeat(times));
  }
} else {
  console.log('Missing size');
}
