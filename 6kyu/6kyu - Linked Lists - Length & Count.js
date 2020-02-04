// 6kyu - Linked Lists - Length & Count

/* Implement Length() to count the number of nodes in a linked list.

length(null) => 0
length(1 -> 2 -> 3 -> null) => 3

Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4

I've decided to bundle these two functions within the same Kata since they are both very similar.

The push() and buildOneTwoThree() functions do not need to be redefined. */

function Node(data) {
    this.data = data;
    this.next = null;
}

function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

function buildOneTwoThree() {
    return [3, 2, 1].reduce((head, data) => push(head, data), null)
}

// function length(head) {
//     for (var i = 0; head; i++)
//         head = head.next;
//     return i;
// }
const length = (head) => !head ? 0 : 1 + length(head.next)

const count = (head, data) => !head ? 0 : (head.data == data ? 1 : 0) + count(head.next, data)

// function count(head, data) {
//     for (var i = 0, counter = 0; head; i++) {
//         if (data == head.data)
//             counter++;
//         head = head.next;
//     }
//     return counter;
// }


list = buildOneTwoThree();
list
q = length(null) // 0, "Length of null list should be zero."
q
q = length(new Node(99)) // 1, "Length of single node list should be one."
q
q = length(list) // 3, "Length of the three node list should be three."
q

list = buildOneTwoThree();
list
q = count(list, 1) // 1, "list should only contain one 1."
q
q = count(list, 2) // 1, "list should only contain one 2."
q
q = count(list, 3) // 1, "list should only contain one 3."
q
q = count(list, 99) // 0, "list should return zero for integer not found in list."
q
q = count(null, 1) // 0, "null list should always return count of zero."
q