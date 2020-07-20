/*
You have to write a function pattern which creates the following pattern upto n number of rows.
If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

        ##Examples:

        pattern(4):

        1234
        234
        34
        4

        pattern(6):

        123456
        23456
        3456
        456
        56
        6

        Note: There are no blank spaces

        Hint: Use \n in string to jump to next line
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Pattern {
    public static String pattern(int n) {
        return IntStream.rangeClosed(1, n)
                .mapToObj(i -> IntStream.rangeClosed(i, n)
                        .mapToObj(Integer::toString).collect(Collectors.joining()))
                .collect(Collectors.joining("\n"));
    }
}
/*
public class Pattern {
    public static String pattern(int n) {
        var res = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                res.append(j);
            }
            res.append("\n");
        }
        return res.toString().trim();
    }
}
*/
/*
public class Pattern {
    public static String pattern(int n) {
        String row = "", output = "";
        while (n > 0)
            output = (row = n-- + row) + (output.isEmpty() ? "" : "\n") + output;
        return output;
    }
}
*/
