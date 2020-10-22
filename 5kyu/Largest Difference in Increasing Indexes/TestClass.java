import junit.framework.TestCase;

public class TestClass extends TestCase {
    public void test1() {
        assertEquals(4, LargestDifference.largestDifference(new int[]{9, 4, 1, 10, 3, 4, 0, -1, -2}));
    }

    public void test2() {
        assertEquals(0, LargestDifference.largestDifference(new int[]{3, 2, 1}));
    }

    public void test3() {
        assertEquals(2, LargestDifference.largestDifference(new int[]{1, 2, 3}));
    }

    public void test4() {
        assertEquals(2, LargestDifference.largestDifference(new int[]{9, 4, 1, 2, 3, 0, -1, -2}));
    }

    public void test5() {
        assertEquals(4, LargestDifference.largestDifference(new int[]{9, 4, 1, 2, 3, 4, 0, -1, -2}));
    }

    public void test6() {
        assertEquals(10, LargestDifference
                .largestDifference(new int[]{78, 88, 64, 94, 17, 91, 57, 69, 38, 62, 13, 17, 35, 15, 20}));
    }

    public void test7() {
        assertEquals(4, LargestDifference.largestDifference(new int[]{4, 3, 3, 1, 5, 2}));
    }
}