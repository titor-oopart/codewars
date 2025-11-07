/*
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
*/

function solution(str) {
  let arr = [];
  if (str.length % 2 != 0) {
    str = str + "_";
  }
  for (let i = 0; i < str.length; i++) {
    if ((i + 1) % 2 == 0) {
      arr[arr.length - 1] = `${arr[arr.length - 1]}${str[i]}`;
    } else {
      arr.push(str[i]);
    }
  }
  return arr;
}

function solution(str) {
  arr = [];
  for (var i = 0; i < str.length; i += 2) {
    second = str[i + 1] || "_";
    arr.push(str[i] + second);
  }
  return arr;
}

module.exports = solution;
