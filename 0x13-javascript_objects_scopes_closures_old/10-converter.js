#!/usr/bin/node
exports.converter = function (base) {
  return function inner(num) {
    return num.toString(base);
  };
};
