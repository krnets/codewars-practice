/*
Given a list of digits, return the smallest number that could be formed from these digits,
using the digits only once (ignore duplicates).

Notes: Only positive integers will be passed to the function (> 0 ), no negatives or zeros.

Input >> Output Examples

        minValue ({1, 3, 1})  ==> return (13)
        (13) is the minimum number could be formed from {1, 3, 1} , Without duplications

        minValue({5, 7, 5, 9, 7})  ==> return (579)
        (579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications

        minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
        (134679) is the minimum number could be formed from {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications
*/

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
public class Minimum {
    public static int minValue(int[] values) {
        return Integer.parseInt(IntStream.of(values)
                .distinct()
                .sorted()
                .mapToObj(String::valueOf)
                .collect(Collectors.joining()));
    }
}*/
/*
public class Minimum {
    public static int minValue(int[] values) {
        return Arrays.stream(values)
                .distinct()
                .sorted()
                .reduce(0, (a, b) -> 10 * a + b);
    }
}
*/
public class Minimum {
    public static int minValue(int[] values) {
        return IntStream.of(values).distinct().sorted().reduce(0, (a, b) -> 10 * a + b);
    }
}
