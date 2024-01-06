#!/usr/bin/node
const arr = [];

for (let i = 2; i < process.argv.length; i++) {
  arr.push(parseInt(process.argv[i]));
}

let maxNumber = arr[0];
let secondMaxNumber = 0;

for (let i = 1; i < arr.length; i++) {
  if (arr[i] > maxNumber) {
    secondMaxNumber = maxNumber;
    maxNumber = arr[i];
  }

  if (arr[i] > secondMaxNumber && arr[i] < maxNumber) {
    secondMaxNumber = arr[i];
  }
}
console.log(secondMaxNumber);
