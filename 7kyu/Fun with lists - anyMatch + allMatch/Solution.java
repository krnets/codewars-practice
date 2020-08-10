/*
Implement the methods anyMatch & allMatch, which accepts a linked list (head)
and a predicate function, and returns true if any / all of the elements apply to the given predicate.

Note: the list may be null and can hold any type of value.

For example:

Given the list: 1 -> 2 -> 3, and the predicate x => x > 1,
anyMatch  should return true (both 2 & 3 are valid for this predicate),
and allMatch should return false (1 is not valid for this predicate)

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

    public void setNext(Node<T> next) {
        this.next = next;
    }
}


public class Solution {
    static <T> boolean anyMatch(Node<T> head, Predicate<T> p) {
        while (head != null) {
            if (p.test(head.data)) return true;
            head = head.next;
        }
        return false;
    }

    static <T> boolean allMatch(Node<T> head, Predicate<T> p) {
        return !anyMatch(head, p.negate());
    }
}