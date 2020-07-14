/*
In the following 6 digit number:

        283910

        91 is the greatest sequence of 2 consecutive digits.

        In the following 10 digit number:

        1234567890

        67890 is the greatest sequence of 5 consecutive digits.

        Complete the solution so that it returns the greatest sequence of five consecutive digits
        found within the number given. The number will be passed in as a string of only digits.
        It should return a five digit integer. The number passed may be as large as 1000 digits.

        Adapted from ProjectEuler.net
*/

import java.util.stream.IntStream;

/*
public class LargestFiveDigitNumber {
    public static int solve(final String digits) {
        var nums = new int[digits.length() - 4];
        for (int i = 0; i < digits.length() - 4; i++) {
            nums[i] = Integer.parseInt(digits.substring(i, i + 5));
        }
        return IntStream.of(nums).max().getAsInt();
    }
}*/

public class LargestFiveDigitNumber {
    public static int solve(final String digits) {
        return IntStream.range(0, digits.length() - 4)
                .mapToObj(i -> digits.substring(i, i + 5))
                .mapToInt(Integer::parseInt)
                .max()
                .orElse(0);
    }
}
