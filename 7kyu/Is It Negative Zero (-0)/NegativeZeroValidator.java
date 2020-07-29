/*
There exist two zeroes: +0 (or just 0) and -0.

Write a function that returns true if the input number is -0 and false otherwise.
*/
/*
public class NegativeZeroValidator {
    public static boolean isNegativeZero(float n) {
        return Float.floatToIntBits(n) == Integer.MIN_VALUE;
    }
}*/
public class NegativeZeroValidator {
    public static boolean isNegativeZero(float n) {
        return Float.NEGATIVE_INFINITY == 1 / n;
    }
}
