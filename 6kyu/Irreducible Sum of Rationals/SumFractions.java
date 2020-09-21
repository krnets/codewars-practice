/*
You will have a list of rationals in the form

        lst = [ [numer_1, denom_1] , ... , [numer_n, denom_n] ]

        or

        lst = [ (numer_1, denom_1) , ... , (numer_n, denom_n) ]

        where all numbers are positive integers.

Produce their sum N / D in an irreducible form:
this means that N and D have only 1 as a common divisor.

Return the result in the form:

        "[N, D]"

If the result is an integer (D evenly divides N) return:

        "n" Java

If the input list is empty, return

        null

Example:

        [ [1, 2], [1, 3], [1, 4] ]  -->  [13, 12]

        1/2  +  1/3  +  1/4     =      13/12
*/

import java.util.stream.Stream;

public class SumFractions {
    public static String sumFracts(int[][] l) {
        if (l.length == 0) return null;

        int denom = Stream.of(l).mapToInt(subArr -> subArr[1]).reduce(1, (a, b) -> a * b);
        int numer = Stream.of(l).mapToInt(subArr -> subArr[0] * denom / subArr[1]).sum();
        int gcd = GCD(numer, denom);

        return gcd == denom ? String.valueOf(numer / denom) : String.format("[%d, %d]", numer / gcd, denom / gcd);
    }

    private static int GCD(int a, int b) {
        return b > 0 ? GCD(b, a % b) : a;
    }
}

