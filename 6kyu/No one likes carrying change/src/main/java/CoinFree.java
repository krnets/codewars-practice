import java.util.Collections;
import java.util.stream.IntStream;

public class CoinFree {
    public static int solve(int amount, int[] coinAmounts) {
        int[] denominations = IntStream.of(coinAmounts).boxed()
                .sorted(Collections.reverseOrder()).mapToInt(i -> i).toArray();

        int count = 0;

        for (int coin : denominations) {
            count += amount / coin;
            amount %= coin;
        }
        return count;
    }
}

