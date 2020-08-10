/*
Implement the method filter, which accepts a linked list (head) and a predicate function,
and returns a new linked list (head) which only contains the elements which apply to the given predicate.

Note: the list may be null and can hold any type of value.

For example: Given the list: 1 -> 2 -> 3, and the predicate x => x >= 2,
             filter should return 2 -> 3, since x >= 2 applies to both 2 and 3.

The linked list is defined as follows:
*/

import java.util.function.Predicate;

class Node<T> {
    public T data;
    public Node<T> next;

    Node(T data, Node next) {
        this.data = data;
        this.next = next;
    }

    Node(T data) {
        this(data, null);
    }
}


/*
class Solution {
    static <T> Node<T> filter(Node<T> head, Predicate<T> p) {
        return head != null ? p.test(head.data) ?
                new Node<>(head.data, filter(head.next, p)) :
                filter(head.next, p) : null;
    }
}
*/
/*
class Solution {
    static <T> Node<T> filter(Node<T> head, Predicate<T> p) {
        if (head == null) return null;
        return p.test(head.data) ? new Node<>(head.data, filter(head.next, p)) : filter(head.next, p);
    }
}
*/
/*
class Solution {
    static <T> Node<T> filter(Node<T> head, Predicate<T> p) {
        Node last = null;
        while (head != null) {
            if (p.test(head.data)) {
                var first = new Node<>(head.data);
                first.next = filter(head.next, p);
                return first;
            }
            head = head.next;
        }
        return last;
    }
}
*/
class Solution {
    static <T> Node<T> filter(Node<T> head, Predicate<T> p) {
        while (head != null) {
            if (p.test(head.data)) {
                var node = new Node<>(head.data);
                node.next = filter(head.next, p);
                return node;
            }
            head = head.next;
        }
        return null;
    }
}
