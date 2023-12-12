#!/usr/bin/node
let printNum = 0;
exports.logMe = function (item) {
  console.log(printNum++, ': ', item);
};
