/*
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]);
// returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org
 */
function solution(list) {
  var result = [];
  for (let i = 0; i < list.length; i++) {
    var firstNumber = list[i];
    var secondNumber = list[i + 1];
    var thirdNumber = list[i + 2];
    var firstResult = `${list[i]}`;
    var finalResult = "";
    if (Math.abs(firstNumber - secondNumber) > 1) {
      result.push(firstResult);
    } else if (
      Math.abs(firstNumber - secondNumber) == 1 &&
      Math.abs(secondNumber - thirdNumber) == 1
    ) {
      for (var j = i; j < list.length; j++) {
        var first = list[j];
        var final = list[j + 1];
        if (Math.abs(first - final) == 1) {
          finalResult = `-${final}`;
        } else {
          i = j;
          break;
        }
      }
      result.push(`${firstResult}${finalResult}`);
    } else {
      result.push(`${firstResult}`);
    }
  }
  return result.join(",");
}

module.exports = solution;
