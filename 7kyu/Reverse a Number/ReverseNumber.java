/*
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

        Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
        Examples

        123 ->  321
        -456 -> -654
        1000 ->    1
*/

/*
import static java.lang.Integer.parseInt;
import static java.lang.Math.*;
import static java.lang.String.valueOf;

public class ReverseNumber {
    public static int reverse(int number) {
        return parseInt(valueOf(new StringBuilder(valueOf(abs(number))).reverse())) * (int) signum(number);
    }
}
*/

public class ReverseNumber {
    public static int reverse(int number) {
        return Integer.parseInt("" + new StringBuilder("" + Math.abs(number)).reverse()) * Integer.signum(number);
    }
}

/*
public class ReverseNumber {
    public static int reverse(int number) {
        int output = 0;
        int sign = number < 0 ? -1 : 1;
        number = Math.abs(number);
        while (number > 0) {
            output = output * 10 + number % 10;
            number /= 10;
        }
        return output * sign;
    }
}
*/

/*
public class ReverseNumber {
    public static int reverse(int number) {
        return number < 0 ? -reverse(-number) : Integer
                .parseInt(new StringBuilder().append(number).reverse().toString());
    }
}
*/

/*
public class ReverseNumber {
    public static int reverse(int number) {
        int result = 0;
        while (number != 0) {
            result = result * 10 + number % 10;
            number /= 10;
        }
        return result;
    }
}
*/
