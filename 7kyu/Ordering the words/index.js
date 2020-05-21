// 7kyu - Ordering the words!

/* Given a string, you need to write a method that order every letter in this string in ascending order.

Also, you should validate that the given string is not empty or null. If so, the method should return:

"Invalid String!"

Notes
• the given string can be lowercase and uppercase.
• the string could include spaces or other special characters like '# ! or ,'

"hello world" => " dehllloorw"
"bobby"       => "bbboy"
""            => "Invalid String!"
"!Hi You!"    => " !!HYiou" */

const orderWord = s => s ? [...s].sort().join('') : 'Invalid String!'

q = orderWord("Hello, World!") // " !,HWdellloor"
q
q = orderWord("bobby") // "bbboy"
q
q = orderWord("b") // "b"
q
q = orderWord("") // "Invalid String!"
q
q = orderWord("completesolution") // "ceeillmnooopsttu"
q
q = orderWord("\"][@!$*(^&%") // "!\"$%&(*@[]^"
q
q = orderWord("i\"d][@z!$r(^a&world%") // "!\"$%&(@[]^addilorrwz"
q
q = orderWord(null) // "Invalid String!"
q
q = orderWord("cba") // "abc"
q
q = orderWord("abc") // "abc"
q