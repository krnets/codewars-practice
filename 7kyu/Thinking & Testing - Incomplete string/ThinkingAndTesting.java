import static java.lang.Character.toChars;
import static java.util.stream.Collectors.joining;
import static java.util.stream.IntStream.range;

public class ThinkingAndTesting {
    static String testIncompleteString(String s) {
        var res = range(0, s.length() / 2)
                .mapToObj(i -> toChars((s.charAt(2 * i) + s.charAt(2 * i + 1)) / 2)[0] + "")
                .collect(joining());

        return s.length() % 2 == 0 ? res : res + s.charAt(s.length() - 1);
    }
}