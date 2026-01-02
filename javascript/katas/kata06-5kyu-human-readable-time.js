/*
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
 */

function solution(seconds) {
  const segMod = "0" + Math.floor(seconds % 60);
  const min = seconds / 60;
  const minMod = "0" + Math.floor(min % 60);
  const hour = "0" + Math.floor(min / 60);
  return `${hour.slice(-2)}:${minMod.slice(-2)}:${segMod.slice(-2)}`;
}

module.exports = solution;
