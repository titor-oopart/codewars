/* 
 The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
*/

function duplicateEncode(str) {
  let i = 0;
  const solution = [];
  while (i < str.length) {
    const char = str[i];
    const pattern = `[${char}].*[${char}]`;
    const regex = new RegExp(pattern, "gi");
    const match = str.search(regex);
    if (match != -1) {
      solution.push(")");
    } else {
      solution.push("(");
    }
    i++;
  }
  return solution.join("");
}

function duplicateEncode(word) {
  return word
    .toLowerCase()
    .split("")
    .map(function (a, i, w) {
      return w.indexOf(a) == w.lastIndexOf(a) ? "(" : ")";
    })
    .join("");
}

module.exports = duplicateEncode;
