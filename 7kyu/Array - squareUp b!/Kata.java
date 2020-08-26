/*
This is a question from codingbat

Given an integer n greater than or equal to 0, create and return an array with the following pattern:

        squareUp(3) => [0, 0, 1, 0, 2, 1, 3, 2, 1]
        squareUp(2) => [0, 1, 2, 1]
        squareUp(4) => [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]

        n<=1000.
*/


import static java.util.stream.IntStream.range;

public class Kata {
    public static int[] squareUp(int n) {
        return range(0, n * n)
//                .map(i -> (Math.abs((i % n) - n) <= i / n + 1) ? Math.abs((i % n) - n) : 0)
                .map(i -> (i / n + 1) < Math.abs(i % n - n) ? 0 : Math.abs(i % n - n))
                .toArray();
    }
}

/*
public class Kata {
    public static int[] squareUp(int n) {
        return range(0, n).flatMap(x -> range(0, n).map(y -> y < (n - x - 1) ? 0 : n - y)).toArray();
    }
}
*/
