/*
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it.
If you have an empty array, you need to return it.

        sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
*/

import java.util.Arrays;

/*
public class Kata {
    public static int[] sortArray(int[] array) {
        int[] odd = Arrays.stream(array).filter(x -> x % 2 != 0).sorted().toArray();

        for (int i = 0, j = 0; i < array.length; i++) {
            if (array[i] % 2 != 0) {
                array[i] = odd[j];
                j++;
            }
        }
        return array;
    }
}*/
public class Kata {
    public static int[] sortArray(int[] array) {
        int[] sortedOdd = Arrays.stream(array).filter(x -> x % 2 != 0).sorted().toArray();

        for (int i = 0, j = 0; i < array.length; i++) {
            if (array[i] % 2 != 0)
                array[i] = sortedOdd[j++];
        }
        return array;
    }
}
/*
import java.util.function.IntPredicate;
import java.util.stream.IntStream;

public class Kata {
    public static IntPredicate isOdd = n -> n % 2 != 0;

    public static int[] sortArray(int[] array) {
        var oddSortedIter = IntStream.of(array)
                .filter(isOdd)
                .sorted()
                .iterator();

        return IntStream.of(array)
                .map(x -> isOdd.test(x) ? oddSortedIter.next() : x)
                .toArray();
    }
}
*/

