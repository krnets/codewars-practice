// 6kyu - Linked Lists - Iterative Reverse

/* Write an iterative Reverse() function that reverses a linked list. 
Ideally, Reverse() should only need to make one pass of the list.

list : 2 -> 1 -> 3 -> 6 -> 5 -> null
reverse(list)
list : 5 -> 6 -> 3 -> 1 -> 2 -> null

The push() and buildOneTwoThree() functions need not be redefined. */

function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

const buildList = (array) => array.reduce((head, data) => push(head, data), null)

function Node(data) {
    this.data = data;
    this.next = null;
}

function reverse(head) {
    if (!head) return null;
    let current = head;
    let previous = null;
    while (current) {
        if (previous) {
            [previous, previous.next] = [new Node(current.data), previous];
        } else {
            previous = new Node(current.data);
        }
        current = current.next;
    }
    head.data = previous.data;
    head.next = previous.next;
    return head;
}

// should be able to handle a null list.
list = null;
reverse(list)
list // null

// should be able to handle a list of length 1
list = buildList([1]);
reverse(list)
list //  "result should be 1 -> null.");

// should be able to handle lists of length 2
list = buildList([1, 3]);
reverse(list)
//  3 -> 1 -> null
list

//  should be able to handle lists of length 3
list = buildList([8, 3, 1])
reverse(list)
//  1 -> 3 -> 8 -> null
list

list = buildList([1, 8, 3])
reverse(list)
//   3 -> 8 -> 1 -> null
list

// Test.it("should be able to handle a list of length 8", function() {
list = buildList([1, 3, 5, 7, 9, 11, 13, 15]);
reverse(list)
//  15 -> 13 -> 11 ... -> 1 -> null
list

list = buildList([15, 13, 11, 9, 7, 5, 3, 1]);
reverse(list)
//  1 -> 3 -> 5 ... 15 -> null
list

list = buildList([9, 1, 7, 3, 5, 15, 13, 11]);
reverse(list)
//  11 -> 13 -> 15 -> 5 -> 3 -> 7 -> 1 -> 9 -> null
list