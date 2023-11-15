#!/usr/bin/node

// store argument
const arg = process.argv[2];

// try to convert the argument to an integer
const num = parseInt(arg);

// check if the argument is an integer
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
