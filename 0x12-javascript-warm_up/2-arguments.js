#!/usr/bin/node

// store the number of arguments passed
const args = process.argv.length - 2;

// print a message according to the number of arguments passed
if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
