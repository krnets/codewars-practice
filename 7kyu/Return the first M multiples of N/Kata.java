/*
Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n. Assume that m is a positive integer.

        multiples(3, 5.0)
        should return
        [5.0, 10.0, 15.0]
*/

/*
public class Kata {
    public static int[] multiples(int m, int n) {
        var result = new int[m];
        for (int i = 1; i <= m; i++)
            result[i - 1] = n * i;
        return result;
    }
}*/

/*
import java.util.stream.IntStream;

public class Kata {
    public static int[] multiples(int m, int n) {
        return IntStream.rangeClosed(1, m).map(i -> i * n).toArray();
    }
}
*/

import java.util.stream.IntStream;

public class Kata {
    public static int[] multiples(int m, int n) {
        return IntStream.iterate(n, i -> i + n).limit(m).toArray();
    }
}
