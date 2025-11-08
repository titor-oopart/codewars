const { assert, config } = require("chai");
const primeFactors = require("../katas/kata03-5kyu-primes-in-number.js");
config.truncateThreshold = 0;

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)");
  });
});
