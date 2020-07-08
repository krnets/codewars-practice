/*
Given an array of integers.

        Return an array, where the first element is the count of positives numbers
        and the second element is sum of negative numbers.

        If the input array is empty or null, return an empty array.

        For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
*/

public class Kata {
    public static int[] countPositivesSumNegatives(int[] input) {
        if (input == null || input.length == 0)
            return new int[]{};
        int countPos = 0, sumNeg = 0;
        for (int x : input) {
            if (x > 0) countPos++;
            if (x < 0) sumNeg += x;
        }
        return new int[]{countPos, sumNeg};
    }
}