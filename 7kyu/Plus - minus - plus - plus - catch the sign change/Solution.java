/*
Count how often sign changes in array.

Result : number from 0 to ... . Empty array returns 0

Example
        const arr = [1, -3, -4, 0, 5];

        | elem | count |
        |------|-------|
        |  1   |  0    |
        | -3   |  1    |
        | -4   |  1    |
        |  0   |  2    |
        |  5   |  2    |

        catchSignChange(arr) == 2;
*/


import java.util.stream.IntStream;

public class Solution {
    public static int signChange(int[] arr) {
        return (int) IntStream.range(1, arr.length)
                .filter(i -> (arr[i] ^ arr[i - 1]) < 0)
                .count();
    }
}

/*
public class Solution {
    public static int signChange(int[] arr) {
        return IntStream.range(1, arr.length)
                .map(i -> (arr[i] ^ arr[i - 1]) < 0 ? 1 : 0)
                .sum();
    }
}
*/
