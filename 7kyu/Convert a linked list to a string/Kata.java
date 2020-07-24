/*
Create a function stringify which accepts an argument list and returns a string representation of the list.
The string representation of the list starts with the value of the current Node, specified by its data property,
followed by a whitespace character, an arrow and another whitespace character (" -> "), followed by the rest of the list.
The end of the string representation of a list must always end with null (all caps or all lowercase depending on the
language you are undertaking this Kata in). For example, given the following list:

        new Node(1, new Node(2, new Node(3)))

        ... its string representation would be:

        "1 -> 2 -> 3 -> null"

        And given the following linked list:

        new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))

        ... its string representation would be:

        "0 -> 1 -> 4 -> 9 -> 16 -> null"

        Note that null itself is also considered a valid linked list.
        In that case, its string representation would simply be "null"

For the simplicity of this Kata, you may assume that any Node in this Kata may only contain non-negative integer values.
For example, you will not encounter a Node whose data/$data/Data property is "Hello World".
*/
class Node {
    private int data;
    private Node next;

    public Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }

    public Node(int data) {
        this.data = data;
        this.next = null;
    }

    public int getData() {
        return data;
    }

    public Node getNext() {
        return next;
    }
}

/*
public class Kata {
    public static String stringify(Node list) {
        if (list == null) return "null";
        Node pointer = list;
        var sb = new StringBuilder().append(pointer.getData()).append(" -> ");
        while (pointer.getNext() != null) {
            pointer = pointer.getNext();
            sb.append(pointer.getData());
            sb.append(" -> ");
        }
        return sb.append("null").toString();
    }
}
*/

public class Kata {
    public static String stringify(Node list) {
        var sb = new StringBuilder();
        Node pointer = list;
        while (pointer != null) {
            sb.append(pointer.getData());
            sb.append(" -> ");
            pointer = pointer.getNext();
        }
        return sb.append("null").toString();
    }
}

/*
public class Kata {
    public static String stringify(Node list) {
        return list == null ? "null" : list.getData() + " -> " + stringify(list.getNext());
    }
}
*/
