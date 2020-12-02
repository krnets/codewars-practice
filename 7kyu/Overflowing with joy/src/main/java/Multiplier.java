/*
public class Multiplier {
    public static int multiply(int a, int b) {
        return Math.multiplyExact(a, b);
    }
}
*/

/*
public class Multiplier {
    public static int multiply(int a, int b) {
        long result = (long) a * b;

        if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
//      if (result != (a * b)) {
            throw new ArithmeticException("multiplication resulted in integer overflow");
        }
        return (int) result;
    }
}
*/

public class Multiplier {
    public static int multiply(int a, int b) {
        int result = a * b;

        if (result != (long) a * b) {
            throw new ArithmeticException("multiplication resulted in integer overflow");
        }
        return result;
    }
}
