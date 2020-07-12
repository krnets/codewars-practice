/*
In this little assignment you are given a string of space separated numbers, return the highest and lowest number.
        Example:

        highAndLow("1 2 3 4 5")  // return "5 1"
        highAndLow("1 2 -3 4 5") // return "5 -3"
        highAndLow("1 9 3 4 -5") // return "9 -5"

        Notes:

        All numbers are valid Int32, no need to validate them.
        There will always be at least one number in the input string.
        Output string must be two numbers separated by a single space, and highest number is first.
*/

import java.util.Arrays;

/*
public class Kata {
    public static String highAndLow(String numbers) {
        var splitNumbers = numbers.split(" ");
        int highest = Integer.MIN_VALUE;
        int lowest = Integer.MAX_VALUE;
        for (var num : splitNumbers) {
            int n = Integer.parseInt(num);
            if (n > highest)
                highest = n;
            if (n < lowest)
                lowest = n;
        }
        return highest + " " + lowest;
    }
}*/
public class Kata {
    public static String highAndLow(String numbers) {
        var stats = Arrays.stream(numbers.split(" ")).mapToInt(Integer::parseInt).summaryStatistics();
        return stats.getMax() + " " + stats.getMin();
    }
}
