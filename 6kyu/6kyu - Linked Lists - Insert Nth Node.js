// 6kyu - Linked Lists - Insert Nth Node

/* Implement an InsertNth() function which can insert a new node at any index within a list.

InsertNth() is a more general version of the Push() function that we implemented in the first kata listed below. 
Given a list, an index 'n' in the range 0..length, and a data element, add a new node to the list so that it has the given index. 
InsertNth() should return the head of the list.

insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)

You must throw/raise an exception if the index is too large. */

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

// function insertNth(head, index, data) {
//     if (index == 0) return push(head, data);
//     head.next = insertNth(head.next, index - 1, data);
//     return head;
// }

function insertNth(head, index, data) {
    if (index == 0) return push(head, data);
    if (head && index > 0) {
        head.next = insertNth(head.next, index - 1, data);
        return head;
    }
    throw new Error('Index is bigger than node chain');
}

q = insertNth(null, 0, 12).data // 12, "should be able to insert a node on an empty/null list."
q
q = insertNth(null, 0, 12).next // null, "value at index 1 should be null."
q
q = insertNth(buildOneTwoThree(), 0, 23).data // 23, "should be able to insert new node at head of list."
q
q = insertNth(buildOneTwoThree(), 0, 23).next.data // 1, "value for node at index 1 should be 1."
q
q = insertNth(buildOneTwoThree(), 0, 23).next.next.data // 2, "value for node at index 2 should be 2."
q
q = insertNth(buildOneTwoThree(), 0, 23).next.next.next.data // 3, "value for node at index 3 should be 3."
q
q = insertNth(buildOneTwoThree(), 0, 23).next.next.next.next // null, "value at index 4 should be null."
q
q = insertNth(buildOneTwoThree(), 1, 23).data // 1, "value for node at index 0 should be 1."
q
q = insertNth(buildOneTwoThree(), 1, 23).next.data // 23, "value for node at index 1 should be 23"
q
q = insertNth(buildOneTwoThree(), 1, 23).next.next.data // 2, "value for node at index 2 should be 2."
q
q = insertNth(buildOneTwoThree(), 1, 23).next.next.next.data // 3, "value for node at index 3 should be 3."
q
q = insertNth(buildOneTwoThree(), 1, 23).next.next.next.next // null, "value at index 4 should be null."
q
q = insertNth(buildOneTwoThree(), 2, 23).data // 1, "head should remain unchanged after inserting new node at index 2"
q
q = insertNth(buildOneTwoThree(), 2, 23).next.data // 2, "value at index 1 should remain unchanged after inserting new node at index 2"
q
q = insertNth(buildOneTwoThree(), 2, 23).next.next.data // 23, "value for node at index 2 should be 23."
q
q = insertNth(buildOneTwoThree(), 2, 23).next.next.next.data // 3, "value for node at index 3 should be 3."
q
q = insertNth(buildOneTwoThree(), 2, 23).next.next.next.next // null, "value at index 4 should be null."
q
q = insertNth(buildOneTwoThree(), 3, 23).data // 1, "head should remain unchanged after inserting new node at tail"
q
q = insertNth(buildOneTwoThree(), 3, 23).next.data // 2, "value at index 1 should remain unchanged after inserting new node at tail"
q
q = insertNth(buildOneTwoThree(), 3, 23).next.next.data // 3, "value for node at index 2 should be 3."
q
q = insertNth(buildOneTwoThree(), 3, 23).next.next.next.data // 23, "value for node at index 3 should be 23."
q
q = insertNth(buildOneTwoThree(), 3, 23).next.next.next.next // null, "value at index 4 should be null."
q
q = insertNth(buildOneTwoThree(), 4, 23) // should throw error
q