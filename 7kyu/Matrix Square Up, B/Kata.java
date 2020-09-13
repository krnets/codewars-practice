/*
Given an integer b greater than 0, create and return a b X b matrix with the following pattern:

        [x,1]
        matrixSquareUp(2) => [2,1]

        [x,x,1]
        [x,2,1]
        matrixSquareUp(3) => [3,2,1]

        [x,x,x,1]
        [x,x,2,1]
        [x,3,2,1]
        matrixSquareUp(4) => [4,3,2,1]

        Those are lowercase 'x'.

        50 > b > 0
*/

/*
public class Kata {
    public static String[][] matrixSquareUp(int b) {
        var matrix = new String[b][b];

        for (int i = 0; i < b; i++) {
            for (int j = b - 1; j > -1; j--) {
                if (i + j + 1 < b)
                    matrix[i][j] = "x";
                else
                    matrix[i][j] = String.valueOf(b - j);
            }
        }
        return matrix;
    }
}*/

public class Kata {
    public static String[][] matrixSquareUp(int b) {
        var matrix = new String[b][b];

        for (int i = 0; i < b; i++) {
            for (int j = 0; j < b; j++) {
                if (i < (b - j - 1))
                     matrix[i][j] = "x";
                else matrix[i][j] = String.valueOf(b - j);
            }
        }
        return matrix;
    }
}
