#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

Object.keys(dict).forEach(key => {
  const occurrence = dict[key];
  if (newDict[occurrence] === undefined) {
    newDict[occurrence] = [key];
  } else {
    newDict[occurrence].push(key);
  }
});

console.log(newDict);
