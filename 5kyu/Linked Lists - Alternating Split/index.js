// 5kyu - Linked Lists - Alternating Split

/* Write an AlternatingSplit() function that takes one list and divides up its nodes to make two smaller lists. 
The sublists should be made from alternating elements in the original list. 
So if the original list is a -> b -> a -> b -> a -> null 
then one sublist should be a -> a -> a -> null 
and the other should be b -> b -> null.


var list = 1 -> 2 -> 3 -> 4 -> 5 -> null
alternatingSplit(list).first === 1 -> 3 -> 5 -> null
alternatingSplit(list).second === 2 -> 4 -> null */

function Node(data) {
    this.data = data;
    this.next = null;
}

function Context(first, second) {
    this.first = first;
    this.second = second;
}

function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

const buildList = (array) => array.reduce((head, data) => push(head, data), null)
const buildOneTwo = () => buildList([2, 1])
const buildOneTwoThree = () => buildList([3, 2, 1])
const buildOneTwoThreeFourFiveSix = () => buildList([6, 5, 4, 3, 2, 1])

// function alternatingSplit(head) {
//     if (!head || !head.next) throw Error('Invalid argument');
//     let first = new Node();
//     let second = new Node();
//     let current = [first, second]
//     let index = 0;
//     while(head) {
//         let node = new Node(head.data);
//         current[index % 2].next = node;
//         current[index % 2] = node;
//         index++;
//         head = head.next;
//     }
//     return new Context(first.next, second.next)
// }

// function alternatingSplit(head) {
//     if (!head || !head.next) throw Error('Invalid argument');
//     let listA = new Node();
//     let listB = new Node();
//     let current = [listA, listB];
//     for (let i = 0; head; i++) {
//         let node = new Node(head.data);
//         current[i % 2].next = node;
//         current[i % 2] = node;
//         head = head.next;
//     }
//     return new Context(listA.next, listB.next);
// }

// function alternatingSplit(head) {
//     if (!head || !head.next) throw Error('Invalid arguments');
//     let frame = [head, head.next];
//     let lists = new Context(...frame);
//     for (let i = 0, j = 1; frame[j];) {
//         frame[i] = frame[i].next = frame[j].next;
//         [i, j] = [j, i];
//     }
//     return lists;
// }

function split(head) {
    let list = new Node(head.data);
    if (head.next && head.next.next)
        list.next = split(head.next.next);
    return list;
}

function alternatingSplit(head) {
    if (!head || !head.next) throw new Error('invalid arguments');
    return new Context(split(head), split(head.next))
}

// Test.it("should be able to handle an empty list.", function() {
// q = alternatingSplit(null)
// "splitting a null list should throw an error." 
// q
// Test.it("should be able to handle a list of length 1.", function() {
// q = alternatingSplit(new Node(23))
// "splitting a single node list should throw an error"
// q
// Test.it("should be able to handle a list of length 2.", function() {
q = buildOneTwo()
q
q = alternatingSplit(buildOneTwo()).first.data // 1, "First index of first linked list should have value of 1."
q
q = alternatingSplit(buildOneTwo()).first.next // null, "Second index of first linked list should be null."
q
q = alternatingSplit(buildOneTwo()).second.data // 2, "First index of second linked list should have value of 2."
q
q = alternatingSplit(buildOneTwo()).second.next // null, "Second index of second linked list should be null."
q
// Test.it("should be able to handle a list of length 3", function() {
q = alternatingSplit(buildOneTwoThree()).first.data // 1, "First index of first linked list should have value of 1."
q
q = alternatingSplit(buildOneTwoThree()).first.next.data // 3, "Second index of first linked list should have value 3."
q
q = alternatingSplit(buildOneTwoThree()).first.next.next // null, "Third index of first linked list should be null."
q
q = alternatingSplit(buildOneTwoThree()).second.data // 2, "First index of second linked list should have value of 2."
q
q = alternatingSplit(buildOneTwoThree()).second.next // null, "Second index of second linked list should be null."
q
// Test.it("should be able to handle a list of length 6"
q = alternatingSplit(buildOneTwoThreeFourFiveSix()).first, buildList([1, 3, 5])
q
// "First list of alternatingSplit(1 -> 2 -> 3 -> ... 6 -> null) should be 1 -> 3 -> 5 -> null"
q = alternatingSplit(buildOneTwoThreeFourFiveSix()).second, buildList([2, 4, 6])
q
// "Second list of alternatingSplit(1 -> 2 -> 3 -> ... 6 -> null) should be 2 -> 4 -> 6 -> null"
q = alternatingSplit(buildOneTwoThreeFourFiveSix()).first.next.next.next
//  "Fourth index of first linked list should be null."
q
q = alternatingSplit(buildOneTwoThreeFourFiveSix()).second.next.next.next
//  null, "Fourth index of second linked list should be null."
q
// Test.it("should be able to handle a list of length 11"
q = alternatingSplit(buildList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).first, buildList([1, 3, 5, 7, 9, 11])
//  "First list of alternatingSplit(1 -> 2 -> 3 -> ... 11 -> null) should be 1 -> 3 -> 5 -> 7 -> 9 -> 11 -> null"
q
q = alternatingSplit(buildList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).second, buildList([2, 4, 6, 8, 10])
//  "Second list of alternatingSplit(1 -> 2 -> 3 -> ... 11 -> null) should be 2 -> 4 -> 6 -> 8 -> 10 -> null"
q
q = alternatingSplit(buildList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).first.next.next.next.next.next.next
// "Seventh index of first linked list should be null."
q
q = alternatingSplit(buildList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).second.next.next.next.next.next
//  "Sixth index of second linked list should be null."
q
// Test.it("should be able to handle are large unordered list."
q = alternatingSplit(buildList([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).first, buildList([5, 1, 3, 3, 8, 4])
//  "First list of alternatingSplit(5 -> 6 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 8 -> 5 -> 4 -> 1 -> null) 
// should be 5 -> 1 -> 3 -> 3 -> 8 -> 4 -> null"
q
q = alternatingSplit(buildList([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).second, buildList([6, 2, 3, 4, 5, 1])
//  "Second list of alternatingSplit(5 -> 6 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 8 -> 5 -> 4 -> 1 -> null) 
// should be 6 -> 2 -> 3 -> 4 -> 5 -> -> 1 -> null"
q
q = alternatingSplit(buildList([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).first.next.next.next.next.next.next
//  null, "Seventh index of first linked list should be null."
q
q = alternatingSplit(buildList([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).second.next.next.next.next.next.next
//  null, "Seventh index of second linked list should be null."
q