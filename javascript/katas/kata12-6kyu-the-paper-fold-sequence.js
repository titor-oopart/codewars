function* paperFold() {
  for (let n = 1; ; n++) {
    let x = n & -n;
    yield ((n & (x << 1)) === 0) ? 1 : 0;
  }
}

module.exports = paperFold;
