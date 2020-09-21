import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class AckermannTest {

    private Solution soln = new Solution();

    @Test
    public void shouldWork() {
        assertEquals("3", 3, soln.Ackermann(1, 1), 0);
        assertEquals("9", 9, soln.Ackermann(2, 3), 0);
        assertEquals("13", 13, soln.Ackermann(4, 0), 0);
        assertEquals("61", 61, soln.Ackermann(3, 3), 0);
    }
}