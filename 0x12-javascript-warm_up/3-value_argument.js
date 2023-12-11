#!/usr/bin/node
if (process.argv.length === undefined) {
	console.log('No argument');
	return;
}
console.log(process.argv[2]);
