/*
Complete the method which accepts an array of integers, and returns one of the following:

        "yes, ascending" - if the numbers in the array are sorted in an ascending order
        "yes, descending" - if the numbers in the array are sorted in a descending order
        "no" - otherwise

        You can assume the array will always be valid, and there will always be one correct answer.
*/

/*
public class Solution {
    public static String isSortedAndHow(int[] array) {
        boolean ascending = false;
        boolean descending = false;
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] < array[i + 1])
                ascending = true;
            if (array[i] > array[i + 1])
                descending = true;
        }
        return ascending && descending ? "no" : ascending ? "yes, ascending" : descending ? "yes, descending" : "";
    }
}*/

import static java.util.stream.IntStream.range;

public class Solution {
    public static String isSortedAndHow(int[] array) {
        return range(1, array.length).allMatch(i -> array[i - 1] <= array[i]) ? "yes, ascending" :
               range(1, array.length).allMatch(i -> array[i - 1] >= array[i]) ? "yes, descending" : "no";
    }
}
