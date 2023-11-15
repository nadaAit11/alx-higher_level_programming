#!/usr/bin/node

// Get the arguments and convert them to numbers
const args = process.argv.slice(2).map(Number);

// Check the number of arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the numbers in descending order
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
