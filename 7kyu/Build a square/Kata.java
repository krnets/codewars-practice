/*
I will give you an integer.
Give me back a shape that is as long and wide as the integer.
The integer will be a whole number between 0 and 50.

        Example
        n = 3, so I expect a 3x3 square back just like below as a string:

        +++
        +++
        +++
*/
/*

public class Kata {
    public static String generateShape(int n) {
        String row = "+".repeat(n);
        var result = new StringBuilder();
        for (int i = 0; i < n; i++) {
            result.append(row);
            result.append("\n");
        }
        return result.toString().trim();
    }
}*/

public class Kata {
    public static String generateShape(int n) {
        return ("+".repeat(n) + "\n").repeat(n).trim();
    }
}

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata {
    public static String generateShape(int n) {
        return IntStream.rangeClosed(1, n)
                .mapToObj(i -> "+".repeat(n))
                .collect(Collectors.joining("\n"));
    }
}
*/
