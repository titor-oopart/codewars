function solution(number) {
  if (number < 1) {
    return 0;
  }
  var sum = [];
  for (let i = 0; i < number; i++) {
    if ((i % 3) == 0) {
      sum.push(i);
    } else if ((i % 5) == 0) {
      sum.push(i);
    }
  }
  const total = sum.reduce((accumulator, current) => accumulator + current, 0);
  return total;
}

module.exports = solution;
