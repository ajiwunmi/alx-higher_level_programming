#!/usr/bin/node
const argList = process.argv;
if (argList[2]=== undefined || isNaN(argList[2])) {
  console.log('Not a number');
} else {
   console.log('My number:'+ parseInt(argList[2])); 
}