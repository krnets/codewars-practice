import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void test_BasicTest1() {
        assertEquals(2, Solution.solve(")()("));
    }

    @Test
    public void test_BasicTest2() {
        assertEquals(1, Solution.solve("((()"));
    }

    @Test
    public void test_BasicTest3() {
        assertEquals(-1, Solution.solve("((("));
    }

    @Test
    public void test_BasicTest4() {
        assertEquals(3, Solution.solve("())((("));
    }

    @Test
    public void test_BasicTest5() {
        assertEquals(4, Solution.solve("())()))))()()("));
    }
}