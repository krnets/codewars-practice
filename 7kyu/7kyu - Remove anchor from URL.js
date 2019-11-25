// 7kyu - Remove anchor from URL
// Complete the function/method so that it returns the url with anything after the anchor (#) removed. 

// const removeUrlAnchor = url => url.replace(/#.*/, '')
// const removeUrlAnchor = url => url.split('#')[0]
const removeUrlAnchor = url => url.match(/^[^#]*/)[0]

q = removeUrlAnchor('www.codewars.com#about') // 'www.codewars.com'
q
q = removeUrlAnchor('www.codewars.com#') // 'www.codewars.com'
q
q = removeUrlAnchor('www.codewars.com?page=1') 
q