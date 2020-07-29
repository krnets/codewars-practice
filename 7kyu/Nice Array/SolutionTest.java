import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void sampleTest() {
        assertEquals(Kata.isNice(new Integer[]{2, 10, 9, 3}), true);
        assertEquals(Kata.isNice(new Integer[]{1, 2, 3, 4, 5}), true);
        assertEquals(Kata.isNice(new Integer[]{5, 4, 3, 2, 1}), true);
        assertEquals(Kata.isNice(new Integer[]{1, 3, 5, 2}), false);
        assertEquals(Kata.isNice(new Integer[]{10, 10, 2, 2, 3}), false);
        assertEquals(Kata.isNice(new Integer[]{}), false);
        assertEquals(Kata.isNice(new Integer[]{1}), false);
    }
}