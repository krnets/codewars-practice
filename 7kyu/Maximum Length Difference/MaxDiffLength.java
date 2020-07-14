/*
You are given two arrays a1 and a2 of strings.
Each string is composed with letters from a to z.
Let x be any string in the first array and y be any string in the second array.

        Find max(abs(length(x) − length(y)))

        If a1 and/or a2 are empty return -1.

#Example:

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
*/


import java.util.Arrays;
import java.util.stream.IntStream;

/*
public class MaxDiffLength {
    public static int mxdiflg(String[] a1, String[] a2) {
        if (a1.length == 0 || a2.length == 0) return -1;
        int[] lenA = Arrays.stream(a1).mapToInt(String::length).toArray();
        int[] lenB = Arrays.stream(a2).mapToInt(String::length).toArray();
        int[] minMaxA = new int[]{IntStream.of(lenA).min().getAsInt(), IntStream.of(lenA).max().getAsInt()};
        int[] minMaxB = new int[]{IntStream.of(lenB).min().getAsInt(), IntStream.of(lenB).max().getAsInt()};
        return Math.max(minMaxA[1] - minMaxB[0], minMaxB[1] - minMaxA[0]);
    }
}*/

public class MaxDiffLength {
    public static int mxdiflg(String[] a1, String[] a2) {
        int maxDiff = -1;
        for (var x : a1)
            for (var y : a2)
                maxDiff = Math.max(maxDiff, Math.abs(x.length() - y.length()));
        return maxDiff;
    }
}
