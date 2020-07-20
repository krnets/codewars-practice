/*
In this kata, you must create a function powers/Powers that takes an array,
and returns the number of subsets possible to create from that list.
In other words, counts the power sets.

        For instance

        powers([1,2,3]) => 8

        ...due to...

        powers([1,2,3]) =>
        [[],
        [1],
        [2],
        [3],
        [1,2],
        [2,3],
        [1,3],
        [1,2,3]]

        Your function should be able to count sets up to the size of 500, so watch out;
        pretty big numbers occur there!

        For comparison, my Haskell solution can compute the number of sets for an array of length 90 000
        in less than a second, so be quick!

        You should treat each array passed as a set of unique values for this kata.

        ###Examples:

        Powers.powers(new int[]{});        // 1
        Powers.powers(new int[]{1});       // 2
        Powers.powers(new int[]{1,2});     // 4
        Powers.powers(new int[]{1,2,3,4}); // 16
*/

import java.math.BigDecimal;
import java.math.BigInteger;

/*
public class Powers {
    public static BigInteger powers(int[] list) {
        var res = BigInteger.valueOf(0);
        for (int i = 1; i <= list.length; i++)
            res = res.add(factorial(list.length).divide(factorial(list.length - i).multiply(factorial(i))));
        return res.add(BigInteger.valueOf(1));
    }

    private static BigInteger factorial(final int n) {
        if (n == 0) return BigInteger.ONE;
        return BigInteger.valueOf(n).multiply(factorial(n - 1));
    }
}*/

/*
public class Powers {
    public static BigInteger powers(int[] list) {
        return BigInteger.ONE.shiftLeft(list.length);
    }
}
*/

/*
public class Powers {
    public static BigInteger powers(int[] list) {
        return BigInteger.ZERO.setBit(list.length);
    }
}
*/

/*
public class Powers {
    public static BigInteger powers(int[] list) {
        return BigInteger.TWO.pow(list.length);
    }
}
*/

public class Powers {
    public static BigInteger powers(int[] list) {
        return new BigDecimal(Math.pow(2, list.length)).toBigInteger();
    }
}
