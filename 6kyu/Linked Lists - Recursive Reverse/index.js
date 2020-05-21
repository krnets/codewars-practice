// 6kyu - Linked Lists - Recursive Reverse

/* Write a Recursive Reverse() function that recursively reverses a linked list. 
You may want to use a nested function for the recursive calls.

var list = 2 -> 1 -> 3 -> 6 -> 5 -> null
reverse(list) === 5 -> 6 -> 3 -> 1 -> 2 -> null  */

function Node(data, next = null) {
    this.data = data;
    this.next = next;
}

function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

const buildList = (array) => array.reduce((head, data) => push(head, data), null)
const buildRandomArray = (n) => Array(n).fill().map((_, i) => (Math.random() * n | 0) + 1)

// q = buildRandomArray(5)
// q
// 3 1 5 2 4  ->  4 2 5 1 3
// ^
//   ^

function reverse(head, prev = null) {
    return head ? reverse(head.next, new Node(head.data, prev)) : prev
}

// Test.describe("tests for iterative reversal of a linked list.", function() {
// Test.it("should be able to handle a null list.", function() {
q = reverse(null) // null, "should return null if passed in list is null.");
q
// Test.it("should be able to handle a list of length 1", function() {
var list = buildList([1])
list
q = reverse(list) // buildList([1]), "result should be 1 -> null."
q
// Test.it("should be able to handle lists of length 2", function() {
var list = buildList([1, 3]);
list
q = reverse(list) // buildList([3, 1]), "result should be 3 -> 1 -> null."
q
list = buildList([3, 1]);
list
q = reverse(list) // buildList([1, 3]), "result should be 1 -> 3 -> null."
q
// Test.it("should be able to handle lists of length 3", function() {
var list = buildList([1, 3, 8]);
q = reverse(list) // buildList([8, 3, 1]), "result should be 8 -> 3 -> 1 -> null."
q
list = buildList([8, 3, 1])
q = reverse(list) // buildList([1, 3, 8]), "result should be 1 -> 3 -> 8 -> null."
q
list = buildList([1, 8, 3])
q = reverse(list) // buildList([3, 8, 1]), "result should be 3 -> 8 -> 1 -> null."
q
list = buildList([3, 8, 1])
q = reverse(list) // buildList([1, 8, 3]), "result should be 1 -> 8 -> 3 -> null."
q
// Test.it("should be able to handle a list of length 8", function() {
var list = buildList([1, 3, 5, 7, 9, 11, 13, 15]);
q = reverse(list) // buildList([15, 13, 11, 9, 7, 5, 3, 1]), "result should be 15 -> 13 -> 11 ... -> 1 -> null."
q
list = buildList([15, 13, 11, 9, 7, 5, 3, 1]);
q = reverse(list) // buildList([1, 3, 5, 7, 9, 11, 13, 15]), "result should be 1 -> 3 -> 5 ... 15 -> null."
q
list = buildList([9, 1, 7, 3, 5, 15, 13, 11]);
q = reverse(list) // buildList([11, 13, 15, 5, 3, 7, 1, 9]), "result should be 11 -> 13 -> 15 -> 5 -> 3 -> 7 -> 1 -> 9 -> null."
q
list = buildList([1, 1, 1, 1, 1, 1, 1, 1]);
q = reverse(list) // buildList([1, 1, 1, 1, 1, 1, 1, 1]), "result should be 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> null."
q
// Test.it("should be able to handle a very large list.", function() {
var largeRandArr = buildRandomArray(1000);
var largeArray = largeRandArr.slice()
var list = buildList(largeArray.slice());
var largeReversedArray = largeArray.slice();
largeReversedArray.reverse();
q = reverse(list)
q
q = buildList(largeReversedArray) // "result should equal large reversed list."
q