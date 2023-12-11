#!/usr/bin/node
if (process.argv[2] === undefined) {
	console.log('No argument');
	return;
}
if (process.argv.length === 3) {
	console.log('Argument found');
	return;
}
console.log('Arguments found');
