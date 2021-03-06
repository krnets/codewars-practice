/* 8kyu - Sum of positive

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0. */

import java.util.Arrays;

public class Positive {
    /*
        public static int sum(int[] arr) {
            int result = 0;
            for (int x : arr) {
                if (x > 0)
                    result += x;
            }
            return result;
        }
    */
    public static int sum(int[] arr) {
        return Arrays.stream(arr).filter(v -> v > 0).sum();
    }
}
