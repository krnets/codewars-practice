// 6kyu - Linked Lists - Sorted Insert

/* Write a SortedInsert() function which inserts a node into the correct location of a pre-sorted linked list which is sorted in ascending order. SortedInsert takes the head of a linked list and data used to create a node as arguments. SortedInsert() should also return the head of the list.

sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)

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

function sortedInsert(head, data) {
    if (!head || data < head.data)
        return push(head, data);
    head.next = sortedInsert(head.next, data);
    return head;
}

q = sortedInsert(null, 23).data // 23, "should be able to insert a node on an empty/null list."
q
q = sortedInsert(null, 23).next // null, "value at index 1 should be null."
q
q = sortedInsert(buildOneTwoThree(), 0.5).data // 0.5, "should be able to insert new node at head of list."
q
q = sortedInsert(buildOneTwoThree(), 0.5).next.data // 1, "value for node at index 1 should be 1."
q
q = sortedInsert(buildOneTwoThree(), 0.5).next.next.data // 2, "value for node at index 2 should be 2."
q
q = sortedInsert(buildOneTwoThree(), 0.5).next.next.next.data // 3, "value for node at index 3 should be 3."
q
q = sortedInsert(buildOneTwoThree(), 0.5).next.next.next.next // null, "value at index 4 should be null."
q
q = sortedInsert(buildOneTwoThree(), 1.5).data // 1, "value for node at index 0 should be 1."
q
q = sortedInsert(buildOneTwoThree(), 1.5).next.data // 1.5, "value for node at index 1 should be 1.5"
q
q = sortedInsert(buildOneTwoThree(), 1.5).next.next.data // 2, "value for node at index 2 should be 2."
q
q = sortedInsert(buildOneTwoThree(), 1.5).next.next.next.data // 3, "value for node at index 3 should be 3."
q
q = sortedInsert(buildOneTwoThree(), 1.5).next.next.next.next // null, "value at index 4 should be null."
q
q = sortedInsert(buildOneTwoThree(), 2.5).data // 1, "head should remain unchanged after inserting new node at index 2"
q
q = sortedInsert(buildOneTwoThree(), 2.5).next.data // 2, "value at index 1 should remain unchanged after inserting new node at index 2"
q
q = sortedInsert(buildOneTwoThree(), 2.5).next.next.data // 2.5, "value for node at index 2 should be 2.5."
q
q = sortedInsert(buildOneTwoThree(), 2.5).next.next.next.data // 3, "value for node at index 3 should be 3."
q
q = sortedInsert(buildOneTwoThree(), 2.5).next.next.next.next // null, "value at index 4 should be null."
q
q = sortedInsert(buildOneTwoThree(), 3.5).data // 1, "head should remain unchanged after inserting new node at tail"
q
q = sortedInsert(buildOneTwoThree(), 3.5).next.data // 2, "value at index 1 should remain unchanged after inserting new node at tail"
q
q = sortedInsert(buildOneTwoThree(), 3.5).next.next.data // 3, "value for node at index 2 should be 3."
q
q = sortedInsert(buildOneTwoThree(), 3.5).next.next.next.data // 3.5, "value for node at index 3 should be 3.5."
q
q = sortedInsert(buildOneTwoThree(), 3.5).next.next.next.next // null, "value at index 4 should be null."
q