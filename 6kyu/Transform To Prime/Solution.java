/*
Given a List [] of n integers , find minimum number to be inserted in a list,
so that sum of all elements of list should equal the closest prime number .

Notes

        List size is at least 2 .

        List's numbers will only positives (n > 0) .

        Repetition of numbers in the list could occur .

        The newer list's sum should equal the closest prime number .

Input >> Output Examples

        1- minimumNumber ({3,1,2}) ==> return (1)
        Since , the sum of the list's elements equal to (6) ,
        the minimum number to be inserted to transform the sum to prime number is (1) ,
        which will make *the sum of the List** equal the closest prime number (7)* .

        2-  minimumNumber ({2,12,8,4,6}) ==> return (5)
        Since , the sum of the list's elements equal to (32) ,
        the minimum number to be inserted to transform the sum to prime number is (5) ,
        which will make *the sum of the List** equal the closest prime number (37)* .

        3- minimumNumber ({50,39,49,6,17,28}) ==> return (2)
        Since , the sum of the list's elements equal to (189) ,
        the minimum number to be inserted to transform the sum to prime number is (2) ,
        which will make *the sum of the List** equal the closest prime number (191)* .
*/

/*
import java.math.BigInteger;
import java.util.stream.IntStream;

public class Solution {
    public static int minimumNumber(int[] numbers) {
        int sum = IntStream.of(numbers).sum();
        int nextPrime = BigInteger.valueOf(sum - 1L).nextProbablePrime().intValue();

        return nextPrime - sum;
    }
}
*/

import java.util.stream.IntStream;

public class Solution {
    public static int minimumNumber(int[] numbers) {
        int sum = IntStream.of(numbers).sum();
        int x = (sum + 1) % 2;

        while (!isPrime(sum + x)) {
            x += 2;
        }
        return x;
    }

    private static boolean isPrime(int n) {
//        return n > 1 && BigInteger.valueOf(n).isProbablePrime((int) Math.log(n));
        if (n < 2) return false;
        if (n < 4) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}

/*
import java.util.stream.IntStream;
import com.google.common.math.IntMath;

public class Solution {
    public static int minimumNumber(int[] numbers) {
        int sum = IntStream.of(numbers).sum();
        int x = (sum + 1) % 2;

        while (!IntMath.isPrime(sum + x)) {
            x += 2;
        }
        return x;
    }
}
*/
