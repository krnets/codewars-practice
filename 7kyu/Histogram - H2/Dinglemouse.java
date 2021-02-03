/*
A 6-sided die is rolled a number of times and the results are plotted as percentages
in a character-based horizontal histogram.

Example:

        6|██ 5%
        5|
        4|███████ 15%
        3|███████████████████████████████████ 70%
        2|█ 3%
        1|███ 7%

Task:   You will be passed the dice value frequencies, and your task is to write the code
        to return a string representing a histogram, so that when it is printed it has
        the same format as the example.

Notes:  There are no trailing spaces on the lines
        All lines (including the last) end with a newline \n
        The percentage is displayed beside each bar except where it is 0%
        The total number of rolls varies, but won't exceed 10,000
        The bar lengths are scaled so that 100% = 50 x bar characters
        The bar character is █, which is the Unicode U+2588 char
        When calculating percentages and bar lengths always floor/truncate to the nearest integer
*/


import java.util.Arrays;

public class Dinglemouse {
    public static String histogram(final int[] results) {
        var out = new StringBuilder();
        int sum = Arrays.stream(results).sum();

        for (int i = results.length - 1; i >= 0; i--) {
            out.append(i + 1);
            out.append("|");
            if (results[i] > 0) {
                int percent = results[i] * 100 / sum;
                out.append("\u2588".repeat(percent / 2));
                out.append(" ");
                out.append(percent);
                out.append("%");
            }
            out.append("\n");
        }
        return out.toString();
    }
}


/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Dinglemouse {
    public static String histogram(final int[] results) {
        return IntStream.range(0, results.length).map(i -> results.length - i)
                .mapToObj(i -> String.format("%d|%s%s%\n", i, "\u2588".repeat(results[i - 1]),
                        (results[i - 1] > 0 ? " " + results[i - 1] : "")))
                .collect(Collectors.joining());
    }
}
