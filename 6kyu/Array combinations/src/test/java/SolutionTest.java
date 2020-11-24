import org.junit.Test;

import java.util.List;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void test_BasicTest1() {
        assertEquals(4,
                Kata.solve(List.of(List.of(1, 2),
                        List.of(4),
                        List.of(5, 6))));
    }

    @Test
    public void test_BasicTests2() {
        assertEquals(4,
                Kata.solve(List.of(List.of(1, 2),
                        List.of(4, 4),
                        List.of(5, 6, 6))));
    }

    @Test
    public void test_BasicTests3() {
        assertEquals(8,
                Kata.solve(List.of(List.of(1, 2),
                        List.of(3, 4),
                        List.of(5, 6))));
    }

    @Test
    public void test_BasicTests4() {
        assertEquals(72,
                Kata.solve(List.of(List.of(1, 2, 3),
                        List.of(3, 4, 6, 6, 7),
                        List.of(8, 9, 10, 12, 5, 6))));
    }
}