#!/usr/bin/node
if (process.argv.length < 3) {
	console.log('No argument');
	return;
}
console.log(process.argv[2]);
