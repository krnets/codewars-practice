/*
Given a triangle of consecutive odd numbers:

        1
        3     5
        7     9    11
        13    15    17    19
        21    23    25    27    29
        ...

        find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

        oddRow(1)  ==  [1]
        oddRow(2)  ==  [3, 5]
        oddRow(3)  ==  [7, 9, 11]
        oddRow(13) ==  [157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181]

        Note: your code should be optimized to handle big inputs.
*/


/*
import java.util.stream.LongStream;

public class UserSolution {
    public static long[] oddRow(int n) {
        return LongStream.iterate((long) n * (n - 1) + 1, i -> i + 2).limit(n).toArray();
    }
}*/

public class UserSolution {
    public static long[] oddRow(int n) {
        var row = new long[n];
        var base = (long) (n + Math.pow((n - 1), 2));

        for (int i = 0; i < n; i++) {
            row[i] = base;
            base += 2;
        }
        return row;
    }
}
