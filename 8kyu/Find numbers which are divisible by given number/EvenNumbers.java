import java.util.stream.IntStream;

/*
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
First argument is an array of numbers and the second is the divisor.

        divisibleBy([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
*/
public class EvenNumbers {
    public static int[] divisibleBy(int[] numbers, int divider) {
        return IntStream.of(numbers).filter(v -> v % divider == 0).toArray();
    }
}