import java.util.Arrays;
import java.util.stream.Collectors;

/*
public class ThinkingAndTesting {
    public static String testSomethingCapitalized(String s) {
        return Arrays.stream(s.split(" "))
                .map(x -> {
                    int len = x.length() - 1;
                    return len < 1 ? x.toUpperCase() : x.substring(0, len) + x.substring(len).toUpperCase();
                })
                .collect(Collectors.joining(" "));
    }
}
*/
/*
public class ThinkingAndTesting {
    public static String testSomethingCapitalized(String s) {
        return s.isEmpty() ? s : Arrays.stream(s.split(" "))
                .map(w -> w.substring(0, w.length() - 1) + w.substring(w.length() - 1).toUpperCase())
                .collect(Collectors.joining(" "));
    }
}*/

public class ThinkingAndTesting {
    public static String testSomethingCapitalized(String s) {
        return Arrays.stream(s.split(" "))
                .map(x -> x.length() < 1 ? x : x.substring(0, x.length() - 1) + x.substring(x.length() - 1).toUpperCase())
                .collect(Collectors.joining(" "));
    }
}
