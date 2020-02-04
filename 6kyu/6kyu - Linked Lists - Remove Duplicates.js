// 6kyu - Linked Lists - Remove Duplicates

/* Write a RemoveDuplicates() function which takes a list sorted in increasing order and 
deletes any duplicate nodes from the list. Ideally, the list should only be traversed once. 
The head of the resulting list should be returned.

var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null

If the passed in list is null/None/nil, simply return null.

Note: Your solution is expected to work on long lists. Recursive solutions may fail due to stack size limitations.

The push() and buildOneTwoThree() functions need not be redefined. */


function Node(data) {
    this.data = data;
    this.next = null;
}

function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

const buildList = (array) => array.reduce((head, data) => push(head, data), null)
const buildOneTwoThree = () => buildList([3, 2, 1])
const buildOneTwoThreeFourFiveSix = () => buildList([6, 5, 4, 3, 2, 1])

function removeDuplicates(head) {
    for (let p = head; p; p = p.next)
        while (p.next && p.data == p.next.data)
            p.next = p.next.next;
    return head;
}

// Test.it("should be able to handle an empty list.", function() {
q = removeDuplicates(null) // null, "removing duplicates from null should return null.")
q
// Test.it("should be able to handle a list of length 1.", function() {
q = removeDuplicates(new Node(23)).data // 23, "removing duplicates from linked list consisting of one node should return the node.");
q
// Test.it("should be able to handle a list without duplicates.", function() {
q = removeDuplicates(buildOneTwoThree()) // buildOneTwoThree(), "removing duplicates from a linked list without duplicates node should return the list."
q
q = removeDuplicates(buildOneTwoThreeFourFiveSix()) // buildOneTwoThreeFourFiveSix(), "removing duplicates from linked list without duplicates node should return the list."
q
// Test.it("should be able to handle a list with duplicates.", function() {
q = removeDuplicates(buildList([1, 2, 2])) // buildList([1, 2]), "should remove the duplicate '2' entries"
q
q = removeDuplicates(buildList([1, 1, 1, 1, 1])) // buildList([1]), "should remove the duplicate '1' entries"
q
q = removeDuplicates(buildList([1, 2, 3, 3, 4, 4, 5])) // buildList([1, 2, 3, 4, 5]), "should remove the duplicate '3' and '4' entries"
q
q = removeDuplicates(buildList([1, 1, 1, 1, 2, 2, 2, 2])) // buildList([1, 2]), "should remove the duplicate '1' and '2' entries"
q