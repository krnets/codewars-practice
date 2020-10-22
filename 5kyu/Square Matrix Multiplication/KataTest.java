import java.util.Random;
import java.util.function.IntSupplier;

import org.junit.Assert;
import org.junit.Test;

public class KataTest {

    private int[][] solution(int[][] a, int[][] b) {

        int n = a.length;
        int[][] c = new int[n][];
        for (int i = 0; i < n; i++) {
            c[i] = new int[n];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return c;
    }

    @Test
    public void ckTest() {

        int[][] a = {
                {1, 2},
                {3, 4}};

        int[][] b = {
                {1, 2},
                {3, 4}};

        int[][] expected = {
                {7, 10},
                {15, 22}};

        int[][] actual = Kata.matrixMultiplication(a, b);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void exampleTest() {

        int[][] a = {
                {1, 2},
                {3, 2}
        };

        int[][] b = {
                {3, 2},
                {1, 1}
        };

        int[][] expected = {
                {5, 4},
                {11, 8}
        };

        int[][] actual = Kata.matrixMultiplication(a, b);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void basicTest() {

        {
            int[][] a = {
                    {9, 7},
                    {0, 1}
            };

            int[][] b = {
                    {1, 1},
                    {4, 12}
            };

            int[][] expected = {
                    {37, 93},
                    {4, 12}
            };

            int[][] actual = Kata.matrixMultiplication(a, b);
            Assert.assertArrayEquals(expected, actual);
        }

        {

            int[][] a = {
                    {1, 2, 3},
                    {3, 2, 1},
                    {2, 1, 3}};

            int[][] b = {
                    {4, 5, 6},
                    {6, 5, 4},
                    {4, 6, 5}};

            int[][] expected = {
                    {28, 33, 29},
                    {28, 31, 31},
                    {26, 33, 31}};

            int[][] actual = Kata.matrixMultiplication(a, b);
            Assert.assertArrayEquals(expected, actual);
        }
    }

    private static final Random rnd = new Random();
    private static final IntSupplier r_size = () -> rnd.nextInt(9) + 2;
    private static final IntSupplier r_elem = () -> rnd.nextInt(21) - 10;

    @Test
    public void randomTestSmallMatrix() {

        for (int test = 0; test < 100; test++) {
            int n = r_size.getAsInt();
            runTest(n);
        }
    }

    @Test
    public void randomTestLargeMatrix() {

        for (int test = 0; test < 100; test++) {
            int n = 100;
            runTest(n);
        }
    }

    private void runTest(int size) {

        int[][] a = new int[size][];
        int[][] b = new int[size][];

        for (int j = 0; j < size; j++) {

            a[j] = new int[size];
            b[j] = new int[size];

            for (int k = 0; k < size; k++) {
                a[j][k] = r_elem.getAsInt();
                b[j][k] = r_elem.getAsInt();
            }
        }

        int[][] expected = solution(a, b);
        int[][] actual = Kata.matrixMultiplication(a, b);
        Assert.assertArrayEquals(expected, actual);
    }
}
