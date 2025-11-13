function countBits(n) {
  var result = 0;
  while (n > 0) {
    const binary = n % 2;
    result += binary;
    n = Math.trunc(n / 2);
  }
  return result;
}

module.exports = countBits;
