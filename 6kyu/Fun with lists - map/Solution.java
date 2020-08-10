/*
Implement the method map, which accepts a linked list (head)
and a mapping function, and returns a new linked list (head)
where every element is the result of applying the given mapping method
to each element of the original list.

Note: the list may be null and can hold any type of value.

For example: Given the list: 1 -> 2 -> 3, and the mapping function x => x * 2,
             map should return 2 -> 4 -> 6

The linked list is defined as follows:
*/

import java.util.function.Function;

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
    static <T, R> Node<R> map(Node<T> head, Function<T, R> f) {
        while (head != null) {
            var node = new Node<>(f.apply(head.data));
            node.next = map(head.next, f);
            return node;
        }
        return null;
    }
}
*/

/*
public class Solution {
    static <T, R> Node<R> map(Node<T> head, Function<T, R> f) {
        return head == null ? null : new Node<>(f.apply(head.data), map(head.next, f));
    }
}
*/

/*
public class Solution {
    static <T, R> Node<R> map(Node<T> head, Function<T, R> f) {
        if (head == null) return null;

        Node<R> headR = new Node(f.apply(head.data));
        var currentT = head;
        var currentR = headR;

        while (currentT.next != null) {
            currentR.next = new Node(f.apply(currentT.next.data));
            currentT = currentT.next;
            currentR = currentR.next;
        }
        return headR;
    }
}
*/
/*
public class Solution {
    static <T, R> Node<R> map(Node<T> head, Function<T, R> f) {
        if (head == null) return null;

        Node<R> headR = new Node(f.apply(head.data));
        var currentR = headR;

        while (head.next != null) {
            currentR.next = new Node(f.apply(head.next.data));
            head = head.next;
            currentR = currentR.next;
        }
        return headR;
    }
}
*/
public class Solution {
    static <T, R> Node<R> map(Node<T> head, Function<T, R> f) {
        var retList = new Node<R>(null);
        var current = retList;
        while (head != null) {
            current.next = new Node(f.apply(head.data));
            current = current.next;
            head = head.next;
        }
        return retList.next;
    }
}
