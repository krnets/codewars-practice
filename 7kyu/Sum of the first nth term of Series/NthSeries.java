/*
Write a function which returns the sum of following series upto nth term(parameter).

        Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

        Rules:
        You need to round the answer to 2 decimal places and return it as String.

        If the given value is 0 then it should return 0.00

        You will only be given Natural Numbers as arguments.

        SeriesSum(1) => 1 = "1.00"
        SeriesSum(2) => 1 + 1/4 = "1.25"
        SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
*/

import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.stream.IntStream;

/*
public class NthSeries {
    public static String seriesSum(int n) {
        var arr = new double[n];
        for (int i = 0; i < n; i++)
            arr[i] = 1.0 / (3 * i + 1);
        double result = Arrays.stream(arr).sum();
        return new DecimalFormat("#0.00").format(result);
    }
}
*/
/*
public class NthSeries {
    public static String seriesSum(int n) {
        var arr = new double[n];
        for (int i = 0; i < n; i++)
            arr[i] = 1.0 / (3 * i + 1);
        double result = Arrays.stream(arr).sum();
        return String.format("%.2f", result);
    }
}*/
/*
public class NthSeries {
    public static String seriesSum(int n) {
        double sum = 0;
        for (int i = 0; i < n; i++)
            sum += 1.0 / (3 * i + 1);
        return String.format("%.2f", sum);
    }
}
*/
/*
public class NthSeries {
    public static String seriesSum(int n) {
        return String.format("%.2f", IntStream.range(0, n).mapToDouble(v -> 1.0 / (3 * v + 1)).sum());
    }
}
*/
public class NthSeries {
    public static String seriesSum(int n) {
        var result = IntStream.range(0, n)
                .mapToDouble(i -> 1.0 / (3 * i + 1))
                .sum();
        return String.format("%.2f", result);
    }
}
