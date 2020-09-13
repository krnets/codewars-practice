import static org.junit.Assert.*;

import org.junit.*;

public class Examples {

    @Test
    public void example() {
        final String expected =
                "6|██ 5%\n" +
                        "5|\n" +
                        "4|███████ 15%\n" +
                        "3|███████████████████████████████████ 70%\n" +
                        "2|█ 3%\n" +
                        "1|███ 7%\n";
        assertEquals(expected, Dinglemouse.histogram(new int[]{7, 3, 70, 15, 0, 5}));
    }

}
