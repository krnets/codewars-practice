/*
Principal Diagonal -- The principal diagonal in a matrix identifies those elements
of the matrix running from North-West to South-East.

Secondary Diagonal -- the secondary diagonal of amatrix identifies those elements
of the matrix running from North-East to South-West.

For example:

matrix: [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]

principal diagonal: [1, 5, 9]
secondary diagonal: [3, 5, 7]

Your task is to find which diagonal is "larger": which diagonal has a bigger sum of their elements.

        If the principal diagonal is larger, return "Principal Diagonal win!"
        If the secondary diagonal is larger, return "Secondary Diagonal win!"
        If they are equal, return "Draw!"

Note: You will always receive matrices of the same dimension.
*/

/*
import java.util.Arrays;

public class Solution {
    public static String diagonal(int[][] matrix) {
        var len = matrix.length;
        var principalDiagonal = new int[len];
        var secondaryDiagonal = new int[len];
        for (int i = 0; i < len; i++) {
            principalDiagonal[i] = matrix[i][i];
            secondaryDiagonal[i] = matrix[i][len - i - 1];
        }
        var principalDiagonalSum = Arrays.stream(principalDiagonal).sum();
        var secondaryDiagonalSum = Arrays.stream(secondaryDiagonal).sum();

        return principalDiagonalSum > secondaryDiagonalSum ? "Principal Diagonal win!" :
               principalDiagonalSum < secondaryDiagonalSum ? "Secondary Diagonal win!" : "Draw!";
    }
}*/

public class Solution {
    public static String diagonal(int[][] matrix) {
        int principalDiagonalSum = 0;
        int secondaryDiagonalSum = 0;

        for (int i = 0; i < matrix.length; i++) {
            principalDiagonalSum += matrix[i][i];
            secondaryDiagonalSum += matrix[matrix.length - i - 1][i];
        }
        return principalDiagonalSum > secondaryDiagonalSum ? "Principal Diagonal win!" :
               principalDiagonalSum < secondaryDiagonalSum ? "Secondary Diagonal win!" : "Draw!";
    }
}