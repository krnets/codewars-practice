// 7kyu - Extending JavaScript Objects - Reverse String

/* Unfortunately, there's no a .reverse() method for the JavaScript String object.
Your task is to extend JavaScript String object, so you can reverse strings just like this:

'Hello, World!'.reverse() // The method should return: '!dlroW ,olleH'  */

String.prototype.reverse = function (string) {
    return [...this].reverse().join('')
}

q = 'Hello, World!'.reverse() // '!dlroW ,olleH'
q