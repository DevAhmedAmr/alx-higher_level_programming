#!/usr/bin/node
let len = parseInt(process.argv[2]);

if (isNaN(len)) {
  console.log('Missing size');
  return;
}
for (let i = 0; i < len; i++) {
  let buffer = '';

  for (let j = 0; j < len; j++) buffer += 'X';

  console.log(buffer);
}
