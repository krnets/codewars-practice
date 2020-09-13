/*
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing.


Write a method, that return the length of the missing array.

Example:
        [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

        If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.
*/

import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.IntStream;

public class Kata {
    public static int getLengthOfMissingArray(Object[][] arrayOfArrays) {

        if (arrayOfArrays == null || arrayOfArrays.length == 0 || Arrays.stream(arrayOfArrays).anyMatch(a -> a == null || a.length == 0)) {
            return 0;
        }

        var arrayOfLengths = Arrays.stream(arrayOfArrays)
                .mapToInt(array -> array.length)
                .sorted()
                .toArray();

        var sourceSet = new HashSet<Integer>();
        var targetSet = new HashSet<Integer>();

        for (int i : arrayOfLengths)
            sourceSet.add(i);

        var min = arrayOfLengths[0];
        var max = arrayOfLengths[arrayOfLengths.length - 1];

        IntStream.rangeClosed(min, max)
                .forEach(targetSet::add);

        targetSet.removeAll(sourceSet);

        return targetSet.stream().mapToInt(i -> i).findFirst().orElse(0);
    }
}