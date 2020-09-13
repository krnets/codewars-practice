/*
You're working in a number zoo, and it seems that one of the numbers has gone missing!

Zoo workers have no idea what number is missing, and are too incompetent to figure it out,
so they're hiring you to do it for them.

In case the zoo loses another number, they want your program to work regardless of
how many numbers there are in total.

Task:
        Write a function that takes a shuffled list of unique numbers from 1 to n
        with one element missing (which can be any number including n).
        Return this missing number.

Note: huge lists will be tested.

Examples:

        [1, 3, 4]  =>  2
        [1, 2, 3]  =>  4
        [4, 2, 3]  =>  1
*/

import java.util.stream.IntStream;

/*
public class NumberZooPatrol {
    public static int findMissingNumber(int[] numbers) {
        var max = IntStream.of(numbers).max().orElse(0);
        var arraySum = IntStream.of(numbers).sum();
        var rangeSum = IntStream.rangeClosed(1, max).sum();
        var diff = rangeSum - arraySum;
        return diff == 0 ? max + 1 : diff;
    }
}*/

/*
public class NumberZooPatrol {
    public static int findMissingNumber(int[] numbers) {
        long n = numbers.length + 1;

        return (int) ((n * (n + 1) / 2) - IntStream.of(numbers).sum());
    }
}
*/

public class NumberZooPatrol {
    public static int findMissingNumber(int[] numbers) {
        long n = numbers.length + 1;
        long sum = IntStream.of(numbers).sum();

        return (int) ((n * (n + 1) / 2) - sum);
    }
}
