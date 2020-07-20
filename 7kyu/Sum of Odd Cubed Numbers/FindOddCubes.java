/*
Find the sum of the odd numbers within an array, after cubing the initial integers.
The function should return null if any of the values aren't numbers.

*/

import java.util.stream.IntStream;

public class FindOddCubes {
    public static int cubeOdd(int arr[]) {
        return (int) IntStream.of(arr).filter(v -> v % 2 != 0).mapToDouble(v -> Math.pow(v, 3)).sum();
    }
}
