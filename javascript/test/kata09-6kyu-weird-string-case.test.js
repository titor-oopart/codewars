
const { assert } = require("chai");
const toWeirdCase = require("../katas/kata09-6kyu-weird-string-case.js");

describe('Tests', function () {


  function doTest(input, expected) {
    const actual = toWeirdCase(input);
    const message = `for ${JSON.stringify(input)}\n`;
    assert.strictEqual(actual, expected, message);
  }

  it('Sample Tests', function () {
    doTest('This is a test', 'ThIs Is A TeSt');
    doTest('', '');
    doTest('unique', 'UnIqUe');
    doTest('UPPER CASE', 'UpPeR CaSe');
    doTest('lower case', 'LoWeR CaSe');
  });
});
