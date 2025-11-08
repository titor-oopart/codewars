/*
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
*/

function primeFactors(n) {
  var result = [];
  let i = 2;
  var temp = 0;
  while (i <= n) {
    if (n % i == 0) {
      n = n / i;
      temp++;
      var aux = temp == 1 ? `(${i})` : `(${i}**${temp})`;
      result[i] = aux;
    } else {
      i++;
      temp = 0;
    }
  }
  return result.join("");
}

module.exports = primeFactors;
