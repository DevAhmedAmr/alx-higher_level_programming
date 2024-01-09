#!/usr/bin/node
function main () {
  const num1 = parseInt(process.argv[2]);
  const num2 = parseInt(process.argv[3]);

  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
    return;
  }

  console.log(num1 + num2);
}

main();
