import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

public class ExampleTests {

    @Test
    public void example() {
        final double[] expected = {-1 / 2d, -2};
        final double[] actual = Dinglemouse.cogRpm(new int[]{100, 50, 25}, 1);
        assertArrayEquals(expected, actual, 0.001);
    }

}