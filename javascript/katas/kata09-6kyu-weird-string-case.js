function toWeirdCase(string) {
  const result = string.toLowerCase()
  const words = result.split(" ");
  for (let j = 0; j < words.length; j++) {
    const word = words[j].split("")
    for (let i = 0; i < word.length; i++) {
      if (i % 2 == 0) {
        word[i] = word[i].toUpperCase();
      }
    }
    words[j] = word.join("")
  }
  return words.join(" ")
}


module.exports = toWeirdCase;
