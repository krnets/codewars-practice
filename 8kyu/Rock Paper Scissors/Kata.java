/*
Let's play! You have to return which player won! In case of a draw return Draw!.

        Examples:

        rps('scissors','paper') // Player 1 won!
        rps('scissors','rock') // Player 2 won!
        rps('paper','paper') // Draw!
*/
public class Kata {
    public static String rps(String p1, String p2) {
        return p1.equals(p2) ? "Draw!" : "Player " + ("scissorspaper paperrock rockscissors".contains(p1 + p2) ? 1 : 2) + " won!";
    }
}
