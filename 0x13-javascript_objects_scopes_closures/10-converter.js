#!/usr/bin/node
exports.converter = function (base) {
  return function (nBase) {
    return (nBase.toString(base));
  };
};
