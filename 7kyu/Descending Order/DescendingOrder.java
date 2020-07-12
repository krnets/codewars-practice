/*
Your task is to make a function that can take any non-negative integer as a argument
and return it with its digits in descending order. Essentially, rearrange the digits
to create the highest possible number.

        Input: 42145 Output: 54421
        Input: 145263 Output: 654321
        Input: 123456789 Output: 987654321
*/

import java.util.Comparator;
import java.util.stream.Collectors;

/*
public class DescendingOrder {
    public static int sortDesc(final int num) {
        var sortedNum = Arrays.stream(String.valueOf(num).split(""))
                .map(Integer::parseInt)
                .sorted()
                .map(String::valueOf)
                .collect(Collectors.joining(""));
        return Integer.parseInt(String.valueOf(new StringBuilder().append(sortedNum).reverse()));
    }
}
*/

public class DescendingOrder {
    public static int sortDesc(final int num) {
        return Integer.parseInt(String.valueOf(num).chars()
                .mapToObj(v -> String.valueOf(Character.getNumericValue(v)))
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.joining()));
    }
}