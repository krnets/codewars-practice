/*
Strong number is the number that the sum of the factorial of its digits is equal to number itself.

        For example: 145, since

        1! + 4! + 5! = 1 + 24 + 120 = 145

        So, 145 is a Strong number.

Task:   Given a number, Find if it is Strong or not.
Notes:  Number passed is always Positive.
        Return the result as String

Input >> Output Examples
        strong_num(1) ==> return "STRONG!!!!"
        Explanation:
        Since , the sum of its digits' factorial of (1) is equal to number itself (1) ,
        Then its a Strong .

        strong_num(123) ==> return "Not Strong !!"
        Explanation:
        Since the sum of its digits' factorial of 1! + 2! + 3! = 9 is not equal to number itself (123) ,
        Then it's Not Strong .

        strong_num(2)  ==>  return "STRONG!!!!"
        Explanation:
        Since the sum of its digits' factorial of 2! = 2 is equal to number itself (2) ,
        Then its a Strong .

        strong_num(150) ==> return "Not Strong !!"
        Explanation:
        Since the sum of its digits' factorial of 1! + 5! + 0! = 122 is not equal to number itself (150),
        Then it's Not Strong .
*/

/*
import java.util.Arrays;

public class StrongNumber {
    public static String isStrongNumber(int num) {
        long result = Arrays.stream(String.valueOf(num).split(""))
                .map(x -> factorial(Integer.parseInt(x)))
                .mapToLong(i -> i)
                .sum();
        return result == num ? "STRONG!!!!" : "Not Strong !!";
    }

    private static long factorial(int num) {
        return num == 0 ? 1 : num * factorial(num - 1);
    }
}*/

/*
import java.util.function.IntUnaryOperator;
import java.util.stream.IntStream;

public class StrongNumber {
    private static IntUnaryOperator factorial = d -> IntStream.rangeClosed(1, d).reduce(1, (a, b) -> a * b);

    public static String isStrongNumber(int num) {
        return num == String.valueOf(num).chars()
                .map(c -> Character.digit(c, 10))
                .map(d -> IntStream.rangeClosed(1, d).reduce(1, (a, b) -> a * b))
                .sum() ? "STRONG!!!!" : "Not Strong !!";
    }
}
*/

/*
public class StrongNumber {
    public static String isStrongNumber(int num) {
        return num == String.valueOf(num).chars()
                .map(c -> Character.digit(c, 10))
                .map(d -> IntStream.rangeClosed(1, d).reduce(1, (a, b) -> a * b))
                .sum() ? "STRONG!!!!" : "Not Strong !!";
    }
}
*/

import java.util.stream.IntStream;

public class StrongNumber {
    public static String isStrongNumber(int num) {
        return num == String.valueOf(num).chars()
                .map(Character::getNumericValue)
                .map(d -> IntStream.rangeClosed(1, d).reduce(1, (a, b) -> a * b))
                .sum() ? "STRONG!!!!" : "Not Strong !!";
    }
}
