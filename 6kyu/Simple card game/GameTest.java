import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class GameTest {

    private Game game = new Game();

    @Test
    public void testGame() {
        assertEquals(
                "small deck",
                "Steve wins 2 to 1",
                game.winner(new String[]{"A", "7", "8"}, new String[]{"K", "5", "9"})
        );

        assertEquals(
                "small deck",
                "Tie",
                game.winner(new String[]{"T"}, new String[]{"T"})
        );

        assertEquals(
                "small deck",
                "Steve wins 1 to 0",
                game.winner(new String[]{"T", "9"}, new String[]{"T", "8"})
        );

        assertEquals(
                "medium deck",
                "Josh wins 4 to 3",
                game.winner(
                        new String[]{"K", "2", "4", "5", "4", "3", "2", "K", "A", "T"},
                        new String[]{"Q", "3", "4", "6", "4", "3", "5", "A", "8", "7"}
                )
        );

        assertEquals(
                "medium deck",
                "Tie",
                game.winner(
                        new String[]{"A", "K", "2", "3", "A", "8", "5", "5", "7", "T"},
                        new String[]{"K", "A", "5", "9", "A", "3", "2", "6", "3", "T"}
                )
        );

        assertEquals(
                "large deck",
                "Steve wins 10 to 8",
                game.winner(
                        new String[]{"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A", "5", "6", "8", "T", "3", "T", "J"},
                        new String[]{"A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "2", "2", "T", "T", "9", "4", "3"}
                )
        );
    }
}