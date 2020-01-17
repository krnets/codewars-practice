// 8kyu - Word Count

/* Write a function that returns word count from a given string?

You have to ensure that spaces in string is a whitespace for real.

What we want and finish of work:

countWords("Hello"); // returns 1 as int
countWords("Hello, World!") // returns 2
countWords("No results for search term `s`") // returns 6
countWords(" Hello") // returns 1
// ... and so on

What kind of tests we got for your code:

    Function have to count words, but not spaces, so be sure that it does right.
    Empty string has no words.
    String with spaces around should be trimmed.
    Non-whitespace (ex. breakspace, unicode chars) should be assumed as delimiter
    Be sure that words with chars like -, ', ` are counted right. */


// const countWords = (str) => str.split(/\s+/).filter(Boolean).length
// const countWords = (str) => str.split(/\S+/).length - 1
// const countWords = (str) => (str.match(/[^\s]+/g) || []).length

q = countWords("Hello") // 1
q
q = countWords("Hello, World!") // 2
q
q = countWords("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.") //19
q
q = countWords("") // 0
q
q = countWords("With! Symbol@ #Around! (Every) %Word$") // 5
q
q = countWords("Dear   Victoria, I love  to press   space button.") // 8
q
q = countWords(" Arthur ") // 1
q
q = countWords(" David") // 1
q
q = countWords("Nelson ") // 1
q
q = countWords("  Hello Gomer  ") // 2
q
q = countWords("  Hello     Bart  ") // 2
q
q = countWords("﻿Hello﻿World ") // 2
q
q = countWords("Hello﻿World") // 2
q