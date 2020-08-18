/*
The number 89 is the first integer with more than one digit that fulfills the property
partially introduced in the title of this kata. What's the use of saying "Eureka"?
Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:

        sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

        sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

If there are no numbers of this kind in the range [a, b] the function should output an empty list.

        sum_dig_pow(90, 100) == []
*/

import java.util.ArrayList;
import java.util.List;

public class SumDigPower {
    public static List<Long> sumDigPow(long a, long b) {
        var result = new ArrayList<Long>();
        for (long i = a; i < b; i++) {
            var strNum = String.valueOf(i);
            int sum = 0;
            for (int j = 0; j < strNum.length(); j++) {
                sum += Math.pow(strNum.charAt(j) - '0', j + 1);
            }
            if (sum == i)
                result.add(i);
        }
        return result;
    }
}

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

public class SumDigPower {
    public static List<Long> sumDigPow(long a, long b) {
        return LongStream.rangeClosed(a, b)
                .filter(i -> isValid(i))
                .boxed()
                .collect(Collectors.toList());
    }

    private static boolean isValid(long n) {
        var strNum = String.valueOf(n);
        return IntStream.range(0, strNum.length())
                .mapToDouble(i -> Math.pow(strNum.charAt(i) - '0', i + 1))
                .sum() == n;
    }
}
*/
