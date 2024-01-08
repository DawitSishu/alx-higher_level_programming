#!/usr/bin/node

exports.callMeMoby = function (x, theFun) {
  for (let i = 0; i < x; i++) {
    theFun();
  }
};
