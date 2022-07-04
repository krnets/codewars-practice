import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SolutionTest {

    @Test
    public void test_BasicTest1() {
        assertEquals("-6,-3-1,3-5,7-11,14,15,17-20", Solution
                .rangeExtraction(
                        new int[]{-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9,
                                10, 11, 14, 15, 17, 18, 19, 20}));
    }

    @Test
    public void test_BasicTest2() {
        assertEquals("-3--1,2,10,15,16,18-20", Solution
                .rangeExtraction(
                        new int[]{-3, -2, -1, 2, 10, 15, 16, 18, 19, 20}));
    }

    @Test
    public void test_BasicTest3() {
        assertEquals("2,10,15,16,18-24", Solution
                .rangeExtraction(
                        new int[]{2, 10, 15, 16, 18, 19, 20, 21, 22, 23, 24}));
    }
}