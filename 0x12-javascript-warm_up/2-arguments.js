#!/usr/bin/node

// prints a message depending of the number of arguments passed

const argv = process.argv.length - 2;

if (argv === 0)
	console.log("No argument");
else if (argv === 1)
	console.log("Argument found");
else
	console.log("Arguments found");
