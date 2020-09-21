/*
There is a planet... in a galaxy far far away.
It is exactly like our planet, but it has one difference:
#The values of the digits 3 and 7 are twisted.
Our 3 means 7 on the planet Twisted-3-7.
And 7 means 3.

Your task is to create a method, that can sort an array the way it would be sorted on Twisted-3-7.

7 Examples from a friend from Twisted-3-7:

        [1,2,3,4,5,6,7,8,9] -> [1,2,7,4,5,6,3,8,9]
        [12,13,14] -> [12,14,13]
        [9,2,4,7,3] -> [2,7,4,3,9]

There is no need for a precheck.
The array will always be not null and will always contain at least one number.

You should not modify the input array
*/

/*
import java.util.function.IntUnaryOperator;
import java.util.stream.Stream;

public class Kata {
    public static Integer[] sortTwisted37(Integer[] array) {
        IntUnaryOperator swap37 = x -> Integer.parseInt(String.valueOf(x)
                .replace("3", "_")
                .replace("7", "3")
                .replace("_", "7"));

        return Stream.of(array)
                .map(swap37::applyAsInt)
                .sorted()
                .map(swap37::applyAsInt)
                .toArray(Integer[]::new);
    }
}*/

import java.util.Comparator;
import java.util.stream.Stream;

public class Kata {
    public static Integer[] sortTwisted37(Integer[] array) {
        return Stream.of(array)
                .map(String::valueOf)
                .sorted(Comparator.comparing(
                        x -> Integer.parseInt(x.replace("3", "_")
                                .replace("7", "3")
                                .replace("_", "7"))))
                .map(Integer::parseInt)
                .toArray(Integer[]::new);
    }
}
