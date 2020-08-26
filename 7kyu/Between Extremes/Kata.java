/*
Given an array of numbers, return the difference between the largest and smallest values.

For example:

        [23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).

        [1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1).

The array will contain a minimum of two elements.
Input data range guarantees that max-min will cause no integer overflow.
*/

import java.util.stream.IntStream;

/*
public class Kata {
    public static int betweenExtremes(int[] numbers) {
        return IntStream.of(numbers).max().orElse(0) - IntStream.of(numbers).min().orElse(0);
    }
}*/


/*
public class Kata {
    public static int betweenExtremes(int[] numbers) {
        var stats = IntStream.of(numbers).summaryStatistics();
        return stats.getMax() - stats.getMin();
    }
}
*/

public class Kata {
    public static int betweenExtremes(int[] numbers) {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for (int n : numbers) {
            max = Math.max(max, n);
            min = Math.min(min, n);
        }
        return max - min;
    }
}

/*
public class Kata {
    public static int betweenExtremes(int[] numbers) {
        int max = numbers[0];
        int min = numbers[0];

        for (int n : numbers) {
            max = Math.max(max, n);
            min = Math.min(min, n);
        }
        return max - min;
    }
}
*/
