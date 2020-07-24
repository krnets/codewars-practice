/*
Linked Lists - Push & BuildOneTwoThree

Write push() and buildOneTwoThree() functions to easily update and initialize linked lists.
Try to use the push() function within your buildOneTwoThree() function.

Here's an example of push() usage:

        var chained = null
        chained = push(chained, 3)
        chained = push(chained, 2)
        chained = push(chained, 1)
        push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null

The push function accepts head and data parameters, where head is either a node object or null/None/nil.
Your push implementation should be able to create a new linked list/node when head is null/None/nil.

The buildOneTwoThree function should create and return a linked list with three nodes:
1 -> 2 -> 3 -> null

Inspired by Stanford Professor Nick Parlante's excellent Linked List teachings.

I'm aware that there are better ways to create linked lists (class methods, reference pointers, etc.),
but not all languages have the same features. I'd like to keep the basic API consistent between language
translations for this kata.
*/

/*
class Node {
    int data;
    Node next = null;

    Node(final int data) {
        this.data = data;
    }

    public static Node push(final Node head, final int data) {
        Node current = new Node(data);
        current.next = head;
        return current;
    }

    public static Node buildOneTwoThree() {
        Node one = new Node(1);
        Node two = new Node(2);
        two.next = new Node(3);
        one.next = two;
        return one;
    }
}*/
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }

    public Node(Node head, int data) {
        this.next = head;
        this.data = data;
    }

    public static Node push(final Node head, final int data) {
        return new Node(head, data);
    }

    public static Node buildOneTwoThree() {
        Node current = new Node(3);
        current = Node.push(current, 2);
        current = Node.push(current, 1);
        return current;
    }
}
/*
    public static Node buildOneTwoThree() {
        Node chained;
        chained = push(null, 3);
        chained = push(chained, 2);
        chained = push(chained, 1);
        return chained;
    }
*/
