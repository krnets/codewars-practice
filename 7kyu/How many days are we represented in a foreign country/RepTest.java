import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class RepTest {
    @Test
    public void testRepresentation() {
        Representation rep = new Representation();
        assertEquals(17, rep.daysRepresented(new int[][]{{10, 15}, {25, 35}}));
        assertEquals(24, rep.daysRepresented(new int[][]{{2, 8}, {220, 229}, {10, 16}}));
//        assertEquals(1, rep.daysRepresented(new int[][]{{365, 1}, {0, 0}}));
    }
}