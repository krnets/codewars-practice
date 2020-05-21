// 7kyu - Linked Lists - Get Nth Node

/* Implement a GetNth() function that takes a linked list and an integer index and 
returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, 
the second is index 1, ... and so on. So for the list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2

The index should be in the range [0..length-1]. If it is not, GetNth() should throw/raise an exception. 
You should also raise an exception if the list is empty/null.

Prerequisite Kata:

    Linked Lists - Push & BuildOneTwoThree
    Linked Lists - Length & Count

    The push() and buildOneTwoThree() functions do not need to be redefined. */


function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

function buildOneTwoThree() {
    return [3, 2, 1].reduce((head, data) => push(head, data), null)
}

function Node(data) {
    this.data = data;
    this.next = null;
}

function getNth(node, index) {
    if (!node) throw new Error('Invalid node at ' + index);
    return (index == 0) ? node : getNth(node.next, index - 1);
}

var list = buildOneTwoThree();
list
q = getNth(list, 0).data // 1, "First node should be located at index 0."
q
q = getNth(list, 1).data // 2, "Second node should be located at index 1."
q
q = getNth(list, 2).data // 3, "Third node should be located at index 2."
q
q = getNth(list, 3) // should throw error
q
q = getNth(list, 100) // should throw error
q
q = getNth(null, 0) // should throw error
q