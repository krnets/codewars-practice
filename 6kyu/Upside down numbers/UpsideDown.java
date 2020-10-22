/*
Consider the numbers 6969 and 9116.
When you rotate them 180 degrees (upside down), these numbers remain the same.
To clarify, if we write them down on a paper and turn the paper upside down,
the numbers will be the same. Try it and see!
Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range.
For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10.
They are 0, 1, 8.

More examples in the test cases.
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class UpsideDown {
    public int solve(int x, int y) {
        return (int) IntStream.range(x, y)
                .filter(this::isUpsideDown)
                .count();
    }

    private boolean isUpsideDown(int n) {
        var b = String.valueOf(n);

        var c = new StringBuilder(b).reverse().toString();

        var d = c.replace("6", "-")
                .replace("9", "6")
                .replace("-", "9");

        return n == Integer.parseInt(d);
    }
}