import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

public class PascalDiagonalsTest {

    @Test
    public void generateDiagonalTest1() {
        long[] arr = {1, 1, 1, 1, 1, 1};
        assertArrayEquals(arr, PascalDiagonals.generateDiagonal(0, 6));
    }

    @Test
    public void generateDiagonalTest2() {
        long[] arr = {1, 2, 3, 4, 5, 6};
        assertArrayEquals(arr, PascalDiagonals.generateDiagonal(1, 6));
    }

    @Test
    public void generateDiagonalTest3() {
        long[] arr = {1, 3, 6, 10};
        assertArrayEquals(arr, PascalDiagonals.generateDiagonal(2, 4));
    }

    @Test
    public void generateDiagonalTest4() {
        long[] arr = {};
        assertArrayEquals(arr, PascalDiagonals.generateDiagonal(2, 0));
    }

}