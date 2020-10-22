import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;


public class TheClockwiseSpiralTest {

    TheClockwiseSpiral spiral = new TheClockwiseSpiral();

    @Test
    public void should_test_spiral() {
        int[][] expected = new int[][]{
                {1, 2, 3},
                {8, 9, 4},
                {7, 6, 5}};

        Assert.assertArrayEquals(expected, spiral.createSpiral(3));

    }

    @Test
    public void testEmptySpiral() {
        int[][] expected = {};

        assertArrayEquals(expected, spiral.createSpiral(0));
    }

    @Test
    public void testTrivialSpiral() {
        int[][] expected = {
                {1}
        };

        assertArrayEquals(expected, spiral.createSpiral(1));
    }

    @Test
    public void testSpiralOfSize2() {
        int[][] expected = {
                {1, 2},
                {4, 3}
        };

        assertArrayEquals(expected, spiral.createSpiral(2));
    }

    @Test
    public void testSpiralOfSize3() {
        int[][] expected = {
                {1, 2, 3},
                {8, 9, 4},
                {7, 6, 5}
        };

        assertArrayEquals(expected, spiral.createSpiral(3));
    }

    @Test
    public void testSpiralOfSize4() {
        int[][] expected = {
                {1, 2, 3, 4},
                {12, 13, 14, 5},
                {11, 16, 15, 6},
                {10, 9, 8, 7}
        };

        assertArrayEquals(expected, spiral.createSpiral(4));
    }

    @Test
    public void testSpiralOfSize5() {
        int[][] expected = {
                {1, 2, 3, 4, 5},
                {16, 17, 18, 19, 6},
                {15, 24, 25, 20, 7},
                {14, 23, 22, 21, 8},
                {13, 12, 11, 10, 9}
        };

        assertArrayEquals(expected, spiral.createSpiral(5));
    }
}