#!/usr/bin/node
const arr = process.argv.slice(2);
let nums = [];
if (arr.length < 2) {
  console.log(0);
} else {
  nums = arr.map(Number);
  nums.sort(function (a, b) {
    return (a - b);
  }).reverse();
  console.log(nums[1]);
}
