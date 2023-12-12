#!/usr/bin/node
function addMeMaybe(number, theFunction) {
  const newNum = number + 1;
  theFunction(newNum);
}

module.exports = { addMeMaybe };