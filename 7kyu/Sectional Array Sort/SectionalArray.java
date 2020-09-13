/*
In this kata you are given an array to sort but you're expected to start sorting
from a specific position of the array (in ascending order) and optionally
you're given the number of items to sort.

Examples:

        SectionalArray.sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2) //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
        SectionalArray.sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5) // => [9, 7, 1, 2, 3, 4, 5, 8, 6]

Documentation:

        SectionalArray.sort(array, start, length);

        array - array to sort
        start - position to begin sorting
        length - number of items to sort (optional)

if the length argument is not passed or is zero,
you sort all items to the right of the start postiton in the array
*/

import java.util.Arrays;

/*
public class SectionalArray {
    static int[] sort(final int[] array, final int start, final int... length) {
        int toIndex;

        if ((length.length > 0) && ((start + length[0]) < array.length))
            toIndex = start + length[0];
        else
            toIndex = array.length;

        Arrays.sort(array, start, toIndex);

        return array;
    }
}
*/

public class SectionalArray {
    static int[] sort(final int[] array, final int start, final int... length) {
        int toIndex = length.length > 0 ?
                Math.min(start + length[0], array.length) :
                array.length;

        Arrays.sort(array, start, toIndex);
        return array;
    }
}
