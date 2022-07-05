/*
In this kata you have to correctly return who is the "survivor", ie:
the last element of a Josephus permutation.

Basically you have to assume that n people are put into a circle and that
they are eliminated in steps of k elements, like this:

        josephus_survivor(7,3) => means 7 people in a circle;
        one every 3 is eliminated until one remains

        [1,2,3,4,5,6,7] - initial sequence

        [1,2,4,5,6,7] => 3 is counted out
        [1,2,4,5,7] => 6 is counted out
        [1,4,5,7] => 2 is counted out
        [1,4,5] => 7 is counted out
        [1,4] => 5 is counted out

        [4] => 1 counted out, 4 is the last element - the survivor!

The above link about the "base" kata description will give you a more thorough
insight about the origin of this kind of permutation, but basically that's all
that there is to know to solve this kata.

Notes and tips: using the solution to the other kata to check your function may be helpful,
but as much larger numbers will be used, using an array/list to compute the number of
the survivor may be too slow; you may assume that both n and k will always be >=1.
*/

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class JosephusSurvivor {
    public static int josephusSurvivor(final int n, final int k) {
        var seq = IntStream.rangeClosed(1, n).boxed().collect(Collectors.toList());
        int i = 0;

        while (seq.size() > 1) {
            i = (i + k - 1) % seq.size();
            seq.remove(i);
        }
        return seq.get(0);
    }
}
*/

public class JosephusSurvivor {
    public static int josephusSurvivor(final int n, final int k) {
        int pos = 0;

        for (int i = 2; i <= n; i++) {
            pos = (pos + k) % i;
        }
        return pos + 1;
    }
}

/*
public class JosephusSurvivor {
    public static int josephusSurvivor(final int n, final int k) {
        return n == 1 ? 1 : (josephusSurvivor(n - 1, k) + k - 1) % n + 1;
    }
}
*/


/*
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

public class JosephusSurvivor {

    private static Node createLinkedList(Node head, int n) {
        Node newNode;
        Node currentNode = head;
        for (int i = head.data + 1; i <= n; i++) {
            newNode = new Node(i);
            currentNode.next = newNode;
            currentNode = newNode;
        }
        return currentNode;
    }

    public static int josephusSurvivor(final int n, final int k) {
        Node head = new Node(1);
        Node tail = createLinkedList(head, n);
        tail.next = head;
        Node previous = tail;
        Node current = head;
        int counter = 1;

        while (current.data != current.next.data) {
            if (counter == k) {
                previous.next = current.next;
                current = previous.next;
                counter = 0;
            } else {
                previous = previous.next;
                current = current.next;
            }
            counter++;
        }

        return current.data;
    }
}*/
