/*
You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

        The first element of the array occupies the first 8 bits of M;
        The second element occupies next 8 bits, and so on.

        Return the obtained integer M as unsigned integer.

Note:

        the phrase "first bits of M" refers to the least significant bits of M
        the right-most bits of an integer. For further clarification see the following example.

Example

        For a = [24, 85, 0], the output should be 21784
        An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.

        After packing these into one number we get 00000000 01010101 00011000
        (spaces are placed for convenience), which equals to 21784.

Input/Output

        [input] integer array a
        Constraints: 1 ≤ a.length ≤ 4 and 0 ≤ a[i] < 256

        [output] an unsigned integer

More Challenge

        Are you a One-Liner? Please try to complete the kata in one line(no test for it)
*/

/*
import static java.lang.Integer.toBinaryString;
import static java.lang.String.format;
import static java.util.stream.Collectors.joining;
import static java.util.stream.IntStream.range;

public class Kata {
    public static long arrayPacking(int[] arr) {
        String binary = range(0, arr.length)
                .map(i -> arr.length - i - 1)
                .mapToObj(i -> format("%8s", toBinaryString(arr[i])).replaceAll(" ", "0"))
                .collect(joining());

        return Long.parseLong(binary, 2);
    }
}*/

/*
import static java.lang.Integer.toBinaryString;
import static java.lang.Long.parseLong;
import static java.lang.String.format;
import static java.util.stream.Collectors.joining;
import static java.util.stream.IntStream.range;

public class Kata {
    public static long arrayPacking(int[] arr) {
        return parseLong(range(0, arr.length)
                .mapToObj(i -> format("%8s", toBinaryString(arr[arr.length - i - 1])).replaceAll(" ", "0"))
                .collect(joining()), 2);
    }
}
*/

/*
public class Kata {
    public static long arrayPacking(int[] arr) {
        var res = 0L;

        for (int i = 0; i < arr.length; i++)
            res += arr[i] * Math.pow(2, i * 8);

        return res;
    }
}
*/

/*
public class Kata {
    public static long arrayPacking(int[] arr) {
        return java.util.stream.IntStream.range(0, arr.length)
                .mapToLong(i -> (long) (arr[i] * Math.pow(2, i * 8)))
                .sum();
    }
}
*/

import static java.util.stream.IntStream.range;

public class Kata {
    public static long arrayPacking(int[] arr) {
        return range(0, arr.length).mapToLong(i -> (long) (arr[i] * Math.pow(2, i * Byte.SIZE))).sum();
    }
}

/*
public class Kata {
    public static long arrayPacking(int[] arr) {
        var res = 0L;

        for (int i = 0; i < arr.length; i++)
            res += arr[i] * Math.pow(2, i * Byte.SIZE);

        return res;
    }
}
*/

/*
public class Kata {
    public static long arrayPacking(int[] arr) {
        long result = 0;
        int shift = 0;
        for (long x : arr) {
            result = result | x << shift;
            shift += Byte.SIZE;
        }
        return result;
    }
}
*/
