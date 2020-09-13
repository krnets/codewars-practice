/*
A non-empty array a of length n is called an array of all possibilities
if it contains all numbers between [0,a.length-1].

Write a method named isAllPossibilities that accepts an integer array
and returns true if the array is an array of all possibilities,else false.

Example:

        a = [1,2,0,3]
        a.length-1 == 3
        a includes [0,3] -> hence the function should return true
*/


/*
import java.util.Arrays;
import java.util.stream.IntStream;

public class Solution {
    public static boolean isAllPossibilities(int[] arg) {
        Arrays.sort(arg);

        return arg.length > 0 && IntStream.range(0, arg.length)
                .allMatch(i -> arg[i] == i);
    }
}
*/

import java.util.Arrays;

public class Solution {
    public static boolean isAllPossibilities(int[] arg) {
        var stats = Arrays.stream(arg).summaryStatistics();

        return (stats.getMin() == 0) && (stats.getMax() == (arg.length - 1));
    }
}
