/*
Background

A 6-sided die is rolled a number of times and the results are plotted as a character-based histogram.

        Example:

        6|##### 5
        5|
        4|# 1
        3|########## 10
        2|### 3
        1|####### 7

Task
        You will be passed the dice value frequencies, and your task is to write the code to return a string
        representing a histogram, so that when it is printed it has the same format as the example.

Notes
        There are no trailing spaces on the lines
        All lines (including the last) end with a newline \n
        A count is displayed beside each bar except where the count is 0
        The number of rolls may vary but there are never more than 100
*/

/*
public class Dinglemouse {
    public static String histogram(final int results[]) {
        var output = new StringBuilder();
        for (int i = results.length; i > 0; i--) {
            output.append(i + "|" + "#".repeat(results[i - 1]) +
                    (results[i - 1] > 0 ? " " + results[i - 1] : "") + "\n");
        }
        return output.toString();
    }
}
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Dinglemouse {
    public static String histogram(final int results[]) {
        return IntStream.range(0, results.length)
                .map(i -> results.length - i)
                .mapToObj(i -> i + "|" + "#".repeat(results[i - 1]) + (results[i - 1] > 0 ? " " + results[i - 1] : ""))
                .collect(Collectors.joining("\n")) + "\n";
    }
}

/*
public class Dinglemouse {
    public static String histogram(final int results[]) {
        return IntStream.range(0, results.length).map(i -> results.length - i)
                .mapToObj(i -> String.format("%d|%s%s\n", i, "#".repeat(results[i - 1]),
                        (results[i - 1] > 0 ? " " + results[i - 1] : "")))
                .collect(Collectors.joining());
    }
}
*/

/*
public class Dinglemouse {
    public static String histogram(final int results[]) {
        return IntStream.iterate(results.length - 1, i -> i - 1).limit(results.length)
                .mapToObj(i -> format("%d|%s%s\n", (i + 1), "#".repeat(results[i]), (results[i] > 0 ? " " + results[i] : "")))
                .collect(Collectors.joining());
    }
}
*/
