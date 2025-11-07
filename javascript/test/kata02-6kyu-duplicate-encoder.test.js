const { assert } = require("chai");
const duplicateEncode = require("../katas/kata02-6kyu-duplicate-encoder.js");

describe("Duplicate Encoder", () => {
  it("Testing for fixed tests", () => {
    assert.strictEqual(duplicateEncode("din"), "(((");
    assert.strictEqual(duplicateEncode("recede"), "()()()");
    assert.strictEqual(
      duplicateEncode("Success"),
      ")())())",
      "should ignore case",
    );
    assert.strictEqual(duplicateEncode("(( @"), "))((");
  });
});
