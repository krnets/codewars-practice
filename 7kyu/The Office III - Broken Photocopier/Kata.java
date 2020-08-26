/*
The bloody photocopier is broken...
Just as you were sneaking around the office to print off your favourite binary code!

Instead of copying the original, it reverses it:
'1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string.
*/

import java.util.Arrays;
import java.util.stream.Collectors;

/*
public class Kata {
    public static String broken(final String x) {
        return x.chars()
                .mapToObj(c -> (char) c == '1' ? "0" : "1")
                .collect(Collectors.joining());
    }
}
*/

/*
public class Kata {
    public static String broken(final String x) {
        return Arrays.stream(x.split(""))
                .map(c -> c.equals("1") ? "0" : "1")
                .collect(Collectors.joining());
    }
}
*/

public class Kata {
    public static String broken(final String x) {
        var sb = new StringBuilder();

        for (var c : x.split("")) {
            sb.append(c.equals("1") ? "0" : "1");
        }
        return sb.toString();
    }
}
/*
public class Kata {
    public static String broken(final String x) {
        var sb = new StringBuilder();

        for (var c : x.toCharArray()) {
            sb.append(c == '1' ? '0' : '1');
        }
        return sb.toString();
    }
}
*/
