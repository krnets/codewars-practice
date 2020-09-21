/*
In this Kata, you will be given an integer array and your task is
to return the sum of elements occupying prime-numbered indices.

        The first element of the array is at index 0.
*/

/*
class Solution {
    public static int solve(int[] arr) {
        int sumPrimeNumIdx = 0;

        for (int i = 0; i < arr.length; i++) {
            if (isPrime(i))
                sumPrimeNumIdx += arr[i];
        }
        return sumPrimeNumIdx;
    }

    private static boolean isPrime(int n) {
        if (n < 2) return false;
        if (n < 4) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
*/

class Solution {
    public static int solve(int[] arr) {
        int sumPrimeNumIdx = 0;

        for (int i = 0; i < arr.length; i++) {
            if (isPrime(i))
                sumPrimeNumIdx += arr[i];
        }
        return sumPrimeNumIdx;
    }

    private static boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0)
                return false;
        }
        return n > 1;
    }
}


/*
import java.math.BigInteger;
import java.util.stream.IntStream;

class Solution {
    public static int solve(int[] arr) {
        return IntStream.range(0, arr.length)
                .map(i -> BigInteger.valueOf(i).isProbablePrime(8) ? arr[i] : 0)
                .sum();
    }
}
*/
