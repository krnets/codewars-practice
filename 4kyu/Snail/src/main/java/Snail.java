public class Snail {

    public static int[] snail(int[][] array) {
        int length = array[0].length;
        int n = 0;
        int nSquared = length * length;
        int[] result = new int[nSquared];

        int rowStart = 0;
        int colStart = 0;
        int rowEnd = length - 1;
        int colEnd = length - 1;

        while (n < nSquared) {

            for (int i = colStart; i <= colEnd; i++) {
                result[n++] = array[rowStart][i];
                if (n == nSquared) {
                    break;
                }
            }
            rowStart++;

            for (int i = rowStart; i <= rowEnd; i++) {
                result[n++] = array[i][colEnd];
                if (n == nSquared) {
                    break;
                }
            }
            colEnd--;

            for (int i = colEnd; i >= colStart; i--) {
                result[n++] = array[rowEnd][i];
                if (n == nSquared) {
                    break;
                }
            }
            rowEnd--;

            for (int i = rowEnd; i >= rowStart; i--) {
                result[n++] = array[i][colStart];
                if (n == nSquared) {
                    break;
                }
            }
            colStart++;
        }
        return result;
    }
}