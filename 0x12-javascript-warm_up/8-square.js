#!/usr/bin/node

// store the size of the square from the command-line arguments
const size = process.argv[2];

// check if the size can be converted to a number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(size); i++) {
    console.log('X'.repeat(Number(size)));
  }
}
