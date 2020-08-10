/*
Implement the method length, which accepts a linked list (head), and returns the length of the list.
Note: the list may be null and can hold any type of value.

For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.

The linked list is defined as follows:
*/

import java.util.Optional;

class Node {
    public Object data;
    public Node next;

    Node(Object data, Node next) {
        this.data = data;
        this.next = next;
    }

    Node(Object data) {
        this(data, null);
    }
}

class Solution {
    static int length(Node head) {
        int count = 0;
//        Node current = head;
//        while (current != null) {
//            current = current.next;
        while (head != null) {
            head = head.next;
            count++;
        }
        return count;
    }
}

/*
class Solution {
    static int length(Node head) {
        return head == null ? 0 : 1 + length(head.next);
    }
}
*/

/*
class Solution {
    static int length(Node head) {
        return Optional.ofNullable(head)
                .map(node -> 1 + length(node.next))
                .orElse(0);
    }
}*/
