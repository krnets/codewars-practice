/*
Balanced number is the number that * The sum of all digits to the left of the middle digit(s)
and the sum of all digits to the right of the middle digit(s) are equal*.

Task: Given a number, Find if it is Balanced or not .
*/

/*
import java.util.Arrays;

import static java.lang.Integer.parseInt;

public class Solution {
    public static String balancedNum(long number) {
        int left = 0, right = 0;
        var strNum = String.valueOf(number);
        if (strNum.length() > 2) {
            if (strNum.length() % 2 == 0) {
                left = sumDigits(parseInt(strNum.substring(0, strNum.length() / 2 - 1)));
            } else {
                left = sumDigits(parseInt(strNum.substring(0, strNum.length() / 2)));
            }
            right = sumDigits(parseInt(strNum.substring(strNum.length() / 2 + 1)));
        }
        return left == right ? "Balanced" : "Not Balanced";
    }

    private static int sumDigits(int num) {
        return Arrays.stream(String.valueOf(num).split("")).mapToInt(Integer::parseInt).sum();
    }
}
*/
/*

public class Solution {
    public static String balancedNum(long number) {
        char[] digits = Long.toString(number).toCharArray();
        long sum = 0;
        for (int i = 0; i < digits.length - i - 2; i++)
            sum += digits[i] - digits[digits.length - i - 1];
        return sum == 0 ? "Balanced" : "Not Balanced";
    }
}*/

public class Solution {
    public static String balancedNum(long number) {
        var digits = Long.toString(number);
        int sum = 0, len = digits.length();
        for (int i = 0; i < len - i - 2; i++)
            sum += digits.charAt(i) - digits.charAt(len - i - 1);
        return sum == 0 ? "Balanced" : "Not Balanced";
    }
}

/*
public class Solution {
    public static String balancedNum(long number) {
        var digits = Long.toString(number);
        int left = digits.substring(0, digits.length() / 2 - (digits.length() % 2 == 0 ? 1 : 0)).chars().sum();
        int right = digits.substring(digits.length() / 2 + 1).chars().sum();
        return left == right ? "Balanced" : "Not Balanced";
    }
}
*/
