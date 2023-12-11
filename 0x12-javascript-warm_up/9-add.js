#!/usr/bin/node
let num1 = parseInt(process.argv[2]);
let num2 = parseInt(process.argv[3]);

if (isNaN(num1) || isNaN(num2)) {
    console.log("NaN");
    return;
}

console.log(num1 + num2);
