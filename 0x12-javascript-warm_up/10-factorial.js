#!/usr/bin/node

function fact(num) {
  if (num > 0) {
    return num * fact(num - 1);
  }
  return 1;
}

console.log(fact(Number(process.argv[2])));
