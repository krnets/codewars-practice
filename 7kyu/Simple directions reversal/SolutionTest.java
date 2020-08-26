import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void basicTests() {
        assertArrayEquals(new String[]{"Begin on Road D", "Right on Road C", "Left on Road B", "Left on Road A"}, Solution
                .solve(new String[]{"Begin on Road A", "Right on Road B", "Right on Road C", "Left on Road D"}));

        assertArrayEquals(new String[]{"Begin on 9th Dr", "Right on First Road", "Left on 3rd Blvd"}, Solution
                .solve(new String[]{"Begin on 3rd Blvd", "Right on First Road", "Left on 9th Dr"}));

        assertArrayEquals(new String[]{"Begin on Road A"}, Solution.solve(new String[]{"Begin on Road A"}));
    }
}