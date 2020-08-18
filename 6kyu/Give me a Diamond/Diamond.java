/*
Jamie is a programmer, and James' girlfriend.
She likes diamonds, and wants a diamond string from James.
Since James doesn't know how to make this happen, he needs your help.

Task:   You need to return a string that looks like a diamond shape when printed on the screen,
        using asterisk (*) characters. Trailing spaces should be removed, and every line
        must be terminated with a newline character (\n).

Return null if the input is an even number or negative,
as it is not possible to print a diamond of even or negative size.

        A size 3 diamond:

        *
        ***
        *

...which would appear as a string of " *\n***\n *\n"

        A size 5 diamond:

        *
        ***
        *****
        ***
        *

...that is: " *\n ***\n*****\n ***\n *\n"
*/

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Diamond {
    public static String print(int n) {
        if (n < 1 || n % 2 == 0) return null;

        return IntStream.iterate(1, i -> i < (2 * n), i -> i + 2)
                .map(i -> i > n ? 2 * n - i : i)
                .mapToObj(i -> " ".repeat((n - i) / 2) + "*".repeat(i) + "\n")
                .collect(Collectors.joining());
    }
}
*/

/*
public class Diamond {
    public static String print(int n) {
        if (n < 1 || n % 2 == 0) return null;
        var diamond = new StringBuilder();
        int midRow = n / 2 + 1;

        for (int i = midRow; i <= n * 2 - midRow; i++) {
            for (int j = 1; j <= n - Math.abs(n - i); j++) {
                if (j <= Math.abs(n - i))
                    diamond.append(" ");
                else diamond.append("*");
            }
            diamond.append("\n");
        }
        return diamond.toString();
    }
}
*/

public class Diamond {
    public static String print(int n) {
        if (n < 1 || n % 2 == 0) return null;
        var diamond = new StringBuilder();

        for (int i = 1; i <= n; i += 2) {
            diamond.append(" ".repeat((n - i) / 2))
                   .append("*".repeat(i))
                   .append("\n");
        }
        for (int i = n - 2; i >= 1; i -= 2) {
            diamond.append(" ".repeat((n - i) / 2))
                   .append("*".repeat(i))
                   .append("\n");
        }
        return diamond.toString();
    }
}
