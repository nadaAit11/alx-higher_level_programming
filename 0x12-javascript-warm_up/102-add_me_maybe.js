#!/usr/bin/node

// Define the addMeMaybe function
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

exports.addMeMaybe = addMeMaybe;
