#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let i = 0; i < list.length; i++) {
    const j = list.length - 1 - i;
    arr.push(list[j]);
  }
  return arr;
};
