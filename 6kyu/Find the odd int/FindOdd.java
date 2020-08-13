/*
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
*/

import java.util.stream.IntStream;

import static java.util.Arrays.stream;
import static java.util.stream.Collectors.*;

/*
public class FindOdd {
    public static int findIt(int[] a) {
        return IntStream.of(a)
                .boxed()
                .collect(groupingBy(x -> x, counting()))
                .entrySet()
                .stream()
                .filter(x -> x.getValue() % 2 != 0)
                .map(x -> x.getKey())
                .findFirst()
                .orElse(0);
    }
}*/
/*
public class FindOdd {
    public static int findIt(int[] a) {
        return stream(a).reduce(0, (x, y) -> x ^ y);
    }
}
*/
public class FindOdd {
    public static int findIt(int[] a) {
        int xor = 0;
        for (int x : a) {
            xor ^= x;
        }
        return xor;
    }
}
