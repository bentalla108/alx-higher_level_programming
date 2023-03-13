#!/usr/bin/node
const value = process.argv[2];
if (Number.isInteger(Number.parseInt(value))) {
  console.log(`My number: ${value[2]}`);
} else {
  console.log('Not a number ');
}
