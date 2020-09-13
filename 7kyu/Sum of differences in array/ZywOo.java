/*
Your task is to sum the differences between consecutive pairs in the array in descending order.

For example:
        sumOfDifferences([2, 1, 10])
        Returns 9

        Descending order: [10, 2, 1]

        Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

        If the array is empty or the array has only one element
        the result should be 0
*/

import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
public class ZywOo {
    public static int sumOfDifferences(int[] arr) {
        int sum = 0;

        var sorted = IntStream.of(arr).boxed()
                .sorted(Collections.reverseOrder())
                .collect(Collectors.toList());

        for (int i = 1; i < sorted.size(); i++)
            sum += (sorted.get(i - 1) - sorted.get(i));

        return sum;
    }
}
*/
/*
public class ZywOo {
    public static int sumOfDifferences(int[] arr) {
        int sum = 0;
        int[] sortedArr = IntStream.of(arr).sorted().toArray();

        for (int i = sortedArr.length - 1; i > 0; i--)
            sum += (sortedArr[i] - sortedArr[i - 1]);

        return sum;
    }
}
*/

/*
import java.util.Arrays;

public class ZywOo {
    public static int sumOfDifferences(int[] arr) {
        var stats = Arrays.stream(arr).summaryStatistics();
        return arr.length < 2 ? 0 : stats.getMax() - stats.getMin();
    }
}
*/

public class ZywOo {
    public static int sumOfDifferences(int[] arr) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int x : arr) {
            if (x < min) min = x;
            if (x > max) max = x;
        }
        return arr.length < 2 ? 0 : max - min;
    }
}
