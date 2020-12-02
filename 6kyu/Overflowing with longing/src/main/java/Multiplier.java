/*
public class Multiplier {
    public static long multiply(long a, long b) {
        return Math.multiplyExact(a, b);
    }
}*/

import java.math.BigInteger;

public class Multiplier {
    public static long multiply(long a, long b) {
        return BigInteger.valueOf(a).multiply(BigInteger.valueOf(b)).longValueExact();
    }
}

/*
public class Multiplier {

    static BigInteger min = BigInteger.valueOf(Long.MIN_VALUE);
    static BigInteger max = BigInteger.valueOf(Long.MAX_VALUE);

    public static long multiply(long a, long b) {
        BigInteger r = BigInteger.valueOf(a).multiply(BigInteger.valueOf(b));

        if (r.compareTo(min) < 0 || r.compareTo(max) > 0) {
            throw new ArithmeticException();
        }
        return a * b;
    }
}
*/
