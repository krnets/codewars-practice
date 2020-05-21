// 6kyu - Linked Lists - Insert Sort

/* Write an InsertSort() function which rearranges nodes in a linked list so they are sorted in increasing order. 
You can use the SortedInsert() function that you created in the "Linked Lists - Sorted Insert" kata below. 
The InsertSort() function takes the head of a linked list as an argument and must return the head of the linked list.

var list = 4 -> 3 -> 1 -> 2 -> null
insertSort(list) === 1 -> 2 -> 3 -> 4 -> null

If the passed in head node is null or a single node, return null or the single node, respectively. 
You can assume that the head node will always be either null, a single node, or a linked list consisting of multiple nodes.

The push(), buildOneTwoThree(), and sortedInsert() functions need not be redefined. */

function Node(data, next = null) {
    this.data = data;
    this.next = next;
}

function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

const buildNodes = (array) => array.reduce((head, data) => push(head, data), null)
// const buildNodes = (array) => array.reduce((head, data) => { let node = new Node(data); node.next = head; return node }, null)
const buildOneTwoThree = () => buildNodes([3, 2, 1])
const buildThreeTwoOne = () => buildNodes([1, 2, 3])
const buildOneTwo = () => buildNodes([2, 1])
const buildTwoOne = () => buildNodes([1, 2])

q = buildOneTwoThree()
// Node { data: 1, next: Node { data: 2, next: Node { data: 3, next: null } } }
q
q = buildThreeTwoOne()
// Node { data: 3, next: Node { data: 2, next: Node { data: 1, next: null } } } 
q

// function sortedInsert(head, data) {
//     if (!head || data < head.data)
//         return push(head, data);
//     head.next = sortedInsert(head.next, data);
//     return head;
// }

// function insertSort(head) {
//     if (!head) return null;
//     return sortedInsert(insertSort(head.next), head.data);
// }

// function insertSort(head) {
//     if (!head) return null;
//     let sorted = new Node(head.data);
//     while (head = head.next) sorted = sortedInsert(sorted, head.data);
//     return sorted;
// }

// function sortedInsert(head, data) {
//     return !head || data < head.data ?
//         new Node(data, head) :
//         new Node(head.data, sortedInsert(head.next, data));
// }

function sortedInsert(head, data) {
    return !head || data < head.data ?
        new Node(data, head) :
        new Node(head.data, sortedInsert(head.next, data));
}

function insertSort(head) {
    return head ? sortedInsert(insertSort(head.next), head.data) : null;
}

// Test.it("should be able to handle an empty list.", function() {
q = insertSort(null) // null, "sorting an empty linked list should return null."
q
// Test.it("should be able to handle a list of length 1.", function() {
q = insertSort(new Node(5)).data // 5, "list should be return if length is 1."
q
// Test.it("should be able to handle a pre-sorted list of length 2.", function() {
q = insertSort(buildOneTwo()).data // 1, "Node at index 0 of InsertSort(1 -> 2) should return 1."
q
q = insertSort(buildOneTwo()).next.data // 2, "Node at index 1 InsertSort(1 -> 2) should return 2."
q
q = insertSort(buildOneTwo()).next.next // null, "Index 2 of InsertSort(1 -> 2) should return null."
q
// Test.it("should be able to handle a reverse sorted list of length 2.", function() {
q = insertSort(buildTwoOne()).data // 1, "Node at index 0 of InsertSort(2 -> 1) should return 1."
q
q = insertSort(buildTwoOne()).next.data // 2, "Node at index 1 InsertSort(2 -> 1) should return 2."
q
q = insertSort(buildTwoOne()).next.next // null, "Index 2 of InsertSort(2 -> 1) should return null."
q
// Test.it("should be able to handle a pre-sorted list of length 3.", function() {
q = insertSort(buildOneTwoThree()).data // 1, "Node at index 0 of InsertSort(1 -> 2 -> 3) should return 1."
q
q = insertSort(buildOneTwoThree()).next.data // 2, "Node at index 1 of InsertSort(1 -> 2 -> 3) should return 2."
q
q = insertSort(buildOneTwoThree()).next.next.data // 3, "Node at index 2 of InsertSort(1 -> 2 -> 3) should return 3."
q
q = insertSort(buildOneTwoThree()).next.next.next // null, "Value at index 3 of InsertSort(1 -> 2 -> 3) should be null."
q
// Test.it("should be able to handle a reverse sorted list of length 3.", function() {
q = insertSort(buildThreeTwoOne()).data // 1, "Node at index 0 of InsertSort(3 -> 2 -> 1) should return 1."
q
q = insertSort(buildThreeTwoOne()).next.data // 2, "Node at index 1 of InsertSort(3 -> 2 -> 1) should return 2."
q
q = insertSort(buildThreeTwoOne()).next.next.data // 3, "Node at index 2 of InsertSort(3 -> 2 -> 1) should return 3."
q
q = insertSort(buildThreeTwoOne()).next.next.next // null, "Value at index 3 of InsertSort(3 -> 2 -> 1) should be null."
q
// Test.it("should be able to handle an unordered list of length > 3.", function() {
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).data // 1, "Node at index 0 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should return 1."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.data // 2, "Node at index 1 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should return 2."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.data // 2, "Node at index 2 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should return 2."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.data // 3, "Value at index 3 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be 3."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.next.data // 4, "Value at index 4 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be 4."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.next.next.data // 5, "Value at index 5 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be 5."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.next.next.next.data // 6, "Value at index 6 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be 6."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.next.next.next.next.data // 8, "Value at index 7 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be 8."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.next.next.next.next.next.data // 9, "Value at index 8 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be 9."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.next.next.next.next.next.next.data // 9, "Value at index 9 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be 9."
q
q = insertSort(buildNodes([4, 8, 1, 3, 2, 9, 6, 5, 9, 2])).next.next.next.next.next.next.next.next.next.next // null, "Value at index 10 of InsertSort(4 -> 8 -> 1 -> 3 -> 2 -> 9 -> 6 -> 5 -> 9 ->2) should be null."
q