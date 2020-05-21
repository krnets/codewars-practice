// 7kyu - Training JS 40 - Regular Expression--"|", "[]" and "()"

/* This time you need to write a regular expression that matches all URL contained in the string. 

The rules:

1) URL start with ```http:// or https://```
2) URL end with ```.com``` or ```.net```
3) The middle part of URL can use letters, numbers and dots
4) Need to ignore case, and a string may contain multiple URLs
5) Your regular expression name should be ```regex``` and your result should be a string array. */

// let regex = /https?:\/\/([a-z\d\.]+){1,}\.(com|net)/gi
// let regex = /https?:\/\/[a-z\d\.]+\.(com|net)/gi
let regex = /https?:\/\/[a-z.0-9]+\.(com|net)/gi
// let regex = /https?:\/\/[a-z\d\.]+\.(com|net)/gi
// let regex=/(http|https):\/\/[a-z\d.]+\.(net|com)/gi

q = "http://codewars.com".match(regex) // [ 'http://codewars.com' ]
q
q = "http://www.codewars.com".match(regex) // [ 'http://www.codewars.com' ]
q
q = "HTTP://CODEWARS.COM".match(regex) // [ 'HTTP://CODEWARS.COM' ]
q
q = "https://www.codewars.com".match(regex) // [ 'https://www.codewars.com' ]
q
q = "http://www.codewars.net".match(regex) // [ 'http://www.codewars.net' ]
q
q = "1234http://www.codewars.comabcd".match(regex) // [ 'http://www.codewars.com' ]
q
q = "http://www.codewars1.com!@#$%http://www.codewars2.net".match(regex) // [ 'http://www.codewars1.com', 'http://www.codewars2.net' ]
q
q = "http://www.codewars1.comabchttp://www.codewars2.net".match(regex) // [ 'http://www.codewars1.com', 'http://www.codewars2.net' ]
q
q = "http://www.codewars.com.net".match(regex) // [ 'http://www.codewars.com.net' ]
q
q = "http://www.codewars.com.fak".match(regex) // [ 'http://www.codewars.com' ]
q
q = "ftp://www.codewars.com".match(regex) // null
q
q = "http://www.code#wars.com".match(regex) // null
q
q = "http://www.codewars.org".match(regex) // null
q
q = "http://www . codewars . com".match(regex) // null
q
q = "http://mail@codewars.com".match(regex) // null
q
q = "http://.com".match(regex) // null
q