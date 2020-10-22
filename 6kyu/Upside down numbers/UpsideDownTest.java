import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class UpsideDownTest {
    UpsideDown sol = new UpsideDown();

    @Test
    public void basicTests() {
//        assertEquals(3, sol.solve(0, 10));
//        assertEquals(4, sol.solve(10, 100));
//        assertEquals(12, sol.solve(100, 1000));
//        assertEquals(20, sol.solve(1000, 10000));
        assertEquals(6, sol.solve(10000, 15000));
        assertEquals(9, sol.solve(15000, 20000));
        assertEquals(15, sol.solve(60000, 70000));
        assertEquals(55, sol.solve(60000, 130000));
    }
}