#!/usr/bin/node
const argSize = process.argv;
if (argSize[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argSize[2]);
}
