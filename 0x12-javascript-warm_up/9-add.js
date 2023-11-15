#!/usr/bin/node

// store the integers from the command-line arguments
const a = process.argv[2];
const b = process.argv[3];

// define the function
function add (a, b) {
  return Number(a) + Number(b);
}

// Print the result of the addition
console.log(add(a, b));
