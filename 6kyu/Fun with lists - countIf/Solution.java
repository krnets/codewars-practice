/*
Implement the method countIf, which accepts a linked list (head) and a predicate function,
and returns the number of elements which apply to the given predicate.

Note: the list may be null and can hold any type of value.

For example: Given the list: 1 -> 2 -> 3, and the predicate x => x >= 2,
            countIf  should return 2, since x >= 2 applies to both 2 and 3.

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
public class Solution {
    static <T> int countIf(Node<T> head, Predicate<T> p) {
        int count = 0;
        while (head != null) {
            if (p.test(head.data))
                count++;
            head = head.next;
        }
        return count;
    }
}
*/

public class Solution {
    static <T> int countIf(Node<T> head, Predicate<T> p) {
        return head == null ? 0 : (p.test(head.data) ? 1 : 0) + countIf(head.next, p);
    }
}
