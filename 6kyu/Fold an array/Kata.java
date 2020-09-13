/*
write a method that folds a given array of integers by the middle x-times.

        An example says more than thousand words:

        Fold 1-times:
        [1,2,3,4,5] -> [6,6,3]

A little visualization (NOT for the algorithm but for the idea of folding):

        Step 1         Step 2        Step 3       Step 4       Step5
        5/           5|         5\
        4/            4|          4\
        1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
        ----*----      ----*          ----*        ----*        ----*


        Fold 2-times:
        [1,2,3,4,5] -> [9,6]

As you see, if the count of numbers is odd, the middle number will stay.
Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

The array will always contain numbers and will never be null.
The parameter runs will always be a positive integer greater than 0
and says how many runs of folding your method has to do.

If an array with one element is folded, it stays as the same array.

The input array should not be modified!
*/


import java.util.Arrays;

/*
public class Kata {
    public static int[] foldArray(int[] array, int runs) {
        int roundedHalf = (int) Math.round(array.length / 2.0);
        int[] folded = Arrays.copyOfRange(array, 0, roundedHalf);

        for (int i = 0; i < array.length / 2; i++)
            folded[i] = array[i] + array[array.length - i - 1];

        return runs > 1 ? foldArray(folded, --runs) : folded;
    }
}
*/

/*
public class Kata {
    public static int[] foldArray(int[] array, int runs) {
        int[] folded = Arrays.copyOfRange(array, 0, (int) Math.ceil(array.length / 2.0));

        for (int i = 0; i < array.length / 2; i++) {
            folded[i] += array[array.length - i - 1];
        }
        return runs > 1 ? foldArray(folded, --runs) : folded;
    }
}
*/

/*
public class Kata {
    public static int[] foldArray(int[] array, int runs) {
        int[] folded = Arrays.copyOfRange(array, 0, (array.length + 1) / 2);

        for (int i = 0; i < array.length / 2; i++) {
            folded[i] += array[array.length - i - 1];
        }
        return runs > 1 ? foldArray(folded, --runs) : folded;
    }
}
*/

public class Kata {
    public static int[] foldArray(int[] array, int runs) {
        int[] folded = Arrays.copyOf(array, array.length);
        int length = array.length;

        for (int i = 0; i < runs; i++) {
            for (int j = 0; j < (length / 2); j++) {
                folded[j] += folded[length - 1 - j];
            }
            length = (length + 1) / 2;
        }
        return Arrays.copyOfRange(folded, 0, length);
    }
}

/*
public class Kata {
    public static int[] foldArray(int[] array, int runs) {
        int[] folded = Arrays.copyOf(array, array.length);
        int length = array.length;

        while (--runs >= 0) {
            for (int j = 0; j < length / 2; j++)
                folded[j] += folded[length - 1 - j];

            length = (length + 1) / 2;
        }
        return Arrays.copyOfRange(folded, 0, length);
    }
}
*/
