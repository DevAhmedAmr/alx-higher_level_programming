#!/usr/bin/node
let arr = [];

for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
}

let max_number = arr[0];
let second_maxNumber = 0;

for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max_number) {
        max_number = arr[i];
    }

    if (arr[i] > second_maxNumber && arr[i] < max_number)
        second_maxNumber = arr[i];
}
console.log(second_maxNumber);
