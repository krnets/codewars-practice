/*
Write a function which takes an array data of numbers and returns the largest difference
in indexes j - i such that data[i] <= data[j]

The largestDifference takes an array of numbers.
That array is not sorted.
Do not sort it or change the order of the elements in any way, or their values.

Consider all of the pairs of numbers in the array where the first one is less than
or equal to the second one.

From these, find a pair where their positions in the array are farthest apart.

Return the difference between the indexes of the two array elements in this pair.

Example:

        LargestDifference.largestDifference(new int[]{1,2,3});
        //returns 2, because here j = 2 and i = 0 and 2 - 0 = 2
*/


/*
public class LargestDifference {
    public static int largestDifference(int[] data) {
        int diff = 0;
        int len = data.length - 1;

        for (int i = 0; len - i > diff; i++) {
            for (int j = len; j - i > diff; j--) {
                if (data[i] <= data[j])
                    diff = j - i;
            }
        }
        return diff;
    }
}
*/

public class LargestDifference {
    public static int largestDifference(int[] data) {
        int indexDifference = 0;
        int len = data.length;

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (data[i] <= data[j] && j - i > indexDifference)
                    indexDifference = j - i;
            }
        }
        return indexDifference;
    }
}
