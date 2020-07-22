/*
Determine the total number of digits in the integer (n>=0) given as input to the function.
For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits.
Be careful to avoid overflows/underflows.

All inputs will be valid.
*/

/*
public class DecTools {
    public static int Digits(long n) {
        if (n == 0) return 1;
        int decimalCount = 0;
        while (n > 0) {
            n /= 10;
            decimalCount++;
        }
        return decimalCount;
    }
}

*/

/*
public class DecTools {
    public static int Digits(long n) {
        int decimalCount = 1;
        while (n >= 10) {
            n /= 10;
            decimalCount++;
        }
        return decimalCount;
    }
}
*/

public class DecTools {
    public static int Digits(long n) {
        return n < 10 ? 1 : 1 + Digits(n / 10);
    }
}
