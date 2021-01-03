/*
When you divide the successive powers of 10 by 13
you get the following remainders of the integer divisions:

        1, 10, 9, 12, 3, 4.

Then the whole pattern repeats.

Hence the following method:

Multiply the right most digit of the number with the left most number in the sequence shown above,
the second right most digit to the second left most digit of the number in the sequence.
The cycle goes on and you sum all these products.
Repeat this process until the sequence of sums is stationary.

...........................................................................

Example: What is the remainder when 1234567 is divided by 13?

        7×1 + 6×10 + 5×9 + 4×12 + 3×3 + 2×4 + 1×1 = 178

We repeat the process with 178:

        8x1 + 7x10 + 1x9 = 87

and again with 87:

        7x1 + 8x10 = 87

...........................................................................

From now on the sequence is stationary and the remainder of 1234567 by 13
is the same as the remainder of 87 by 13:
9

Call thirt the function which processes this sequence of operations on an integer n (>=0).
thirt will return the stationary number.

        thirt(1234567) calculates 178, then 87, then 87 and returns 87.

        thirt(321) calculates 48, 48 and returns 48
*/

import java.util.List;
import java.util.stream.IntStream;

/*
class Thirteen {
    public static long thirt(long n) {
        var pattern = List.of(1, 10, 9, 12, 3, 4);
        var nString = String.valueOf(n);
        var nLength = nString.length();

        var sum = IntStream.range(0, nLength)
                .map(i -> pattern.get(i % pattern.size()) * Character
                        .getNumericValue(nString.charAt(nLength - i - 1)))
                .sum();

        return sum == n ? sum : thirt(sum);
    }
}*/

/*
class Thirteen {
    static List<Integer> pattern = List.of(1, 10, 9, 12, 3, 4);

    public static long thirt(long n) {
        var nString = String.valueOf(n);
        var nLength = nString.length();

        var sum = IntStream.range(0, nLength)
                .map(i -> pattern.get(i % pattern.size()) * Character
                        .getNumericValue(nString.charAt(nLength - i - 1)))
                .sum();

        return sum == n ? sum : thirt(sum);
    }
}
*/

class Thirteen {
    static int[] arr = {1, 10, 9, 12, 3, 4};

    public static long thirt(long n) {
        long sum = 0;
        long ans = n;

        for (int i = 0; ans > 0; i++) {
            sum += (ans % 10) * arr[i % arr.length];
            ans /= 10;
        }
        return sum == n ? sum : thirt(sum);
    }
}