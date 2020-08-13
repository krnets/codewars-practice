/*
Implement the method reduce, which accepts three arguments:

        linked list (head)
        bi-function - (accumulated_value, current_element_data)
        initial value

This method should return the result of applying the given function on every element
with the accumulating result, starting with the initial value.

Note: the list may be null and can hold any type of value.

Given the list: 1 -> 2 -> 3,
the function (acc, curr) => acc + curr and an initial value of 0, reduce should return 6, because:

        (0, 1) and the function (acc, curr) => acc + curr gives 1
        (1, 2) and the function (acc, curr) => acc + curr gives 3
        (3, 3) and the function (acc, curr) => acc + curr gives 6

Given the list: 1 -> 2 -> 3 -> 4,
the function (acc, curr) => acc * curr and an initial value of 1, reduce should return 24

        The linked list is defined as follows:
*/

import java.util.function.BiFunction;

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
    static <T> T reduce(Node<T> head, BiFunction<T, T, T> f, T init) {
        T acc = init;
        while (head != null) {
            acc = f.apply(acc, head.data);
            head = head.next;
        }
        return acc;
    }
}*/

public class Solution {
    static <T> T reduce(Node<T> head, BiFunction<T, T, T> f, T init) {
        while (head != null) {
            init = f.apply(init, head.data);
            head = head.next;
        }
        return init;
    }
}

/*
public class Solution {
    static <T> T reduce(Node<T> head, BiFunction<T, T, T> f, T init) {
        for (; head != null; head = head.next) {
            init = f.apply(init, head.data);
        }
        return init;
    }
}
*/

/*
public class Solution {
    static <T> T reduce(Node<T> head, BiFunction<T, T, T> f, T init) {
        for (Node<T> node = head; node != null; node = node.next) {
            init = f.apply(init, node.data);
        }
        return init;
    }
}
*/

/*
public class Solution {
    static <T> T reduce(Node<T> head, BiFunction<T, T, T> f, T init) {
        return head == null ? init : reduce(head.next, f, f.apply(init, head.data));
    }
}
*/
