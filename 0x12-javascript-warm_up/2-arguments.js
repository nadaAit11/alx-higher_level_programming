#!/usr/bin/node

// store the number of arguments passsed
const argv = process.argv.length - 2;

// print a message according to the number of arguments
if (argv === 0)
	console.log('No argument');
else if (argv === 1)
	console.log('Argument found');
else
	console.log('Arguments found');
