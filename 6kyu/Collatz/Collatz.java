/*
A collatz sequence, starting with a positive integer n,
is found by repeatedly applying the following function to n until n == 1 :

        f(n)={n/2, if n is even
              3n+1, if n is odd}

        A more detailed description of the collatz conjecture may be found on Wikipedia.

        Create a function collatz that returns a collatz sequence string starting with
        the positive integer argument passed into the function, in the following form:

        "X0->X1->...->XN"

        Where Xi is each iteration of the sequence and N is the length of the sequence.
        Sample Input

        Collatz.collatz(2) // should return "2->1"
        Collatz.collatz(3) // should return "3->10->5->16->8->4->2->1"
        Collatz.collatz(4) // should return "4->2->1"

        Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1.
*/

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
/*

public class Collatz {
    public static String collatz(int n) {
        List<Integer> seq = new ArrayList<>();
        seq.add(n);
        while (n > 1) {
            n = (n % 2 == 0) ? n / 2 : (n * 3) + 1;
            seq.add(n);
        }
        return seq.stream().mapToInt(Integer::intValue)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining("->"));
    }
}*/

/*
public class Collatz {
    public static String collatz(int n) {
        var seq = new StringBuilder().append(n);
        while (n > 1) {
            n = (n % 2 == 0) ? n / 2 : (3 * n) + 1;
            seq.append("->").append(n);
        }
        return seq.toString();
    }
}
*/

public class Collatz {
    public static String collatz(int n) {
        return n > 1 ? n + "->" + collatz(n % 2 == 0 ? n / 2 : 3 * n + 1) : "1";
    }
}
