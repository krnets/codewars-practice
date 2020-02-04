// 7kyu - Linked Lists - Push & BuildOneTwoThree

/* Write push() and buildOneTwoThree() functions to easily update and initialize linked lists. 
Try to use the push() function within your buildOneTwoThree() function.

Here's an example of push() usage:

var chained = null
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null

The push function accepts head and data parameters, where head is either a node object or null.
Your push implementation should be able to create a new linked list/node when head is null.

The buildOneTwoThree function should create and return a linked list with three nodes: 1 -> 2 -> 3 -> null */

// function push(head, data) {
//     let node = new Node(data);
//     node.next = head;
//     return node;
// }

// function buildOneTwoThree() {
//     let a = null;
//     a = push(a, 3);
//     a = push(a, 2);
//     a = push(a, 1);
//     return a;
// }

// function Node(data, next) {
//     this.data = data;
//     this.next = next || null;
// }

// function push(head, data) {
//     return new Node(data, head);
// }

// function buildOneTwoThree() {
//     return [3, 2, 1].reduce((head, data) => push(head, data), null)
// }

class Node {
    constructor(data, next) {
        this.data = data;
        this.next = next || null;
    }
}
const push = (head, data) => new Node(data, head);
const build = (...args) => args.reduce(push, null);
const buildOneTwoThree = build.bind(null, 3, 2, 1);


q = push(null, 1).data // 1, "Should be able to create a new linked list with push()."
q
q = push(null, 1).next // null, "Should be able to create a new linked list with push()."
q
q = push(new Node(1), 2).data // 2, "Should be able to prepend a node to an existing node."
q
q = push(new Node(1), 2).next.data // 1, "Should be able to prepend a node to an existing node."
q
q = buildOneTwoThree().data // 1, "First node should should have 1 as data."
q
q = buildOneTwoThree().next.data // 2, "First node should should have 1 as data."
q
q = buildOneTwoThree().next.next.data // 3, "Second node should should have 2 as data."
q
q = buildOneTwoThree().next.next.next // null, "Third node should should have 3 as data."
q