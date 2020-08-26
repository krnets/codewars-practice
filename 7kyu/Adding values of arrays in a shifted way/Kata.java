/*
#The method should add the values of the arrays to one new array.

The arrays in the array will all have the same size and this size will always be greater than 0.
The shifting value is always a value from 0 up to the size of the arrays.
There are always arrays in the array, so you do not need to check for null or empty.

#1. Example:

        [[1,2,3,4,5,6], [7,7,7,7,7,-7]], 0

        1,2,3,4,5,6
        7,7,7,7,7,-7

        --> [8,9,10,11,12,-1]

#2. Example

        [[1,2,3,4,5,6], [7,7,7,7,7,7]], 3

        1,2,3,4,5,6
              7,7,7,7,7,7

        --> [1,2,3,11,12,13,7,7,7]

#3. Example

        [[1,2,3,4,5,6], [7,7,7,-7,7,7], [1,1,1,1,1,1]], 3


        1,2,3,4,5,6
              7,7,7,-7,7,7
                     1,1,1,1,1,1

        --> [1,2,3,11,12,13,-6,8,8,1,1,1]
*/


/*
public class Kata {
    public static int[] addingShifted(int[][] arrayOfArrays, int shift) {
        var result = new int[shift * (arrayOfArrays.length - 1) + arrayOfArrays[0].length];

        for (int i = 0; i < arrayOfArrays.length; i++)
            for (int j = 0; j < arrayOfArrays[i].length; j++)
                result[i * shift + j] += arrayOfArrays[i][j];

        return result;
    }
}*/

public class Kata {
    public static int[] addingShifted(int[][] arrayOfArrays, int shift) {
        var columnSum = new int[(arrayOfArrays.length - 1) * shift + arrayOfArrays[0].length];

        for (int i = 0; i < arrayOfArrays.length; i++)
            for (int j = 0; j < arrayOfArrays[i].length; j++)
                columnSum[i * shift + j] += arrayOfArrays[i][j];

        return columnSum;
    }
}
