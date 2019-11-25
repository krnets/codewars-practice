// 5kyu - Extract the domain name from a URL

// Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

// const domainName = url => (parsed = url.match(/(https?:\/\/)?([w]{0,3}\.)?([^\.]+)/))[parsed.length - 1]
// const domainName = url => url.match(/(?:http(?:s)?:\/\/)?(?:w{3}\.)?([^\.]+)/i)[1]
// const domainName = url => url.replace(/(https?:\/\/)?(www\.)?/, '').split('.')[0]
const domainName = url => url.replace(/.+\/\/|www.|\..+/g, '')

q = domainName("http://google.com") // "google"
q
q = domainName("http://google.co.jp") // "google"
q
q = domainName("www.xakep.ru") // "xakep"
q
q = domainName("https://youtube.com") // "youtube"
q