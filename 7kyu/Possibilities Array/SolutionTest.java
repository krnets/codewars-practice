import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void simpleTest1() {
        assertEquals(true, Solution.isAllPossibilities(new int[]{0, 1, 2, 3}));
    }

    @Test
    public void simpleTest2() {
        assertEquals(false, Solution.isAllPossibilities(new int[]{1, 2, 3, 4}));
    }

    @Test
    public void simpleTest3() {
        assertEquals(false, Solution.isAllPossibilities(new int[]{6, 0, 4}));
    }
}