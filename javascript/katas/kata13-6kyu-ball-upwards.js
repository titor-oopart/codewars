function maxBall(v0) {
  const v0ms = (v0 * 1000) / 3600; // 3600seg = 1 hr, 1000m = 1km
  let h0 = 0;
  let h = 0;
  let t = 0;
  for (let i = 0; i != -1; i++) {
    h0 = v0ms * t - 0.5 * 9.81 * t * t;
    if (h0 < h) {
      return i - 1;
    } else {
      h = h0;
    }
    t = t + 0.1;
  }
}

module.exports = maxBall;
