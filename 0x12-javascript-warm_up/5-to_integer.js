#!/usr/bin/node
let arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
    console.log("Not a number");
    return;
}

console.log("My number:", arg);
