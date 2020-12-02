import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

public class CatComparatorTest {

    @Test
    public void testSimpleCase() {
        Cat[] cats = new Cat[2];
        cats[0] = new Cat("Lily", 30);
        cats[1] = new Cat("Drake", 15);

        Arrays.sort(cats, new CatWeightComparator());

        assertEquals("Incorrect cat found at index 0", "Drake", cats[0].name);
        assertEquals("Incorrect cat found at index 1", "Lily", cats[1].name);
    }

    @Test
    public void compareTest() {
        var lily1 = new Cat("Lily", 30);
        var lily2 = new Cat("Lily", 12);
        var drake = new Cat("Drake", 15);
        assertEquals(8, lily1.compareTo(drake));
        assertEquals(-8, drake.compareTo(lily2));
        assertEquals(0, lily1.compareTo(lily2));
    }

    @Test
    public void testEquals() {
        var lily = new Cat("Lily", 30);
        assertEquals(lily, lily);
        assertEquals(lily, new Cat("Lily", 30));
        assertNotEquals(lily, new Cat("Lily", 12));
        assertNotEquals(lily, new Cat("Drake", 30));
        assertNotEquals(lily, new Object());
        assertNotEquals(null, lily);
    }

    @Test
    public void testHashcode() {
        assertEquals(1151229207, new Cat("Lily", 30).hashCode());
        assertEquals(-1163150508, new Cat("Drake", 15).hashCode());
    }
}
