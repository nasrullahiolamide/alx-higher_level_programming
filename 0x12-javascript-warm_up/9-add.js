#!/usr/bin/node
const process = require('process');

const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);

function add (x, y) {
  return (x + y);
}

console.log(add(a, b));
