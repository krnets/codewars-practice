// 7kyu - Linked Lists - Append

/* Write an Append() function which appends one linked list to another. The head of the resulting list should be returned.

var listA = 1 -> 2 -> 3 -> null
var listB = 4 -> 5 -> 6 -> null
append(listA, listB) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null

If both listA and listB are null, return null. If one list is null and the other is not, simply return the non-null list.

The push() and buildOneTwoThree() functions need not be redefined.   */

function Node(data) {
    this.data = data;
    this.next = null;
}

function push(head, data) {
    let node = new Node(data);
    node.next = head;
    return node;
}

const buildNodes = (array) => array.reduce((head, data) => push(head, data), null)
const buildOneTwoThree = () => buildNodes([3, 2, 1])
const buildFourFiveSix = () => buildNodes([6, 5, 4])

// function append(listA, listB) {
//     if (!listA) return listB;
//     let pointerA = listA;
//     while (pointerA.next) {
//         pointerA = pointerA.next;
//     }
//     pointerA.next = listB;
//     return listA;
// }

function append(listA, listB) {
    if (!listA) return listB;
    listA.next = append(listA.next, listB);
    return listA;
}


q = append(null, null) // null, "appending two empty lists should return null.");
q
q = append(null, buildOneTwoThree()) // buildOneTwoThree(), "appending a list to null should return the list."
q
q = append(buildOneTwoThree(), null) // buildOneTwoThree(), "appending null to a list should return the list."
q
q = append(new Node(1), new Node(2)) // buildOneTwo(), "appending a list to another list should return the concatenated list."
q
q = append(new Node(2), new Node(1)) // buildTwoOne(), "appending a list to another list should return the concatenated list."
q
q = append(new Node(2), new Node(1)).next.next // null, "null should exist at end of concatenated linked list."
q
q = append(buildOneTwoThree(), buildFourFiveSix()) // buildOneTwoThreeFourFiveSix(), "appending a list to another list should return the concatenated list."
q
q = append(buildFourFiveSix(), buildOneTwoThree()) // buildFourFiveSixOneTwoThree(), "appending a list to another list should return the concatenated list."
q
q = append(buildFourFiveSix(), buildOneTwoThree()).next.next.next.next.next.next // null, "null should exist at end of concatenated linked list."
q