#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  list.forEach(element => {
    newlist.unshift(element);
  });
  return (newlist);
};
