/*
You have to search all numbers from inclusive 1 to inclusive a given number x,
that have the given digit d in it.

        The value of d will always be 0 - 9.
        The value of x will always be greater than 0.

        You have to return as an array
        the count of these numbers,
        their sum
        and their product.

        For example:
        ``` x = 11 d = 1 -> Numbers: 1, 10, 11 Return: [3, 22, 110] ```
        If there are no numbers, which include the digit, return [0,0,0].
*/

import java.util.Arrays;
import java.util.stream.LongStream;

public class Kata {
    public static long[] NumbersWithDigitInside(long x, long d) {
        long[] arr = LongStream.rangeClosed(1, x)
                .mapToObj(String::valueOf)
                .filter(num -> num.contains(String.valueOf(d)))
                .mapToLong(Long::parseLong).toArray();
        long count = arr.length;
        long sum = Arrays.stream(arr).sum();
        long product = count > 0 ? Arrays.stream(arr).reduce(1, (a, b) -> a * b) : 0;
        return new long[]{count, sum, product};
    }
}
