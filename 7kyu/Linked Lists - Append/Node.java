/*
Write an Append() function which appends one linked list to another.
The head of the resulting list should be returned.

        var listA = 1 -> 2 -> 3 -> null
        var listB = 4 -> 5 -> 6 -> null
        append(listA, listB) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null

If both listA and listB are null, return null.
If one list is null and the other is not, simply return the non-null list.
*/

class Node {
    int data;
    Node next;

    Node(final int data) {
        this.data = data;
    }

    public Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }

    public static Node append(Node listA, Node listB) {
        if (listA == null) return listB;
        Node pointerA = listA;
        while (pointerA.next != null) {
            pointerA = pointerA.next;
        }
        pointerA.next = listB;
        return listA;
    }
}