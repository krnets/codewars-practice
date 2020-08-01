import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class RectTest {

    private Solution soln = new Solution();

    @Test
    public void shouldWorkWith4x4() {
        assertEquals("100", 100, soln.numberOfRectangles(4, 4), 0);
    }

    @Test
    public void shouldWorkWith5x5() {
        assertEquals("225", 225, soln.numberOfRectangles(5, 5), 0);
    }


}