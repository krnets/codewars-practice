// 7kyu - Fun with lists: length

/* Implement the method length, which accepts a linked list (head), and returns the length of the list.
For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.
Note: the list may be null and can hold any type of value. */

function Node(data, next = null) {
    this.data = data;
    this.next = next;
}

// function length(head) {
//     let count = 0
//     while (head) {
//         head = head.next
//         count++
//     }
//     return count
// }

// const length = head => head ? 1 + length(head.next) : 0
const length = head => head instanceof Node ? 1 + length(head.next) : 0

q = length(null) // 0
q
q = length(listFromArray([1, 2, 3, 4])) // 4
q
