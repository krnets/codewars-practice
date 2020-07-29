/*
A Nice array is defined to be an array where for every value n in the array,
there is also an element n-1 or n+1 in the array.

Example:  [2,10,9,3] is Nice array because

          2=3-1
          10=9+1
          3=2+1
          9=10-1

Write a function named isNice that returns true if its array argument is a Nice array, else false.
Return false if input array has no elements.
*/

import static java.util.Arrays.*;

public class Kata {
    public static boolean isNice(Integer[] arr) {
        return arr.length > 1 && stream(arr).allMatch(el -> stream(arr).anyMatch(x -> Math.abs(el - x) == 1));
    }
}