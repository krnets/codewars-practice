/*
Disarium number is the number that
The sum of its digits powered with their respective positions is equal to the number itself.

Task:   Given a number, Find if it is Disarium or not .

Notes:  Number passed is always Positive. Return the result as String

Input >> Output Examples

        disariumNumber(89) ==> return "Disarium !!"
        Explanation:
        Since , 81 + 92 = 89 , thus output is "Disarium !!"

        disariumNumber(564) ==> return "Not !!"
        Explanation:
        Since , 51 + 62 + 43 = 105 != 564 , thus output is "Not !!"
*/
/*

public class Solution {
    public static String disariumNumber(int number) {
        var strNum = String.valueOf(number);
        int acc = 0;
        for (int i = 0; i < strNum.length(); i++)
            acc += Math.pow(Integer.parseInt(String.valueOf(strNum.charAt(i))), i + 1);
        return acc == number ? "Disarium !!" : "Not !!";
    }
}*/

import java.util.stream.IntStream;

/*
public class Solution {
    public static String disariumNumber(int number) {
        int[] digits = String.valueOf(number).chars().map(Character::getNumericValue).toArray();

        return IntStream.range(0, digits.length)
                .map(i -> (int) Math.pow(digits[i], i + 1))
                .sum() == number ? "Disarium !!" : "Not !!";
    }
}
*/
public class Solution {
    public static String disariumNumber(int number) {
        var strNum = String.valueOf(number);
        return IntStream.range(0, strNum.length())
                .map(i -> (int) Math.pow(strNum.charAt(i) - '0', i + 1))
                .sum() == number ? "Disarium !!" : "Not !!";
    }
}
