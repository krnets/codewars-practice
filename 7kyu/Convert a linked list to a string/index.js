// 7kyu - Convert a linked list to a string

/* Preloaded for you is a class Node used to construct linked lists in this Kata.

Create a function stringify which accepts an argument list and returns a string representation of the list. 
The string representation of the list starts with the value of the current Node, specified by its data property, 
followed by a whitespace character, an arrow and another whitespace character (" -> "), followed by the rest of the list. 
The end of the string representation of a list must always end with null
(all caps or all lowercase depending on the language you are undertaking this Kata in). For example, given the following list:

new Node(1, new Node(2, new Node(3)))

... its string representation would be:

"1 -> 2 -> 3 -> null"

And given the following linked list:

new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))

... its string representation would be:

"0 -> 1 -> 4 -> 9 -> 16 -> null"

Note that null itself is also considered a valid linked list. In that case, its string representation would simply be "null"
For the simplicity of this Kata, you may assume that any Node in this Kata may only contain non-negative integer values. 
For example, you will not encounter a Node whose data property is "Hello World". */

class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

// function stringify(list) {
//     if (list == null) return 'null'
//     return list.data + ' -> ' + stringify(list.next)
// }

const stringify = (list) => list ? list.data + ' -> ' + stringify(list.next) : 'null'


q = new Node(1, new Node(2, new Node(3))) // "1 -> 2 -> 3 -> null"
q

q = stringify(new Node(1, new Node(2, new Node(3)))) // "1 -> 2 -> 3 -> null"
q
q = stringify(new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))) // "0 -> 1 -> 4 -> 9 -> 16 -> null"
q
q = stringify(null) // "null"
q