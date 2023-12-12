#!/usr/bin/node
let x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
  return;
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
