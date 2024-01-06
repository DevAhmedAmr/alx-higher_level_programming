#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
let arg = parseInt(process.argv[2]);

if (isNaN(arg)) arg = 1;

console.log(factorial(arg));
