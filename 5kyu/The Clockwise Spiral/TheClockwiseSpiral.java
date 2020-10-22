public class TheClockwiseSpiral {

    public static int[][] createSpiral(int N) {
        int[][] matrix = new int[N][N];
        int rowStart = 0;
        int colStart = 0;
        int rowEnd = N - 1;
        int colEnd = N - 1;

        int inc = 1;
        int nSquared = N * N;

        while (inc <= nSquared) {

            for (int i = colStart; i <= colEnd; i++) {
                matrix[rowStart][i] = inc++;
            }
            rowStart++;

            for (int i = rowStart; i <= rowEnd; i++) {
                matrix[i][colEnd] = inc++;
            }
            colEnd--;

            for (int i = colEnd; i >= colStart; i--) {
                matrix[rowEnd][i] = inc++;
            }
            rowEnd--;

            for (int i = rowEnd; i >= rowStart; i--) {
                matrix[i][colStart] = inc++;
            }
            colStart++;
        }

        return matrix;

    }
}