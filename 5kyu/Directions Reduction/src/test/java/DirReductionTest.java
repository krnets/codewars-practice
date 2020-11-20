import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

public class DirReductionTest {

    @Test
    public void testSimpleDirReduc1() {
        assertArrayEquals("\"NORTH\", \"SOUTH\", \"SOUTH\", \"EAST\", \"WEST\", \"NORTH\", \"WEST\"",

                new String[]{"WEST"},
                DirReduction.dirReduc(
                        new String[]{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}));
    }

    @Test
    public void testSimpleDirReduc2() {
        assertArrayEquals("\"NORTH\",\"SOUTH\",\"SOUTH\",\"EAST\",\"WEST\",\"NORTH\"",

                new String[]{},
                DirReduction.dirReduc(
                        new String[]{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"}));
    }

    @Test
    public void testSimpleDirReduc3() {
        assertArrayEquals("\"NORTH\",\"SOUTH\",\"SOUTH\",\"EAST\",\"WEST\",\"NORTH\",\"NORTH\"",

                new String[]{"NORTH"},
                DirReduction.dirReduc(
                        new String[]{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"}));
    }

    @Test
    public void testSimpleDirReduc4() {
        assertArrayEquals(
                "\"EAST\", \"EAST\", \"WEST\", \"NORTH\", \"WEST\", \"EAST\", \"EAST\", \"SOUTH\", \"NORTH\", \"WEST\"",

                new String[]{"EAST", "NORTH"},
                DirReduction.dirReduc(new String[]{
                        "EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"}));
    }

    @Test
    public void testSimpleDirReduc5() {
        assertArrayEquals(
                "\"NORTH\", \"EAST\", \"NORTH\", \"EAST\", \"WEST\", \"WEST\", \"EAST\", \"EAST\", \"WEST\", \"SOUTH\"",

                new String[]{"NORTH", "EAST"},
                DirReduction.dirReduc(new String[]{
                        "NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"}));
    }

    @Test
    public void testSimpleDirReduc6() {
        assertArrayEquals("\"NORTH\", \"WEST\", \"SOUTH\", \"EAST\"",

                new String[]{"NORTH", "WEST", "SOUTH", "EAST"},
                DirReduction.dirReduc(new String[]{
                        "NORTH", "WEST", "SOUTH", "EAST"}));
    }

}
