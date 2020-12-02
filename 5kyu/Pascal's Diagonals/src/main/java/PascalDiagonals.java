import java.util.stream.IntStream;

public class PascalDiagonals {

    public static long[] generateDiagonal(int n, int l) {
        long[][] triangle = new long[n + l][];

        for (int i = 0; i < (n + l); i++) {
            triangle[i] = new long[i + 1];
            triangle[i][0] = 1;
            triangle[i][i] = 1;

            for (int j = 1; j < i; j++) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
        return IntStream.range(0, l).mapToLong(i -> triangle[n + i][n]).toArray();
    }
}
