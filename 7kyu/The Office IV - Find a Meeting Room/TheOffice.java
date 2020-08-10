/*
Your job at E-Corp is both boring and difficult.
It isn't made any easier by the fact that everyone constantly wants to have a meeting with you,
and that the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room. Your job?
Find the first empty one and return its index (N.B. There may be more than one empty room in some test cases).

        'X' --> busy 'O' --> empty

        If all rooms are busy, return 'None available!'.
*/

/*
public class TheOffice {
    public static Object meeting(char[] x) {
        String s = String.valueOf(x);
        return s.contains("O") ? s.indexOf("O") : "None available!";
    }
}
*/

/*
public class TheOffice {
    public static Object meeting(char[] x) {
        int i = String.valueOf(x).indexOf("O");
        return i < 0 ? "None available!" : i;
    }
}
*/

import java.util.stream.IntStream;

public class TheOffice {
    public static Object meeting(char[] x) {
        return IntStream.range(0, x.length)
                .filter(i -> x[i] == 'O')
                .mapToObj(i -> (Object) i)
                .findFirst()
                .orElse("None available!");
    }
}
