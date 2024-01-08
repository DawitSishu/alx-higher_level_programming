#!/usr/bin/node

const th = process.argv.length;

if (th < 3) {
  console.log('No argument');
} else if (th === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
