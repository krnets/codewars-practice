import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class RotationTest {
    @Test
    public void test() {
        assertEquals(1, CalculateRotation.shiftedDiff("coffee", "ecoffe"));
        assertEquals(2, CalculateRotation.shiftedDiff("coffee", "eecoff"));
        assertEquals(3, CalculateRotation.shiftedDiff("coffee", "feecof"));
        assertEquals(4, CalculateRotation.shiftedDiff("eecoff", "coffee"));
        assertEquals(-1, CalculateRotation.shiftedDiff("moose", "Moose"));
        assertEquals(2, CalculateRotation.shiftedDiff("isn't", "'tisn"));
        assertEquals(0, CalculateRotation.shiftedDiff("Esham", "Esham"));
        assertEquals(-1, CalculateRotation.shiftedDiff("dog", "god"));
    }
}