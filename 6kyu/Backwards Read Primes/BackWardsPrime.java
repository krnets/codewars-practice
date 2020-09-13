/*
Backwards Read Primes are primes that when read backwards in base 10
(from right to left) are a different prime.
(This rules out primes which are palindromes.)

Examples:

        13 17 31 37 71 73 are Backwards Read Primes

        13 is such because it's prime and read from right to left writes 31 which is prime too.
        Same for the others.

Task

        Find all Backwards Read Primes between two positive given numbers (both inclusive),
        the second one always being greater than or equal to the first one.
        The resulting array or the resulting string will be ordered following the natural order
        of the prime numbers.

        backwardsPrime(2, 100) => "13 17 31 37 71 73 79 97"
        backwardsPrime(9900, 10000) => "9923 9931 9941 9967"
        backwardsPrime(501, 599) => ""
*/

import java.math.BigInteger;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

public class BackWardsPrime {
    private static boolean isPrime(long num) {
        return num > 1 && BigInteger.valueOf(num).isProbablePrime((int) Math.log(num));
    }

    private static boolean isBackwardsPrime(long num) {
        String reversed = new StringBuilder(num + "").reverse().toString();
        return isPrime(Long.parseLong(reversed));
    }

    private static boolean isPalindrome(long num) {
        String reversed = new StringBuilder(num + "").reverse().toString();
        return num == Long.parseLong(reversed);
    }

    public static String backwardsPrime(long start, long end) {
        return LongStream.rangeClosed(Math.max(start, 12), end)
                .filter(num -> isPrime(num))
                .filter(num -> isBackwardsPrime(num))
                .filter(num -> !BackWardsPrime.isPalindrome(num))
                .mapToObj(Long::toString)
                .collect(Collectors.joining(" "));
    }
}

