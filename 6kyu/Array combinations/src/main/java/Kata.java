import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Kata {
    public static int solve(final List<List<Integer>> data) {
        return data.stream()
                .map(HashSet::new)
                .mapToInt(Set::size)
                .reduce(1, (a, b) -> a * b);
    }
}