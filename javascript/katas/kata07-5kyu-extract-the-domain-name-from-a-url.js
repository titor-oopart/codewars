function domainName(url) {
  const text = url.replace(/(http:\/\/www.|https:\/\/www.|https:\/\/|http:\/\/|:\/ \/|www.)/, "");
  return text.split(".")[0]
}

module.exports = domainName;
