#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrencesNum = 0;
  for (const i of list) {
    if (i === searchElement) occurrencesNum++;
  }
  return occurrencesNum;
};
