/*
In this kata you need to create a function that takes a 2D array/list of non-negative integer pairs
and returns the sum of all the "saving" that you can have getting the LCM of each couple of number
compared to their simple product.

        For example, if you are given:
        [[15,18], [4,5], [12,60]]

        Their product would be:
        [270, 20, 720]

        While their respective LCM would be:
        [90, 20, 60]

        Thus the result should be:
        (270-90)+(20-20)+(720-60)==840

This is a kata that I made, among other things, to let some of my trainees familiarize with the euclidean algorithm,
a really neat tool to have on your belt.
*/

import java.util.Arrays;
import java.util.stream.IntStream;

public class Solution {
    public static int sumDifferencesBetweenProductsAndLCMs(final int[][] pairs) {
        var pairProduct = Arrays.stream(pairs).mapToInt(pair -> pair[0] * pair[1]).toArray();
        var pairLCM = Arrays.stream(pairs).mapToInt(Solution::LCM).toArray();

        return IntStream.range(0, pairs.length).map(i -> pairProduct[i] - pairLCM[i]).sum();
    }

    static int LCM(int[] pair) {
        int a = pair[0];
        int b = pair[1];
        return a * b / GCD(a, b);
    }

    static int GCD(int a, int b) {
        return Math.max(b == 0 ? a : GCD(b, a % b), 1);
    }
}

