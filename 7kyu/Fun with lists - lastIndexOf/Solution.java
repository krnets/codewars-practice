/*
Implement the method lastIndexOf, which accepts a linked list (head) and a value,
and returns the index (zero based) of the last occurrence of that value if exists, or -1 otherwise.

Note: the list may be null and can hold any type of value.

For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, lastIndexOf should return 3.

The linked list is defined as follows:
*/

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

/*
public class Solution {
    static int lastIndexOf(Node head, Object value) {
        int index = -1;
        for (int i = 0; head != null; head = head.next, i++) {
            if (head.data.equals(value))
                index = i;
        }
        return index;
    }
}*/

class Solution {
    static int lastIndexOf(Node head, Object value) {
        if (head == null) return -1;
        int index = lastIndexOf(head.next, value);
        return index + (index > -1 || head.data.equals(value) ? 1 : 0);
    }
}
