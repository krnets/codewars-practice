public class Spiralizor {

    public static int[][] spiralize(int size) {
        int[][] matrix = new int[size][size];
        int colStart = 0, rowStart = 0;
        int colEnd = size - 1, rowEnd = size - 1;

        while (rowStart <= rowEnd) {
            for (int j = colStart; j <= colEnd; j++) matrix[rowStart][j] = 1;
            for (int i = rowStart; i <= rowEnd; i++) matrix[i][colEnd] = 1;

            if (colStart != 0) colStart += 1;
            if (rowEnd - 1 == rowStart) break;

            for (int j = colEnd - 1; j >= colStart; j--) matrix[rowEnd][j] = 1;
            for (int i = rowEnd - 1; i > rowStart + 1; i--) matrix[i][colStart] = 1;

            rowStart += 2;
            colEnd -= 2;
            rowEnd -= 2;
            colStart += 1;
        }
        return matrix;
    }
}


/*
public class Spiralizor {

    public static int[][] spiralize(int size) {
        int[][] grid = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {

                if ((j + 1 == i) && (i * 2 < size)) {
                    grid[i][j] = j % 2;
                } else {
                    grid[i][j] = 1 - (Math.min(size - Math.max(i, j) - 1, Math.min(i, j)) % 2);
                }
            }
        }
        if (size % 2 == 0) {
            grid[size / 2][size / 2 - 1] = 0;
        }
        return grid;
    }
}
*/
