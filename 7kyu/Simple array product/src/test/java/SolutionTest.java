import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void basicTest1() {
        assertEquals(8, Solution.solve(new int[][]{{1, 2}, {3, 4}}));
    }

    @Test
    public void basicTest2() {
        assertEquals(45, Solution.solve(new int[][]{{10, -15}, {-1, -3}}));
    }

    @Test
    public void basicTest3() {
        assertEquals(12, Solution.solve(new int[][]{{-1, 2, -3, 4}, {1, -2, 3, -4}}));
    }

    @Test
    public void basicTest4() {
        assertEquals(17600, Solution.solve(new int[][]{{-11, -6}, {-20, -20}, {18, -4}, {-20, 1}}));
    }

    @Test
    public void basicTest5() {
        assertEquals(3584, Solution.solve(new int[][]{{14, 2}, {0, -16}, {-12, -16}}));
    }

    @Test
    public void basicTest6() {
        assertEquals(12, Solution.solve(new int[][]{{-3, -4}, {1, 2, -3}}));
    }

    @Test
    public void basicTest7() {
        assertEquals(-40, Solution.solve(new int[][]{{-2, -15, -12, -8, -16}, {-4, -15, -7}, {-10, -5}}));
    }
}