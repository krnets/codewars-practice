// 7kyu - Linked Lists - Move Node

/* Write a MoveNode() function which takes the node from the front of the source list and moves it to the 
front of the destintation list. You should throw an error when the source list is empty. For simplicity, 
we use a Context object to store and return the state of the two linked lists. A Context object containing 
the two mutated lists should be returned by moveNode.

var source = 1 -> 2 -> 3 -> null
var dest = 4 -> 5 -> 6 -> null
moveNode(source, dest).source === 2 -> 3 -> null
moveNode(source, dest).dest === 1 -> 4 -> 5 -> 6 -> null

MoveNode() is a handy utility function to have for later problems.  */

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

function Context(source, dest) {
    this.source = source;
    this.dest = dest;
}

// function moveNode(source, dest) {
//     if (!source) throw new Error('Source list is empty');
//     let newSource = source.next;
//     source.next = dest;
//     return new Context(newSource, source);
// }


function moveNode(source, dest) {
    if (!source) throw new Error('Source list is empty');
    return new Context(source.next, new Node(source.data, dest));
}

// Test.describe("tests for moving a node from the head of one list to another."
// Test.it("should be able to handle two empty lists."
// q = moveNode(null, null) // "error should be thrown when source list is empty"
// q
// Test.it("should be able to handle one empty list.", function() {
// q = moveNode(null, new Node(23)) // Test.expectError("error should be thrown when source list is empty", function () {
// q
q = moveNode(buildOneTwoThree(), null) // new Context(buildList([2, 3]), new Node(1))
q
// Test.it("should be able to handle two non-empty lists.", function() {
q = moveNode(buildOneTwoThree(), buildOneTwoThree()) // new Context(buildList([2, 3]), buildList([1, 1, 2, 3]))
q
q = moveNode(buildOneTwoThreeFourFiveSix(), buildOneTwoThreeFourFiveSix()) // new Context(buildList([2, 3, 4, 5, 6]), buildList([1, 1, 2, 3, 4, 5, 6]))
q
q = moveNode(buildList([1, 2, 3, 4, 5, 6, 7]), buildList([4, 5, 6, 7])) // new Context(buildList([2, 3, 4, 5, 6, 7]), buildList([1, 4, 5, 6, 7]))
q