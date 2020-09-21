import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import static junit.framework.TestCase.fail;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.CoreMatchers.nullValue;
import static org.junit.Assert.assertThat;

public class BallotsCounterTest {

    @Test
    public void testGetWinner_01() {
        assertThat(BallotsCounter.getWinner(Arrays.asList("A")), is("A"));
    }

    @Test
    public void testGetWinner_02() {
        assertThat(BallotsCounter.getWinner(Arrays.asList("A", "A", "A", "B", "B", "B", "A")), is("A"));
    }

    @Test
    public void testGetWinner_03() {
        assertThat(BallotsCounter.getWinner(Arrays.asList("A", "A", "A", "B", "B", "B")), is(nullValue()));
    }

    @Test
    public void testGetWinner_04() {
        assertThat(BallotsCounter.getWinner(Arrays.asList("A", "A", "A", "B", "C", "B")), is(nullValue()));
    }

    @Test
    public void testGetWinner_05() {
        assertThat(BallotsCounter.getWinner(Arrays.asList("A", "A", "B", "B", "C")), is(nullValue()));
    }

    @Test
    public void testGetWinner_06() {
        final List<String> ballotBox = new ArrayList<>(1200000);
        String winner = null;

        for (int i = 0; i < 300000; i++) {
            ballotBox.add("Z");
        }

        for (int i = 0; i < 300000; i++) {
            ballotBox.add("XY");
        }

        for (int i = 0; i < 299999; i++) {
            ballotBox.add("U");
        }

        for (int i = 0; i < 300000; i++) {
            ballotBox.add("XY");
        }

        try {
            winner = BallotsCounter.getWinner(Collections.unmodifiableList(ballotBox));
        } catch (Throwable t) {
            fail("No exception expected" + t);
        }

        assertThat("XY should win this election with 600,000 votes against 599,999 votes", winner, is("XY"));
    }


    @Test
    public void testGetWinner_07() {
        final List<String> ballotBox = new ArrayList<>(2083);
        String winner = null;

        for (int i = 0; i < 1040; i++) {
            //"Random" names.
            ballotBox.add(String.valueOf((char) ((i % 26) + 65)));

            if (1 == i % 2) {
                //After for loop, we got 1040 votes for KL, but we got a total of 2081 votes.
                ballotBox.add("KL");
                ballotBox.add("KL");
            }
        }

        //Due to this vote, KL wins this election.
        ballotBox.add("KL");

        try {
            winner = BallotsCounter.getWinner(Collections.unmodifiableList(ballotBox));
        } catch (Throwable t) {
            fail("No exception expected");
        }

        assertThat(winner, is("KL"));
    }

    @Test
    public void testGetWinner_08() {
        final List<String> ballotBox = new ArrayList<>(2083);
        String winner = null;

        for (int i = 0; i < 1040; i++) {
            //"Random" names.
            ballotBox.add(String.valueOf((char) ((i % 26) + 65)));

            if (1 == i % 2) {
                //After for loop, we got 1040 votes for KL, but we got a total of 2081 votes => No one wins this
                //election.
                ballotBox.add("KL");
                ballotBox.add("KL");
            }
        }

        try {
            winner = BallotsCounter.getWinner(Collections.unmodifiableList(ballotBox));
        } catch (Throwable t) {
            fail("No exception expected");
        }

        assertThat(winner, is(nullValue()));
    }

    @Test
    public void testGetWinner_09() {
        final List<String> ballotBox = new ArrayList<>(1200000);
        String winner = null;

        for (int i = 0; i < 300000; i++) {
            ballotBox.add("Z");
        }

        for (int i = 0; i < 299999; i++) {
            ballotBox.add("XY");
        }

        for (int i = 0; i < 299999; i++) {
            ballotBox.add("U");
        }

        for (int i = 0; i < 300000; i++) {
            ballotBox.add("XY");
        }

        try {
            winner = BallotsCounter.getWinner(Collections.unmodifiableList(ballotBox));
        } catch (Throwable t) {
            fail("No exception expected" + t);
        }

        assertThat("No one should win this election.", winner, is(nullValue()));
    }

    @Test
    public void testGetWinner_10() {
        final List<String> ballotBox = new ArrayList<>(1200000);
        String winner = null;

        for (int i = 0; i < 600000; i++) {
            ballotBox.add("XY");
        }

        for (int i = 0; i < 300000; i++) {
            ballotBox.add("Z");
        }

        for (int i = 0; i < 299999; i++) {
            ballotBox.add("U");
        }

        try {
            winner = BallotsCounter.getWinner(Collections.unmodifiableList(ballotBox));
        } catch (Throwable t) {
            fail("No exception expected");
        }

        assertThat("XY should win this election with 600,000 votes against 599,999 votes", winner, is("XY"));
    }
}
