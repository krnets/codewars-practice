/* Write a function pattern which returns the following Pattern up to n number of rows.

        Note: Returning the pattern is not the same as Printing the pattern.

        Rules/Note:

        If n < 1 then it should return "" i.e. empty string.
        There are no whitespaces in the pattern.

        Pattern:

        (n)(n-1)(n-2)...4321
        (n)(n-1)(n-2)...432
        (n)(n-1)(n-2)...43
        (n)(n-1)(n-2)...4
        ...............
        ..............
        (n)(n-1)(n-2)
        (n)(n-1)
        (n)

        Examples:

        pattern(4):

        4321
        432
        43
        4

        pattern(11):

        1110987654321
        111098765432
        11109876543
        1110987654
        111098765
        11109876
        1110987
        111098
        11109
        1110
        11

        Hint: Use \n in string to jump to next line
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class CompleteThePattern {
    public static String pattern(int n) {
        return IntStream.rangeClosed(1, n)
                .mapToObj(i -> IntStream.rangeClosed(i, n)
                        .map(j -> n - j + i)
                        .mapToObj(Integer::toString)
                        .collect(Collectors.joining()))
                .collect(Collectors.joining("\n"));
    }
}

/*
public class CompleteThePattern {
    public static String pattern(int n) {
        String row = "", output = "";
        while (n > 0)
            output = (row += n--) + (output.isEmpty() ? "" : "\n") + output;
        return output;
    }
}
*/
/*
public class CompleteThePattern {
    public static String pattern(int n) {
        String output = "";
        var row = new StringBuilder();
        while (n > 0)
            output = row.append(n--) + (output.isEmpty() ? "" : "\n") + output;
        return output;
    }
}
*/
