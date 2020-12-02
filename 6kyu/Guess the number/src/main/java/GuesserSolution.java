/*
public class GuesserSolution extends Guesser {
    public int getNumber() {
        int low = 1, high = 1000, mid;

        while (low <= high) {
            mid = (low + high) / 2;

            switch (guess(mid)) {
                case "Too low!": low = mid; break;
                case "Too high!": high = mid; break;
                default: return mid;
            }
        }
        return -1;
    }
}
*/

public class GuesserSolution extends Guesser {
    public int getNumber() {
        int low = 1, high = 1000, mid;

        while (true) {
            mid = (low + high) / 2;

            switch (guess(mid)) {
                case "Too low!": low = mid; break;
                case "Too high!": high = mid; break;
                case "Correct!": return mid;
            }
        }
    }
}
