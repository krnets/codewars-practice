import java.util.stream.IntStream;

/*
Given a non-empty array of integers, return the result of multiplying the values together in order.

        [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
*/
/*
public class Kata {
    public static int grow(int[] x) {
        int result = 1;
        for (int val : x)
            result *= val;
        return result;
    }
}*/
public class Kata {
    public static int grow(int[] x) {
        return IntStream.of(x).reduce(1, (a, b) -> a * b);
    }
}
