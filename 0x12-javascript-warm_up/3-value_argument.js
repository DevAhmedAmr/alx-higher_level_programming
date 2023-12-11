#!/usr/bin/node
if (process.argv[2] === undefined) {
	console.log('No argument');
	return;
}
console.log(process.argv[2]);
